# Halbleiter

- Valenzelektronen: Elektronen auf der äußersten Atom-Schale
- Halbleiter-Werkstoffe: Silizium, Germanium, Selen, Galliumarsenid, Indiumphosphid, Indiumantimonid
- Germanium und Silizium: 4 Valenzelektronen
- bei niedrigen Temperaturen, evtl noch bei Raumtemperatur Nichtleiter
- zunehmende Leitfähigkeit mit steigender Temperatur &rarr; NTC-Widerstand
- "thermal runaway"
- N-leitende Halbleiter: dotiert mit Material mit mehr Valenzelektronen (Überschusselektronen)
- P-leitende Halbleiter: dotiert mit Material mit weniger Valenzelektronen (Löcher)
- Dotierung erhöht Leitfähigkeit bei niedrigeren Temperaturen

# Dioden

- Übergänge zwischen P- und N-dotierten Stoffen
- Rekombination im Übergangsbereich
- Überschusselektronen aus dem N-dotierten Material füllen Löcher im P-dotierten Material
- nichtleitende Sperrschicht, da keine freien Elektronen mehr
- Sperrschicht durch Elektronenwanderung elektrisch geladen
- Diffusionsspannung:
  - Germanium 0.2 - 0.4 V
  - Silizium 0.6 - 0.8 V

```
          P                   N
     +----------+---+---+----------+
     |          | - | + |          |
     |          | - | + |          |
o----| neutral  | - | + |  neutral |----o
     |          | - | + |          |
     |          | - | + |          |
     +----------+---+---+----------+
```

```
      +---+---+
o-----| P | N |-----o
      +---+---+


+   ------> I   -
_______|\|_______
       |/|
  Anode   Katode
```

## Kennlinie
* die Strom-Spannungs-Kennlinie einer Diode ist nichtlinear
* zunächst fließt kein Strom
* mit Erreichen der Schwellspannung beginnt ein Stromfluss durch die Diode
    * Germanium ca. 0.2 V
    * Silizium ca. 0.65 V
* die Spannung, für die ein bestimmter Strom fließt, heißt Durchlassspannung
* dieser Punkt auf der Kennlinie heißt Arbeitspunkt
* der Kennlinie der Germaniumdiode ist flacher als die der Siliziumdiode

### Sperrschaltung

- Verarmungszone wird verbreitert
- PN-Übergang sperrt
- nur geringer Sperrstrom fließt (µA oder nA)
- wird die Durchbruchspannung überschritten, so wird das Bauteil zerstört
- dabei wirkt die Diode als Kurzschluss
- dies passiert normalerweise bei Spannungen > 1000 V

```
- _______|\|_______ +
         |/|
    Anode   Katode
```

## Zener-Diode

- gewöhnlich werden Dioden zerstört wenn die Durchbruchspannung überschritten wird
- Zener-Dioden, oder Z-Dioden, werden beim Durchbruch nicht zerstört
- ihre Durchbruchspannung liegt im Bereich 3 - 100 V
- der dabei fließende Strom muss begrenzt werden
- kann genutzt werden um Spannungen zu stabilisieren

## Schottky-Diode
* besonders geeignet als Schaltdiode für HF-Anwendungen
* nutzbar bis etwa 50 GHz
* Durchlassspannung von nur etwa 0.25 V
* Aufbau aus Metallschicht und N-dotierter Siliziumschicht
* Elektronen gelangen leichter aus dem Silizium in das Metall als umgekehrt
* dadurch bildet sich die Schottky-Sperrschicht

## Kapazitätsdiode
* Varicap, Varaktor
* so lange die Schwellspannung nicht überschritten wird, kann eine Diode als Kondensator aufgefasst werden
* dabei fungiert die Sperrschicht als Dielektrikum
* Kapazitätsdiode wird in Sperrschicht betrieben
* die Sperrschichtkapazität ist umgekehrt proportional zur Sperrspannung
* die Kapazität kann also durch eine Gleichspannung in Sperrrichtung gesteuert werden

