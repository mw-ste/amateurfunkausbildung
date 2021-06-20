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

- die Dauer einer Umladung ist abhängig von den Kapazitätswerten und Induktivitätswerten der Bauteile
- bei freier Schwingung stellt sich die Resonanzfrequenz $f_{res}$ ein
- Thomsonsche Schwingkreisformel
- $f_{res} = \frac{1}{2 \cdot \pi \cdot \sqrt{L \cdot C}}$
- die Frequenz sinkt mit steigenden Bauteilwerten

## Reihenschwingkreis

- Reihenschaltung von Kondensator und Spule
- der Widerstand ist bei Resonanz am **kleinsten**
- der Resonanzwiderstand entspricht etwa dem Verlustwiderstand der Spule
- Saugkreis?

## Parallelschwingkreis

- Parallelschaltung von Kondensator und Spule
- der Widerstand ist bei Resonanz am **größten**
- er ist daher einer Bandsperre
- die **Bandbreite** der Bandsperre ist der Frequenzbereich, in dem der Widerstand mindestens 70% seines Maximalwertes beträgt

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
