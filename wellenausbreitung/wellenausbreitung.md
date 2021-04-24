# Vorbereitung auf den ersten Termin

## Aus der Klasse E

https://www.darc.de/der-club/referate/ajw/lehrgang-te/e09/
bis zur Überschrift **"UKW-Wellenausbreitung"**

## Aus der Klasse A

https://www.darc.de/der-club/referate/ajw/lehrgang-ta/a08/#Wellenausbreitung
bis zur Überschrift **"Die Wellenausbreitung oberhalb 30 MHz"**

# Wellenausbreitung

- Funkamateure senden im Kurzwellenbereich und im Ultrakurzwellenbereich
- Ausbreitung UKW (VHF/UHF) vorwiegend wie Licht
- Ausbreitung Kurzwelle
  - Reflexion an der Ionosphäre möglich (Raumwelle)
  - Bodenwelle entlang der Erdoberfläche, wird mit zunehmender `f` stärker gedämpft

# Ionosphäre

- Heavyside-Schicht
- 100-500km Höhe
- wird durch Sonneneinstrahlung ionisiert
- Reflexion abhängig von
  - Frequenz
  - Stärke der Ionisation
    - Tag/Nacht
    - Sommer/Winter

# Sonnenfleckenzyklus

- wiederholt sich alle 11 Jahre

# Raumwelle

- Kritische Frequenz $f_k$
- Frequenz bei der senkrecht in Ionosphäre eintretende Raumwelle gerade noch reflektiert wird

- Maximal Usable Frequency MUF
- alle Frequenzen drüber werden nur gebrochen, nicht reflektiert
- Sekansgesetz $MUF \approx \frac{f_k}{sin \left( \alpha \right)} |_{\alpha \ge 40°}$
- $\alpha$ Abstrahlungswinkel über der Horizontalen
- beste Reichweite knapp unter der MUF, da Dämpfung am geringsten

# Ionosphäre-Schichten

## D-Schicht

- 70-90km
- Dämpfungssicht zwischen Erdoberfläche und Ionosphäre
- bildet sich tagsüber, vor allem in Sommermonaten
- verschwindet nach Sonnenuntergang schnell
- absorbiert 80m (untere Kurzwelle) und 160m (Mittelwelle) Bänder

- **Mögel-Dellinger-Effekt:**
  - D-Schicht soweit ionisiert, dass zeitweilig im gesamten Kurzwellenbereich keine Reflexion an der Ionosphäre möglich ist
  - lässt sich mit Leistungserhöhung teilweise ausgleichen

## E-Schicht

- 100-130km
- bildet sich Juni-August tagsüber
- Reflektiert Kurzwelle, evtl UKW (evtl 2m, 6m, 10m)
- Grenzfrequenz hierfür 100 MHz
- Durchmesser dieser Schicht oft nur 20-100km

## F-Schicht

- 200-400km
- hauptverantwortlich für die Ionosphären-Reflexion
- Mehrfach-Reflexionen, M-Reflexion, innerhalb der Ionosphäre möglich
- Gleiches Phänomen auch bei Reflexion an Wasser

### F1-Schicht

- Spaltung der F-Schicht bei starker Sonneneinstrahlung
- Dämpft die Reflektierten Wellen
- Führt zu geringerer Reichweite: tagsüber Europa-Verkehr (short skip)

### F2-Schicht

- höchste Schicht, größte Höhenausdehnung
- wenig abhängig von der Sonneneinstrahlung
- für weiteste Reichweiten bis zu 4000km
- nachts interkontinentaler Funkverkehr

# Fading

- bei ständigem Wechsel zwischen konstruktiver und destruktiver Überlagerung
- zwischen Raum- und Bodenwelle
- bei Reflexion an Flugzeugen im UKW-Bereich

# Tote Zone

- Bereich ohne Empfang
- Zwischen dem Abklingbereich der Bodenwelle und dem Wiederauftreffen der reflektierten Raumwelle
- Ausdehnung: Sprungdistanz - Reichweite der Bodenwelle

# Bandplan

$f = \frac{c}{\lambda}$ &lrarr; $\lambda = \frac{c}{f}$

| Band | Frequenzbereich Start | Frequenzbereich Ende | Details |
| ---- | --------------------- | -------------------- | ------- |
| 160m | 1.810 MHz             | 2.000 MHz            |         |
| 80m  | 3.500 MHz             | 3.800 MHz            |         |
| 40m  | 7.000 MHz             | 7.200 MHz            |         |
| 30m  | 10.100 MHz            | 10.150 MHz           |         |
| 20m  | 14.000 MHz            | 14.350 MHz           |         |
| 17m  | 18.068 MHz            | 18.168 MHz           |         |
| 15m  | 21.000 MHz            | 21.450 MHz           |         |
| 12m  | 24.890 MHz            | 24.990 MHz           |         |
| 10m  | 28.000 MHz            | 29.700 MHz           |         |
| 6m   | 50.080 MHz            | 51.000 MHz           |         |
| 2m   | 144 MHz               | 146 MHz              | VHF     |
| 70cm | 430 MHz               | 440 MHz              | UHF     |
| 23cm | 1240 MHz              | 1300 MHz             | SHF     |
| 3cm  | 10.0 GHz              | 10.5 GHz             |         |

### 160m

- Mittelwellencharakter
- tagsüber: Dämpfung durch D-Schicht
- nachts: Reflexion an der F-Schicht ermöglict Reichweiten von mehreren 1000km

### 80m

- tagsüber: Dämpfung durch D-Schicht
- geringere Dämpfung im Winter oder bei Sonnenfleckenminimum
- dann vor allem nachts lange Direktverbindungen möglich
- typisches Band für Funkverkehr im eigenen Land

### 40m

- tagsüber: Dämpfung durch D-Schicht
- trotzdem tagsüber entfernungen um 1000km
- typisches Band für Funkverkehr in Europa
- nachts und bei Sonnenfleckenminimum theoretisch interkontinentaler Verkehr möglich, aber oft von Nahstationen überdeckt
- wenn diese in den Wintermonaten in der toten Zone liegen sind interkontinentale Verbindungen innerhald der Dunkelzone möglich

### 30m

- ähnlich dem 40m Band
- tagsüber, im Sommer, Zeiten mit wenig Sonnenflecken Europaband
- interkontinentaler Funkverkehr in den anderen Zeiten

### 20m

- tradizionelles DX Band
- tags und nachts interkontinentaler Funkverkehr
- außer im Sommer bei Short-Skip an E-Schicht
- Bei Sonnenfleckenminimum ist das Band nachts nicht offen

### 17m und 15m

- stark abhängig von Sonnenfleckenzyklus
- bei Sonnenfleckenmaximum für DX-Funkverkehr geöffnet
- dann mit geringer Leistung große Entfernungen möglich
- bei Sonnenfleckenminimum nur kurzzeitig, tagsüber, in den Sommermonaten offen
- Reflexionen an der sporadischen E-Schicht möglich, Short Skip bis 2000km

### 12m und 10m

- extrem abhängig von Sonnenfleckenzyklus
- Reflexionen nur bei starker Sonnenaktivität
- tagsüber für DX-Funkverkehr geöffnet
- dann mit geringer Leistung große Entfernungen möglich
- bei Sonnenfleckenminimum keine Fernverbindungen möglich
- Reflexionen an der sporadischen E-Schicht möglich, Short Skip über mittlere Reichweite

# Greyline DX

- besonders große Reichweiten auf den Kurzwellenbändern
- im Bereich der Dämmerungszonen
  - zwischen Dunkelheit und Sonnenaufgang
  - zwischen Abenddämmerung und Nacht
