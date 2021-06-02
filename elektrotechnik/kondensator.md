# Kondensatoren

## Kapazität

```
      |  |
 o----|  |----o
      |  |
```

- **Formelzeichen**: `C`
- **Einheit**: Farad $1F = 1 \frac{As}{V}$

- wird ein Kondensator durch eine Spannung aufgeladen, so kann er Energie speichern
- dieses Speichervermögen ist seine Kapazität `C`
- die gespeicherte Ladung `Q` ist abhängig von der Kapazität `C` des Kondensator und der angelegten Spannung `U`

- $Q = I \cdot t = C \cdot U$
- $C = \frac{I \cdot t}{U}$

- die Kapazität eines Kondensators ist abhängig von seiner Fläche `A`, deren Abstand `d` und der Dielektrizitätszahl $\varepsilon$

- $\varepsilon = \varepsilon_0 \cdot \varepsilon_r$
- $C = \frac{\varepsilon_0 \cdot \varepsilon_r \cdot A}{d}$

## Schaltungen

### Parallelschaltung

- (es steigt quasi die Fläche `A`)
- die Gesamtkapazität einer Parallelschaltung aus Kondensatoren entspricht der Summe der Einzelkapazitäten

### Reihenschaltung

- (es steigt quasi der Abstand `d`)
- $\frac{1}{C_{ges}} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots + \frac{1}{C_N}$
- $C_{ges} = \frac{C_1 \cdot C_2}{C_1 + C_2}$
- Berechnung wie bei parallelgeschalteten Widerständen

## Wechselstromwiderstand

- ein Kondensator sperrt Gleichstrom und lässt Wechselstrom fließen
- er stellt damit einen frequenzabhängigen Widerstand dar
- Wechselstromwiderstand des Kondensators $X_C$
- $X_c = \frac{U_C}{I_C}$
- $X_c = \frac{1}{2 \pi \cdot f \cdot C}$
- sinkt mit zunehmender Frequenz und Kapazität

## Bauformen

* besteht aus gegenüberliegenden Leitern
* getrennt durch ein Dielektrikum
* einstellbare Plattendrehkondensatoren (Rotor/Stator)
* Elektrolytkondensatoren (Elko) (Polung beachten!)

![Kondensatoren](https://www.darc.de/fileadmin/filemounts/referate/ajw/Onlinelehrgang/e05/Bild05-08SchaltsymboleC.gif)
    a) allgemein
    b) einstellbar (Trimmer)
    c) veränderbar
    d) gepolt
    e) Elko gepolt
    f) Elko ungepolt

## Dielektrikum
* gut isolieren
* hoher Dielektrizitätswert
    * Keramik
    * Kunststoff
    * Luft

## Kapazitätsangabe
* oft Buchstabe der Größenordnung anstatt Dezimalzeichen
* `m47` &rarr; `0.47 mF`
* `4µ7` &rarr; `4.7 µF`