## Foto-Diode

- wird in Sperrichtung geschaltet
- der Sperrstrom steigt mit zunehmender Lichtintensität
- **Foto-Element**: Foto-Diode als Spannungsquelle

## Solarzelle

- großflächige Fotodioden
- Spannung bis etwa 500 mV
- Strom bis einige hundert mA
- können als Energiequellen genutzt werden, z.B. für Satelliten

## Leuchtdiode LED

- LED: light emitting diode
- durch bestimmte Dotierung wird bei der Rekombination Licht frei
- Grundmaterial Galliumphosphid oder Gallium-Arsenphosphid
- Lichtfarbe je nach Dotierung:
  - Zink: grünes Licht
  - Zinksauerstoff: rotes Licht
- etwa 1.5 V, 5 - 50 mA
- hohe Lebensdauer, geringe Abmessungen

## Optokoppler

- Leuchtdioden können zur Signalübertragung bis etwa 10 MHz genutzt werden
- Galvanische Entkopplung
- elektrisches Signal &rarr; optisches Signal &rarr; elektrisches Signal

## Typkennzeichnung

- Typenkennzeichnung für Halbleiterbauelemente in Europa
- 2-3 Buchstabeln plus eine Zahl
- Erster Buschstabe: Ausgangsmaterial
  - A: Germanium
  - B: Silizium
- Zweiter Buschstabe: Anwendung
  - A: Diode
  - B: Kapazitätsdiode
  - E: Tunneldiode
  - X: Vervielfacherdiode
  - Y: Leistungsdiode
  - Z: Z-Diode
- Dritter Buchstabe: Spezialanwendungen (falls vorhanden)
  - W, X, Y, Z
- Ziffern: laufende Kennzeichnung

- Amerikanische und Asiatische Hersteller: "1N" plus eine zwei- bis vierstellige laufende Zahl

# Anwendungen von Dioden

## Diode als Gleichrichter

### Einweggleichrichter
```
                            R_L
         |\|               _____
o--------|/|--------o-----|_____|-----+
                                      |
U~                  U_                |
                                      |
                                      |
o-------------------o-----------------+
```

- die Halbwelle in Sperrichtung wird abgeschnitten
### Einweggleichrichter mit Ladekondensator

```
                            R_L
         |\|               _____
o--------|/|--------o-----|_____|-----+
                    |                 |
U~                --+--               |
                  --+-- C_L           |
                    |                 |
o-------------------o-----------------+
```

- die Halbwelle in Sperrichtung wird abgeschnitten
- der Kondensator hält die Spannung zwischen den verbleibenden Halbwellen aufrecht

### Mittelpunkt-Zweiweggleichrichtung

* Doppelweggleichrichtung
* über Transformator mit zwei gleichen Wicklungen oder Mittelanzapfung
* die Wicklungen werden gegenläufig auf den gleichen Signalpfad geschaltet
* der Mittelpunkt bildet die Masse
* durch Dioden wird bei beiden Wicklungen nur jeweils die positive oder negative Halbwelle durchgelassen
* so werden beide Halbwellen in den positiven Bereich gebracht

### Brücken-Gleichrichterschaltung
* Doppelweggleichrichtung
* Schaltung aus vier Dioden
* kein Transformator nötig
* Sperrwiderstände der Dioden müssen gleich groß sein
* als fertiges Bauteil erhältlich
* z.B. B40C1000
    * B: Brückenschaltung
    * 40: max 40 V Effektivspannung
    * 1000: max 1000 mA Ausgangsstrom
    * C: bei Glättung mit einem Kondensator

## Spannungsbegrenzung

* zwei Dioden werden antiparallel gegen Masse geschaltet
* steigt die Eingangsspannung im Betrag über die Durchlassspannung, so wird die darüber hinaus gehende Spannung kurzgeschlossen

# Weiter gehts bei:
https://www.darc.de/der-club/referate/ajw/lehrgang-ta/a05#Siebung