#!/usr/bin/env python3
"""Raggruppa le righe per-data dello stesso spettacolo in un unico evento.

Problema: le tournée teatrali e le residency arrivano come una riga per data
(es. 62 righe per lo stesso musical), quindi la lista pubblica sembra piena
di duplicati e le pagine SEO sono migliaia di paginette sottili.

Questo step (da eseguire DOPO dedup.py e PRIMA di build_event_pages.py)
fonde le righe che rappresentano lo stesso spettacolo:
- stessa citta'
- stessa categoria
- venue equivalente: il nome venue viene tagliato a " (", " - ", " – "
  (varianti tipo "Teatro Principe (Allo Sbagliato)" / "Teatro Principe – Allo
  Sbagliato" / "Teatro Manzoni - ING" collassano sulla stessa chiave)
- titolo equivalente: token uguali, oppure un insieme di token contenuto
  nell'altro (min 3 token), oppure Jaccard >= 0.75

L'evento fuso conserva: date ordinate in "dates" [{d, t}], startDate=min,
endDate=max, descrizione piu' lunga, fonti unite, coordinate dalla prima
riga che le ha. dateLabel viene rigenerata ("dal ... al ... · N date").

Uso: group_shows.py [--dry-run] [path events.json]
Idempotente: le righe gia' dotate di "dates" partecipano con tutte le loro date.
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict
from datetime import date

MONTHS = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno',
          'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']
WDAYS = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']


def norm(s):
    s = unicodedata.normalize('NFKD', (s or '').lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def venue_keys(v):
    """Chiavi bucket per un venue: nome completo normalizzato (token ordinati,
    senza parentesi e senza token rumore) e primo segmento prima del trattino.
    Le varianti con ordine invertito ("Allo Sbagliato – Teatro Principe")
    condividono la chiave completa; quelle con suffisso ("Teatro Manzoni - ING")
    condividono la chiave del primo segmento."""
    v = (v or '').strip()
    v = re.sub(r'\([^)]*\)', ' ', v)
    full = norm(v)
    full_key = ' '.join(sorted(set(full.split()) - {'ing', 'spa', 'srl', 'snc'}))
    first = re.split(r'\s-\s|\s–\s', v)[0]
    first_key = ' '.join(sorted(set(norm(first).split()) - {'ing', 'spa', 'srl', 'snc'}))
    return {full_key, first_key} - {''}


def tokens(s):
    # le parentesi nei titoli sono quasi sempre annotazioni (residency,
    # seconda data, replica): non distinguono lo spettacolo
    s = re.sub(r'\([^)]*\)', ' ', s or '')
    return set(norm(s).split()) - {'il', 'lo', 'la', 'i', 'gli', 'le', 'di', 'de', 'del', 'della', 'e'}


def title_match(a, b):
    if a == b:
        return True
    if len(a) >= 3 and a <= b:
        return True
    if len(b) >= 3 and b <= a:
        return True
    u = a | b
    if u and len(a & b) / len(u) >= 0.75:
        return True
    return False


def fmt_day(ds):
    y, m, d = (int(x) for x in ds.split('-'))
    wd = WDAYS[date(y, m, d).weekday()]
    return f'{wd} {d} {MONTHS[m - 1]} {y}'


def fmt_short(ds):
    y, m, d = (int(x) for x in ds.split('-'))
    return f'{d} {MONTHS[m - 1]} {y}'


def main():
    dry = '--dry-run' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    path = args[0] if args else '/home/hatch/workspace/eventi-pubblico/data/events.json'
    data = json.load(open(path, encoding='utf-8'))
    events = data['events']

    buckets = defaultdict(list)
    for i, e in enumerate(events):
        for vk in venue_keys(e.get('venue')):
            buckets[(norm(e.get('city')), vk, e.get('category'))].append(i)

    parent = list(range(len(events)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    compared = 0
    for idxs in buckets.values():
        if len(idxs) < 2:
            continue
        toks = {i: tokens(events[i].get('title')) for i in idxs}
        for n, i in enumerate(idxs):
            for j in idxs[n + 1:]:
                compared += 1
                if title_match(toks[i], toks[j]):
                    union(i, j)

    clusters = defaultdict(list)
    for i in range(len(events)):
        clusters[find(i)].append(i)

    merged_events = []
    n_clusters = 0
    n_rows_in = 0
    big = []
    for root, idxs in clusters.items():
        if len(idxs) == 1:
            merged_events.append(events[idxs[0]])
            continue
        n_clusters += 1
        n_rows_in += len(idxs)
        rows = [events[i] for i in idxs]
        base = max(rows, key=lambda e: (len(e.get('details') or ''), ))
        # tutte le date (anche da righe gia' raggruppate)
        dmap = {}
        for e in rows:
            if e.get('dates'):
                for x in e['dates']:
                    dmap[x['d']] = x.get('t') or dmap.get(x['d']) or ''
            elif e.get('startDate'):
                dmap[e['startDate']] = e.get('timeLabel') or ''
        dates = [{'d': d, 't': dmap[d]} for d in sorted(dmap)]
        out = dict(base)
        out['startDate'] = dates[0]['d']
        out['endDate'] = dates[-1]['d']
        out['dates'] = dates
        times = {x['t'] for x in dates if x['t']}
        out['timeLabel'] = times.pop() if len(times) == 1 else ''
        if len(dates) > 1:
            out['dateLabel'] = (f'dal {fmt_short(dates[0]["d"])} al {fmt_short(dates[-1]["d"])}'
                                f' · {len(dates)} date')
        else:
            out['dateLabel'] = fmt_day(dates[0]['d'])
        # fonti unite per URL
        seen, sources = set(), []
        for e in rows:
            for s in (e.get('sources') or []):
                k = s.get('url') or s.get('name')
                if k not in seen:
                    seen.add(k)
                    sources.append(s)
        out['sources'] = sources
        for f in ('latitude', 'longitude', 'address', 'foodDetails', 'caveat', 'priceLabel'):
            if not out.get(f):
                for e in rows:
                    if e.get(f):
                        out[f] = e[f]
                        break
        if len(dates) >= 5:
            big.append((len(dates), out.get('title'), out.get('venue'), out.get('city')))
        merged_events.append(out)

    merged_events.sort(key=lambda e: (e.get('startDate') or '', e.get('title') or ''))
    print(f'Eventi prima: {len(events)} · dopo: {len(merged_events)} '
          f'· cluster fusi: {n_clusters} (righe assorbite: {n_rows_in - n_clusters})')
    big.sort(reverse=True)
    for n, t, v, c in big[:10]:
        print(f'  x{n:3d} {t[:50]!r} @ {v[:35]!r} ({c})')
    if not dry:
        data['events'] = merged_events
        data['count'] = len(merged_events)
        json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False)
        print('Scritto:', path)


if __name__ == '__main__':
    main()
