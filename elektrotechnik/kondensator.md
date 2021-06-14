# Kondensatoren

## Kapazität

```
      |  |
 o----|  |----o
      |  |
```

- **Formelzeichen**: `C`
- **Einheit**: Farad $1F = 1 \frac{As}{V}$

- wird ein Kondensator durch eine Spannung aufgeladen, so kann er Energie in einem elektrischen Feld speichern
- dieses Speichervermögen ist seine Kapazität `C`
- die gespeicherte Ladung `Q` ist abhängig von der Kapazität `C` des Kondensator und der angelegten Spannung `U`

- $Q = I \cdot t = C \cdot U$
- $C = \frac{I \cdot t}{U}$

- die Kapazität eines Kondensators ist abhängig von seiner Fläche `A`, deren Abstand `d` und der Dielektrizitätszahl $\varepsilon$

- $\varepsilon = \varepsilon_0 \cdot \varepsilon_r$
- $C = \frac{\varepsilon_0 \cdot \varepsilon_r \cdot A}{d}$

## Schaltungen

### Reihenschaltung

- (es steigt quasi der Abstand `d`)
- $\frac{1}{C_{ges}} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots + \frac{1}{C_N}$
- $C_{ges} = \frac{C_1 \cdot C_2}{C_1 + C_2}$
- Berechnung wie bei parallelgeschalteten Widerständen

### Parallelschaltung

- (es steigt quasi die Fläche `A`)
- die Gesamtkapazität einer Parallelschaltung aus Kondensatoren entspricht der Summe der Einzelkapazitäten

## Ent-/Ladevorgang

```
     A
     |                       *
   U |                *
     |           *
63%  ---------*
     |     *
     |   *
     |  *
     | *
     |*
     |*
     |---------------------------------------> t

```

```
     A
     |*
   U |*
     | *
     |  *
     |   *
     |     *
37% ----------*
     |           *
     |                *
     |                       *
     |---------------------------------------> t
```

- zunächst fließt ein hoher Ladestrom
- mit zunehmender Ladung nimmt der Ladestrom ab
- charakterisiert durch die Zeitkonstante $\tau$
- die Zeitkonstante entspricht der Zeit, in der ein Kondensator um 63% ge- bzw. entladen wurde

* **Formelzeichen**: $\tau$
* **Einheit**: Sekunde

- $\tau = R \cdot C$
- $R$ ist der Widerstand im Ent-/Ladestromkreis
- der Entladestrom fließt entgegen dem Ladestrom

## Wechselstromwiderstand

- ein Kondensator sperrt Gleichstrom und lässt Wechselstrom fließen
- er stellt damit einen frequenzabhängigen Widerstand dar
- Wechselstromwiderstand des Kondensators $X_C$
- kapazitiver Blindwiderstand $X_C$
- Kreisfrequenz $\omega = 2 \pi \cdot f$

- $X_C = \frac{U_C}{I_C}$
- $X_C = \frac{1}{2 \pi \cdot f \cdot C} = \frac{1}{\omega \cdot C}$
- $I_C = \omega \cdot C \cdot U_C$
- $U_C = \frac{I_C}{\omega \cdot C}$

- sinkt mit zunehmender Frequenz und Kapazität
- außerdem ergibt sich ein Phasenversatz zwischen Strom und Spannung
- am Kondensator eilt der Strom um eine viertel Periode der Spannung **voraus**

## Scheinwiderstand

```
      |  |     _____
 o----|  |----|_____|-----o
      |  |
```

- der Scheinwiderstand $Z$ realer Kondensatoren setzen sich aus Blindwiderstand $X_C$ und Wirkwiderstand $R$ zusammen
- $Z = \sqrt{R^2 + {X_C}^2}$

## Verlustbehafteter Widerstand

```
             ---> I_R
             _____
      +-----|_____|-----+
      |       R_V       |
      |                 |
o-----|                 |-----o
      |       ||        |
      +-------||--------+
              ||

             ---> I_C
```

- Verlustwärme durch parallelgeschalteten Widerstand $R_V$
- Verlustfaktor $tan \left( \delta \right)$
- Gütefaktor $\frac{1}{tan \left( \delta \right)}$
- $tan \left( \delta \right) = \frac{I_R}{I_C} = \frac{X_C}{R_V}$

## Bauformen

- besteht aus gegenüberliegenden Leitern
- getrennt durch ein Dielektrikum
- einstellbare Plattendrehkondensatoren (Rotor/Stator)
- Elektrolytkondensatoren (Elko) (Polung beachten!)

![Kondensatoren](https://www.darc.de/fileadmin/filemounts/referate/ajw/Onlinelehrgang/e05/Bild05-08SchaltsymboleC.gif)
a) allgemein
b) einstellbar (Trimmer)
c) veränderbar
d) gepolt
e) Elko gepolt
f) Elko ungepolt

## Dielektrikum

- gut isolieren
- hoher Dielektrizitätswert
  - Keramik
  - Kunststoff
  - Luft

## Kapazitätsangabe

- oft Buchstabe der Größenordnung anstatt Dezimalzeichen
- `m47` &rarr; `0.47 mF`
- `4µ7` &rarr; `4.7 µF`
