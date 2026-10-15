import json

WD = {"Thursday":"giovedì","Friday":"venerdì","Saturday":"sabato","Sunday":"domenica","Monday":"lunedì","Tuesday":"martedì","Wednesday":"mercoledì"}
M = {"10":"ottobre","11":"novembre"}
import datetime
def dateLabel(iso):
    d = datetime.date.fromisoformat(iso)
    en = d.strftime("%A")
    return f"{WD[en]} {d.day} {M[iso[5:7]]} {d.year}"

TM = "https://www.ticketmaster.it"
E = []
def add(title, category, start, end, time, venue, addr, city, prov, area, kind, url, details=None, caveat=None):
    E.append({
        "title": title, "category": category, "startDate": start, "endDate": end,
        "dateLabel": dateLabel(start), "timeLabel": time, "venue": venue,
        "city": city, "province": prov, "area": area, "kind": kind,
        "priceLabel": "Prezzo non pubblicato", "priceType": "unknown",
        "details": details, "foodDetails": None, "caveat": caveat, "address": addr,
        "sources": [{"name":"Ticketmaster Italia","url":url,"channel":"ticketing"}]
    })

# --- Ottobre 2026 ---
add("FABIO DE LUIGI - BIOL - In Carne e Ossa Tour","comedy","2026-10-15",None,"21:00","Teatro Lirico Giorgio Gaber","Via Larga 14, Milano","Milano","MI","milano","stand-up",f"{TM}/biglietti/fabio-de-luigi-biol-in-carne-e-ossa-tour-milano-15-10-2026/event/ruug3ocpsvd1","Show di Fabio De Luigi, tour 'In Carne e Ossa'.")
add("FABIO DE LUIGI - BIOL - In Carne e Ossa Tour","comedy","2026-10-16",None,"21:00","Teatro Lirico Giorgio Gaber","Via Larga 14, Milano","Milano","MI","milano","stand-up",f"{TM}/biglietti/fabio-de-luigi-biol-in-carne-e-ossa-tour-milano-16-10-2026/event/kdjpdoz5dozc","Show di Fabio De Luigi, tour 'In Carne e Ossa'.")
add("Jay Park Ft. LNGSHOT - Serenades & Body Rolls Tour","music","2026-10-17",None,"19:00","Fabrique","Via Gaudenzio Fantoli 9, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/jay-park-ft-lngshot-milano-17-10-2026/event/q9zp9b365mon")
add("Willie Peyote - Club Tour 2026","music","2026-10-20",None,"21:00","Fabrique","Via Gaudenzio Fantoli 9, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/willy-peyote-milano-20-10-2026/event/xwpn9rj7894t")
add("SAYF - Santissimo Tour","music","2026-10-21",None,"21:00","Alcatraz","Via Valtellina 25, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/sayf-milano-21-10-2026/event/i5z603yq40n8")
add("Enrico Brignano - Bello di Mamma Indoor","comedy","2026-10-21",None,"21:15","Teatro Clerici","Via S. Zeno 168, Brescia","Brescia","BS","lombardia","stand-up",f"{TM}/biglietti/enrico-brignano-bello-di-mamma-indoor-brescia-21-10-2026/event/qwql4egquz46","Show di Enrico Brignano, 'Bello di Mamma' versione indoor.")
add("SAYF - Santissimo Tour","music","2026-10-22",None,"21:00","Alcatraz","Via Valtellina 25, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/sayf-milano-22-10-2026/event/tndqp9s9o2uj")
add("L'Antidote | JAZZMI 2026","music","2026-10-22",None,"21:00","Santeria Toscana 31","Viale Toscana 31, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/lantidote-jazzmi-2026-milano-22-10-2026/event/635n7g1qdbsr","Nell'ambito del festival JAZZMI 2026.")
add("Songhoy Blues | JAZZMI 2026","music","2026-10-23",None,"22:00","Biko","Via Ettore Ponti 40, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/songhoy-blues-milano-23-10-2026/event/dllk3x36rxiq","Nell'ambito del festival JAZZMI 2026.")
add("Corto Alto | JAZZMI 2026","music","2026-10-24",None,"21:30","Santeria Toscana 31","Viale Toscana 31, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/corto-alto-milano-24-10-2026/event/buxybc5hgz4r","Nell'ambito del festival JAZZMI 2026.")
add("Rokia Traoré | JAZZMI 26","music","2026-10-27",None,"21:00","Alcatraz","Via Valtellina 25, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/rokia-traore-milano-27-10-2026/event/cslhv3zcj4wp","Nell'ambito del festival JAZZMI 2026.")
add("DON TOLIVER: NITROUS - OCTANE WORLD TOUR LEG 2","music","2026-10-27",None,"21:00","Unipol Forum","Via Giuseppe di Vittorio 6, Assago","Assago","MI","lombardia","concerto",f"{TM}/biglietti/don-toliver-nitrous-octane-world-tour-leg-2-assago-27-10-2026/event/ly6393czzwwd")
add("Kjartan Sveinsson, Gyda Valtýsdóttir, Bert Cools and Indrė Jurgelevičiūtė | JAZZMI 2026","music","2026-10-28",None,"21:00","Auditorium San Fedele","Via Ulrico Hoepli, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/kjartan-sveinsson-gyda-valtsdttir-bert-cools-and-indr-jurgeleviit-jazzmi-2026-milano-28-10-2026/event/rewuxahmfdvm","Nell'ambito del festival JAZZMI 2026.")
add("Paolo Fresu Quintet 'Ascensore per il Patibolo' | JAZZMI 26","music","2026-10-29",None,"21:00","Teatro Lirico Giorgio Gaber","Via Larga 14, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/paolo-fresu-quintet-ascensore-per-il-patibolo-milano-29-10-2026/event/2ofhixil342w","Nell'ambito del festival JAZZMI 2026.")
add("FABIO DE LUIGI - BIOL - In Carne e Ossa Tour","comedy","2026-10-28",None,"21:00","ChorusLife Arena","Via Carlo Serassi 26, Bergamo","Bergamo","BG","lombardia","stand-up",f"{TM}/biglietti/fabio-de-luigi-bergamo-28-10-2026/event/1i4oz9swbrxj","Show di Fabio De Luigi, tour 'In Carne e Ossa'.")
add("Niall Horan: Dinner Party Live On Tour","music","2026-10-28",None,"20:30","Unipol Forum","Via Giuseppe di Vittorio 6, Assago","Assago","MI","lombardia","concerto",f"{TM}/biglietti/niall-horan-dinner-party-live-on-tour-assago-28-10-2026/event/7zc6cew7ggtp")
add("Tommy Emmanuel | JAZZMI 2026","music","2026-10-30",None,"21:00","Teatro Dal Verme","Via S. Giovanni sul Muro 2, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/tommy-emmanuel-milano-30-10-2026/event/60q5rr243dpg","Nell'ambito del festival JAZZMI 2026.")
add("Louis Matute Large Ensemble | JAZZMI 2026","music","2026-10-30",None,"22:00","Biko","Via Ettore Ponti 40, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/louis-matute-large-ensemble-jazzmi-2026-milano-30-10-2026/event/i8al81rrclr2","Nell'ambito del festival JAZZMI 2026.")
add("Gaetano Liguori Idea Trio 'Underground' | JAZZMI 2026","music","2026-10-31",None,"12:00","Teatro dell'Arte - Triennale Milano","Viale Emilio Alemagna 6, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/gaetano-liguori-idea-trio-underground-jazzmi-2026-milano-31-10-2026/event/uadyji7hf4tc","Nell'ambito del festival JAZZMI 2026. Matinée.")
add("Enrico Intra meets Gerry Mulligan | JAZZMI 26","music","2026-10-31",None,"16:00","Teatro dell'Arte - Triennale Milano","Viale Emilio Alemagna 6, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/enrico-intra-milano-31-10-2026/event/95v0v4q2l07c","Nell'ambito del festival JAZZMI 2026.")
add("The Songs of Joni Mitchell | JAZZMI 2026","music","2026-10-31",None,"20:00","Teatro dell'Arte - Triennale Milano","Viale Emilio Alemagna 6, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/the-songs-of-joni-mitchell-milano-31-10-2026/event/elav7zbxih6o","Nell'ambito del festival JAZZMI 2026.")

