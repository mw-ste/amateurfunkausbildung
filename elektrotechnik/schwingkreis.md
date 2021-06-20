# Schwingkreis

- Zusammenschaltung aus Spule und Kondensator
- eines der Bauteile wird geladen
- es gibt seine energie anschließend ab und wirkt damit als Energiequelle
- dadurch wird das jeweils andere Bauteil geladen bis das erste entladen ist
- anschließend tauschen die Bauteile ihre Rollen und der Umladung beginnt erneut
- in beiden Bauteilen wirkt der Entladestrom dem Ladestrom entgegen
- bei idealer Spule und Kondensator wäre dies eine ungedämpfte Schwingung
- durch die verlustbehafteten realen Bauteile ergibt sich jedoch eine gedämpfte abklingende Schwingung

## Schwingkreisfrequenz

- Serienschwingkreis
- die Dauer einer Umladung ist abhängig von den Kapazitätswerten und Induktivitätswerten der Bauteile
- bei freier Schwingung stellt sich die Resonanzfrequenz $f_{res}$ ein
- diese ergibt sich, wenn die Blindwiderstände beider Bauteile gleich groß sind $X_L = X_C$
- Thomsonsche Schwingkreisformel
- $f_{res} = f_0= \frac{1}{2 \cdot \pi \cdot \sqrt{L \cdot C}} = \frac{1}{\omega \sqrt{L \cdot C}}$
- die Frequenz sinkt mit steigenden Bauteilwerten

## Reihenschwingkreis

- Reihenschaltung von Kondensator und Spule
- **der Widerstand ist bei Resonanz am kleinsten**
- der Resonanzwiderstand entspricht etwa dem Verlustwiderstand der Spule
- Saugkreis?

## Parallelschwingkreis

- Parallelschaltung von Kondensator und Spule
- **der Widerstand ist bei Resonanz am größten**
- er ist daher einer Bandsperre
- die **Bandbreite** der Bandsperre ist der Frequenzbereich, in dem der Widerstand mindestens 70% (-3dB) seines Maximalwertes beträgt

## Schwingkreis-Güte

- die Bandbreite ist abhängig von der Güte
- die Güte ist abhängig von den Verlustwiderständen der Bauteile
- hautpsächlich von der Güte der Spule
- Güte im **Reihenschwingkreis**: $Q = \frac{X_L}{R_S}$
- Güte im **Parallelschwingkreis**: $Q = \frac{R_P}{X_L}$
- **Bandbreite** $B = \frac{f_{res}}{Q}$
- Um die Bandbreite gering zu halten, muss entweder die Güte steigen oder die Rsonanzfrequenz sinken

## Quarz als Schwingkreis

- Schwingquarz hat ähnliches Verhalten wie ein LC-Schwingkreis
- besteht aus reinem Siliziumdioxid
- Plättchen aus einem Quarzkristall
- nutzt den umgekehrten Piezoelektrischen Effekt
- durch anlegen einer Spannung
  _ verbiegt sich der Quarz (Biegeschwinger)
  _ verändert der Quarz seine Dicke (Dickenschwinger)
- je dünner der Quarz, desto höher die Frequenz
- Grundwellenquarze für **50 kHz bis 15 MHz**
- werden in Oszillatoren für HF genutzt
- Genauigkeiten von $10^{-6}$ - $10^{-8}$ bzw. 1 - 0.01 ppm

```
            | |                   _____
      +-----| |-----)()()()(-----|_____|-----+
      |     | |                              |
      |     C_S        L           R         |
o-----+                                      +-----o
      |               C_P                    |
      |               | |                    |
      +---------------| |--------------------+
                      | |
```

- Serienresonanzfrequenz $f_S = \frac{1}{2 \cdot f \cdot \sqrt{L \cdot C_S}}$
- Parallelresonanzfrequenz $f_P = \frac{1}{2 \cdot f \cdot \sqrt{L \cdot C_{ges}}}$
- dabei gilt $C_{ges}$ aus Serienschaltung von $C_S$ und $C_P$
- $f_S$ und $f_P$ liegen dicht beieinander
- sehr hoher Widerstand bei $f_P$
- sehr niedriger Widerstand bei $f_S$

