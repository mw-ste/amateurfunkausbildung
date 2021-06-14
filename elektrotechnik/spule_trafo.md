# Spule

## Induktivität

- **Formelzeichen**: `L`
- **Einheit**: Henry $1H = 1 \frac{Vs}{A}$

- fließt Strom durch eine Spule, so kann sie Energie in einem magnetischen Feld speichern

- $L = \frac{\mu \cdot A \cdot N^2}{l}$

- die Induktivität der Spule ist abhängig von der Windungszahl `N`, der Länge `l` und der Querschnittsfläche `A` der Spule und der Permeabilität `µ` des Kernmaterials

- Übliche Wertebereich der Induktivität
  - `µH` für Luftspulen
  - `mH` für Spule mit Ferritkern

## Schaltungen

### Reihenschaltung

- die Gesamtkapazität einer Parallelschaltung aus Kondensatoren entspricht der Summe der Einzelkapazitäten

### Parallelschaltung

- $\frac{1}{L_{ges}} = \frac{1}{L_1} + \frac{1}{L_2} + \cdots + \frac{1}{L_N}$
- $L_{ges} = \frac{L_1 \cdot L_2}{L_1 + L_2}$
- Berechnung wie bei parallelgeschalteten Widerständen

## Ent-/Ladevorgang

- Aufbau des magnetischen Felds dauert immer eine gewisse Zeit
- daher steigt der Strom am Ausgang der Spulenicht nicht sprunghaft an
- zunächst wird Energie in das Magnetfeld übertragen
- sobald sich der Strom durch die Spule ändert wird eine Gegenspannung (Selbstinduktionsspannung) erzeugt

## Wechselstromwiderstand

- ein Kondensator sperrt Wechselstrom und lässt Gleichstrom fließen
- er stellt damit einen frequenzabhängigen Widerstand dar
- Wechselstromwiderstand des Kondensators $X_L$
- induktiver Blindwiderstand $X_C$
- Kreisfrequenz $\omega = 2 \pi \cdot f$

- $X_L = \frac{U_L}{I_L}$
- $X_L = 2 \pi \cdot f \cdot L = \omega \cdot L$

- steigt mit zunehmender Frequenz und Induktivität
- außerdem ergibt sich ein Phasenversatz zwischen Strom und Spannung
- an der Spule eilt der Strom um eine viertel Periode der Spannung **nach**

## Bauformen

- Luftspule
  - kann selbst gewickelt werden
  - einzelne Wickelkörper verfügbar
  - einstellbare Abgreifer möglich
- Mit Ferritkern
  - einstellbare Kerne möglich
- Printspule
  - gedruckt auf Leiterplatte
  - UHF-Bereich
- Vermeidung schädlicher Kapazitäten
  - Kreuzwickelspule
  - in Kammern unterteilte Spulenkörper

# Transformator

```
        o--------|   |--------o
    |             ) (            |
    |             ) (            |
U_1 |   N_1       ) (      N_2   | U_2
    |             ) (            |
    V             ) (            V
        o--------|   |--------o

      Primärseite     Sekundärseite
```

* getrennte Spulen die über das gleiche magnetische Feld verbunden sind
* Verhältnisse der **Wechselspannungen** entsprechen denen der Windungen
* man spricht von Primärseite und Sekundärseite

* Übersetzungsverhältnis `ü`
* $ü = \frac{N_1}{N_2} = \frac{U_1}{U_2}$