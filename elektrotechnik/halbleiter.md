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

## Diode

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

### Sperrschaltung

- Verarmungszone wird verbreitert
- PN-Übergang sperrt
- nur geringer Sperrstrom fließt (µA oder nA)
- wird die Durchbruchspannung überschritten, so wird das Bauteil zerstört

```
- _______|\|_______ +
         |/|
    Anode   Katode
```

## Zener-Diode

- gewöhnlich werden Dioden zerstört wenn die Durchbruchspannung überschritten wird
- dies passiert normalerweise bei Spannungen > 1000 V
- Zener-Dioden, oder Z-Dioden, werden beim Durchbruch nicht zerstört
- ihre Durchbruchspannung liegt im Bereich 3 - 100 V
- der dabei fließende Strom muss begrenzt werden
- kann genutzt werden um Spannungen zu stabilisieren

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
- durch bestimmte Dotierung wird Licht frei
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

# Diode als Gleichrichter

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

- Einweggleichrichter
- die Halbwelle in Sperrichtung wird abgeschnitten

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

- Einweggleichrichter mit Ladekondensator
- die Halbwelle in Sperrichtung wird abgeschnitten
- der Kondensator hält die Spannung zwischen den verbleibenden Halbwellen aufrecht