![](https://www.darc.de/fileadmin/filemounts/referate/ajw/Onlinelehrgang/a04/bild4-08.gif)

# Bandpassfilter

- aufgrund seines Frequenzgangs eignet sich der Parallelschwingkreis für Bandpassfilter
- hierzu können zwei oder mehr Parallelschwingkreise zusammengeschaltet werden
- die Kopplung kann induktiv oder kapazitiv erfolgen
- es werden Frequenzen abseits der Resonanzfrequenz gesperrt

- Kopplung
  - lose: Verlauf wie bei Einzelkreis
  - unterkritisch: geringere Übertragung, Verlauf wie bei Einzelkreis
  - kritisch: waagerechtes Dach (flat top)
  - überkritisch: Einsattelung (zwei Peaks)

# Sperrkreis, Bandpass, Leitkreis, Saugkreis

## Sperrkreis

- Bandsperre, Notch-Filter
- Parallelschwingkreis im Signalpfad
- lässt Frequenzen abseits der Resonanzfrequenz durch
- Widerstand im Signalpfade bei der Resonanzfrequenz am höchsten

## Bandpass

- Parallelschwingkreis gegen Masse
- blockt Frequenzen abseits der Resonanzfrequenz
- schließt Frequenzen abseits der Resonenzfrequenz gegen Masse kurz

## Leitkreis

- Serienschwingkreis im Signalpfad
- blockt Frequenzen abseits der Resonanzfrequenz
- Widerstand im Signalpfade bei der Resonanzfrequenz am niedrigsten

## Saugkreis

- Serienschwingkreis gegen Masse
- lässt Frequenzen abseits der Resonanzfrequenz durch
- schließt Resonanzfrequenz gegen Masse kurz
- beispielsweise zur Störungsunterdrückung
- störende Frequenzen werden _abgesaugt_

# Tiefpass und Hochpass

## Tiefpass

```
o--------)()()()(-----+--------o
            L         |
                    __|__
                    _____  C
                      |
o---------------------+--------o
```

- Spule in Reihe
- Kondensator gegen Masse

```
      A
    U | * * * * * *  *   *
      |                     *
      |                       *
0.7 U |-------------------------*
      |                         |*
      |                         | *
      |                         |  *
      |                         |   *
      |                         |     *
      |                         |        *
      +-------------------------|--------------->  f
                               f_g
```

- Tiefpass: niedrige Frequenzen können ungehindert passieren
- bei honen Frequenzen steigt der Widerstand der Spule
- außerdem wird das Signal über den Kondensator kurzgeschlossen
- bei der **Grenzfrequenz** $f_g$ beträgt die Ausgangsspannung 70% der Eingangsspannung

- **T-Schaltung**: Spule in Serie, Kondensator gegen Masse, Spule in Serie
- **Pi-Schaltung**: Kondensator gegen Masse, Spule in Serie, Kondensator gegen Masse

- Netzspannungsentstörung mit Tiefpass in Pi-Schaltung
- dann oft symmetrischer Aufbau

## Hochpass

```
         | |
o--------| |-----+------------------o
         | |     |
          C      +--)()()()(--+
                       L      |
o-----------------------------+-----o
```

- Kondensator in Reihe
- Spule gegen Masse

```
      A
    U |                      *  *  * * * *
      |                   *
      |                *
0.7 U ---------------*
      |            * |
      |          *   |
      |         *    |
      |        *     |
      |      *       |
      |   *          |
      +--------------|-------------------------->  f
                    f_g
```

- Hochpass: hohe Frequenzen können ungehindert passieren
- bei niedrigen Frequenzen steigt der Widerstand des Kondensators
- außerdem wird das Signal über die Spule kurzgeschlossen
- bei der **Grenzfrequenz** $f_g$ beträgt die Ausgangsspannung 70% der Eingangsspannung

- **T-Schaltung**: Kondensator in Serie, Spule gegen Masse, Kondensator in Serie
- **Pi-Schaltung**: Spule gegen Masse, Kondensator in Serie, Spule gegen Masse

## Bandpass in Pi-Schaltung

- Schwingkreise im Pi-Schaltung
- steilere Flanken
- Parallelschwingkreis gegen Masse, Serienschwingkreis im Signalpfad, Parallelschwingkreis gegen Masse

## RC-Hochpass und RC-Tiefpass

- Widerstand statt Spule
- gleiche Funktion, geringere Flankensteilheit
- Grenzfrequenz $f_g$: 0.7 U bzw. -3 dB
- $f_g = f_0 = \frac{1}{2 \cdot \pi \cdot R \cdot C}$
- **Tiefpass**: Widerstand im Signalpfad, Kondensator gegen Masse
- **Hochpass**: Kondensator im Signalpfad, Widerstand gegen Masse

# Resonanztransformation

- Schwingkreis zu Transformationszwecken
- **Beispiel**:
  - Tiefpass in Pi-Schaltung
  - Transformation zwischen Eingangs- und Ausgangswiderstand
  - gesteuert durch das Verhältnis der Kapazitäten
  - $\frac{C_2}{C_1} = \sqrt{\frac{R_1}{R_2}}$