# --- Novembre 2026 ---
TRI = "Teatro dell'Arte - Triennale Milano"
TRI_A = "Viale Emilio Alemagna 6, Milano"
J = "Nell'ambito del festival JAZZMI 2026."
add("Dimitri Grechi Espinoza, Aziz Senol Filiz e Guido Zorn 'Meditation on a Love Supreme' | JAZZMI 2026","music","2026-11-01",None,"16:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/dimitri-grechi-espinoza-aziz-senol-filiz-e-guido-zorn-meditation-on-a-love-supreme-jazzmi-2026-milano-01-11-2026/event/gevbmvgtyfcd",J)
add("Nate Smith | JAZZMI 2026 (ore 20:00)","music","2026-11-01",None,"20:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/nate-smith-milano-01-11-2026/event/nau82bpktnhz",J,caveat="Ticketmaster elenca due spettacoli distinti di Nate Smith il 1/11 (ore 20:00 e 22:00).")
add("Nate Smith | JAZZMI 2026 (ore 22:00)","music","2026-11-01",None,"22:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/nate-smith-milano-01-11-2026/event/yt3vccabbvfa",J,caveat="Ticketmaster elenca due spettacoli distinti di Nate Smith il 1/11 (ore 20:00 e 22:00).")
add("David Binney & Louis Cole | JAZZMI 2026","music","2026-11-03",None,"20:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/david-binney-action-trio-ft-louis-cole-and-pera-krstrasic-jazzmi-2026-milano-03-11-2026/event/dbwhhzabwtc1",J)
add("China Moses | JAZZMI 2026","music","2026-11-04",None,"21:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/china-moses-milano-04-11-2026/event/fhlk6u4ydk7c",J)
add("A New Sketches of Spain | JAZZMI 2026","music","2026-11-05",None,"20:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/a-new-sketches-of-spain-jazzmi-2026-milano-05-11-2026/event/3nh75kgje87l",J)
add("Il Festival dello Spettacolo - Biglietto giornaliero","music","2026-11-06",None,"12:00","Superstudio Più","Via Tortona 27, Milano","Milano","MI","milano","festival",f"{TM}/biglietti/il-festival-dello-spettacolo-milano-06-11-2026/event/vf9f3b4tgu2z","Festival dell'industria dello spettacolo a Superstudio Più: biglietto valido per il singolo giorno.")
add("Festival dello Spettacolo 2026 - Abbonamento 3 giorni","music","2026-11-06","2026-11-08","12:00","Superstudio Più","Via Tortona 27, Milano","Milano","MI","milano","festival",f"{TM}/biglietti/festival-dello-spettacolo-2026/event/rdr2eokohvhx","Festival dell'industria dello spettacolo a Superstudio Più: abbonamento valido 6-8 novembre.")
add("Svaneborg Kardyb | JAZZMI 2026","music","2026-11-06",None,"21:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/svaneborg-kardyb-milano-06-11-2026/event/133qrwadspqa",J)
add("MT Jones | JAZZMI 2026","music","2026-11-06",None,"21:30","Santeria Toscana 31","Viale Toscana 31, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/mt-jones-jazzmi-2026-milano-06-11-2026/event/h8izq30gog31",J)
add("Placebo - 30th Anniversary Tour","music","2026-11-06",None,"20:30","Unipol Forum","Via Giuseppe di Vittorio 6, Assago","Assago","MI","lombardia","concerto",f"{TM}/biglietti/placebo-assago-06-11-2026/event/8ne6ogrbggt9")
add("Il Festival dello Spettacolo - Biglietto giornaliero","music","2026-11-07",None,"10:00","Superstudio Più","Via Tortona 27, Milano","Milano","MI","milano","festival",f"{TM}/biglietti/il-festival-dello-spettacolo-milano-07-11-2026/event/98c7ddpysxbh","Festival dell'industria dello spettacolo a Superstudio Più: biglietto valido per il singolo giorno.")
add("Enzo Favata 'Atlantico' | JAZZMI 2026","music","2026-11-07",None,"16:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/enzo-favata-atlantico-milano-07-11-2026/event/xh6nj5djbk6m",J)
add("Bill Frisell with Luke Bergman and Tim Angulo | JAZZMI 2026 (ore 20:00)","music","2026-11-07",None,"20:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/bill-frisell-with-luke-bergman-and-tim-angulo-milano-07-11-2026/event/n1n72x6qq006",J,caveat="Ticketmaster elenca due spettacoli distinti di Bill Frisell il 7/11 (ore 20:00 e 22:00).")
add("The Messthetics and James Brandon Lewis | JAZZMI 2026","music","2026-11-07",None,"21:30","Santeria Toscana 31","Viale Toscana 31, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/the-messthetics-and-james-brandon-lewis-milano-07-11-2026/event/h190ouw6l1n2",J)
add("Bill Frisell with Luke Bergman and Tim Angulo | JAZZMI 2026 (ore 22:00)","music","2026-11-07",None,"22:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/bill-frisell-with-luke-bergman-and-tim-angulo-milano-07-11-2026/event/9o2en666vm3x",J,caveat="Ticketmaster elenca due spettacoli distinti di Bill Frisell il 7/11 (ore 20:00 e 22:00).")
add("nayt: Noi Individui Tour","music","2026-11-07",None,"20:45","Unipol Forum","Via Giuseppe di Vittorio 6, Assago","Assago","MI","lombardia","concerto",f"{TM}/biglietti/nayt-noi-individui-tour-assago-07-11-2026/event/02o4qbpf2d4q")
add("Il Festival dello Spettacolo - Biglietto giornaliero","music","2026-11-08",None,"10:00","Superstudio Più","Via Tortona 27, Milano","Milano","MI","milano","festival",f"{TM}/biglietti/il-festival-dello-spettacolo-milano-08-11-2026/event/hlt04baruovt","Festival dell'industria dello spettacolo a Superstudio Più: biglietto valido per il singolo giorno.")
add("Isaiah Collier | JAZZMI 2026","music","2026-11-08",None,"19:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/isaiah-collier-milano-08-11-2026/event/m1ad85rlkjq4",J)
add("Sergio Cammariere | JAZZMI 2026","music","2026-11-08",None,"20:00","Conservatorio di Milano - Sala Verdi","Via Conservatorio 12, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/sergio-cammariere-milano-08-11-2026/event/v471kcstoywt",J)
add("Calibro 35 vs. L.A. | JAZZMI 2026","music","2026-11-08",None,"21:00",TRI,TRI_A,"Milano","MI","milano","concerto",f"{TM}/biglietti/calibro-35-vs-la-jazzmi-2026-milano-08-11-2026/event/68cgvasvwcpx",J)
add("The Kid LAROI - A Perfect World Tour","music","2026-11-12",None,"21:00","Fabrique","Via Gaudenzio Fantoli 9, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/the-kid-laroi-a-perfect-world-tour-milano-12-11-2026/event/sk7vixbr0l7f")
add("Nuzzo e Di Biase - Allo Sbagliato","comedy","2026-11-12",None,"20:30","Allo Sbagliato - Teatro Principe",None,"Milano","MI","milano","stand-up",f"{TM}/biglietti/nuzzo-e-di-biase-milano-12-11-2026/event/lcom2reewzy2","Duo comico Nuzzo e Di Biase nella rassegna 'Allo Sbagliato'.",caveat="Scheda Ticketmaster senza indirizzo del venue.")
add("LIVE GULINO (MARTA SUI TUBI)","music","2026-11-13",None,"20:00","Q-HUB","Via Mecenate, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/gulino-milano-13-11-2026/event/r53wpxyt38th","Live di Gulino (Marta sui Tubi) al Q-HUB.")
add("The Pretty Reckless - Dear God Tour","music","2026-11-14",None,"20:00","Fabrique","Via Gaudenzio Fantoli 9, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/the-pretty-reckless-dear-god-tour-milano-14-11-2026/event/rnpslxf1z7vn")
add("22Simba | Miria - Live Tour","music","2026-11-15",None,"21:00","Fabrique","Via Gaudenzio Fantoli 9, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/22simba-miria-live-tour-milano-15-11-2026/event/ir5g2luy26oq")
add("Gloria - Il Musical","music","2026-11-15",None,"17:00","Teatro Clerici","Via S. Zeno 168, Brescia","Brescia","BS","lombardia","musical",f"{TM}/biglietti/gloria-il-musical-brescia-15-11-2026/event/qi6i8icbh8u8")
add("22Simba | Miria - Live Tour","music","2026-11-16",None,"21:00","Fabrique","Via Gaudenzio Fantoli 9, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/22simba-miria-live-tour-milano-16-11-2026/event/q0v5q45eqaeo")
add("The Molotovs","music","2026-11-16",None,"21:00","Santeria Toscana 31","Viale Toscana 31, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/the-molotovs-milano-16-11-2026/event/0eguf2918h2j")
add("22Simba | Miria - Live Tour","music","2026-11-17",None,"21:00","Fabrique","Via Gaudenzio Fantoli 9, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/22simba-miria-live-tour-milano-17-11-2026/event/hvn9kd8ywxf0")
add("LEAP - Entropy World Tour","music","2026-11-17",None,"21:00","Magazzini Generali","Via Pietrasanta 16, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/leap-entropy-world-tour-milano-17-11-2026/event/bhb7je2h6ivc")
add("Live Session - Allo Sbagliato: prima stanza a destra, Gioia Lucia, Angelica Bove, IL MAESTRALE","comedy","2026-11-19",None,"20:30","Allo Sbagliato - Teatro Principe",None,"Milano","MI","milano","stand-up",f"{TM}/biglietti/live-session-allo-sbagliato-milano-19-11-2026/event/i00cb5mjwwc8","Serata 'Live Session' nella rassegna 'Allo Sbagliato'.",caveat="Scheda Ticketmaster senza indirizzo del venue.")
add("Artemas - LOVERCORE / GETTING UP TO NO GOOD Tour","music","2026-11-20",None,"20:30","Fabrique","Via Gaudenzio Fantoli 9, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/artemas-milano-20-11-2026/event/dct3j4c0sm5a")
add("Muse - The Wow! Signal Europa Tour","music","2026-11-20",None,"20:30","Unipol Dome","Via Romualdo Bonfadini 148, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/muse-the-wow-signal-europa-tour-milano-20-11-2026/event/nkjzd7z38ebl")
add("Muse - The Wow! Signal Europa Tour","music","2026-11-21",None,"20:30","Unipol Dome","Via Romualdo Bonfadini 148, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/muse-the-wow-signal-europa-tour-milano-21-11-2026/event/7dxucbjp51gm")
add("Fiorella Canta Fabrizio E Ivano: Anime Salve","music","2026-11-21",None,"21:00","ChorusLife Arena","Via Carlo Serassi 26, Bergamo","Bergamo","BG","lombardia","concerto",f"{TM}/biglietti/fiorella-canta-fabrizio-e-ivano-anime-salve-bergamo-21-11-2026/event/snu11bn4j2uy","Fiorella Mannoia canta Fabrizio De André e Ivano Fossati.",caveat="La scheda Ticketmaster indica come nome venue 'Sala BA nuovo' allo stesso indirizzo della ChorusLife Arena (Via Carlo Serassi 26, Bergamo).")
add("Carlotta Spallino, Cecilia Forastieri, Fill Pill - Allo Sbagliato","comedy","2026-11-24",None,"20:30","Allo Sbagliato - Teatro Principe",None,"Milano","MI","milano","stand-up",f"{TM}/biglietti/carlotta-spallino-allo-sbagliato-milano-24-11-2026/event/3bncp8grqxvm","Serata nella rassegna 'Allo Sbagliato'.",caveat="Scheda Ticketmaster senza indirizzo del venue.")
add("Freya Skye - Stars Align Tour","music","2026-11-25",None,"21:00","Fabrique","Via Gaudenzio Fantoli 9, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/freya-skye-stars-align-tour-milano-25-11-2026/event/6rnub74hz835")
add("Polyphia: BE NOT AFRAID World Tour","music","2026-11-25",None,"21:00","Alcatraz","Via Valtellina 25, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/polyphia-milano-25-11-2026/event/dz6i7w2rktep")
add("Saint Levant - AFANDI WORLD TOUR","music","2026-11-26",None,"21:00","Alcatraz","Via Valtellina 25, Milano","Milano","MI","milano","concerto",f"{TM}/biglietti/saint-levant-afandi-world-tour-milano-26-11-2026/event/vml9fogfr66x")
add("VALENTINA PERSIA - NATA CON LA GUÊPIÈRE","comedy","2026-11-28",None,"21:00","Teatro Clerici","Via S. Zeno 168, Brescia","Brescia","BS","lombardia","stand-up",f"{TM}/biglietti/valentina-persia-nata-con-la-gupire-brescia-28-11-2026/event/lbtf5u4n44n7")
add("ALESSANDRO CATTELAN - Benvenuto nell'AI!","comedy","2026-11-30",None,"21:00","Teatro Lirico Giorgio Gaber","Via Larga 14, Milano","Milano","MI","milano","stand-up",f"{TM}/biglietti/alessandro-cattelan-benvenuto-nellai-milano-30-11-2026/event/eqklpt9wtfyx")

json.dump(E, open("ticketmaster_events.json","w"), ensure_ascii=False, indent=1)
print("events:", len(E))
