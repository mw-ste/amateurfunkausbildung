# Elektrotechnik Grundlagen

- [Spannung und Strom, Wechselspannung (E)](https://www.darc.de/der-club/referate/ajw/lehrgang-te/e02/)
- [Ohmsches Gesetz, Leistung, Arbeit (E)](https://www.darc.de/der-club/referate/ajw/lehrgang-te/e03/)
- [Ohmsches Gesetz (A)](https://www.darc.de/der-club/referate/ajw/lehrgang-ta/a02/#Ohmsches)
- [Aufbau von Widertänden (A)](https://www.darc.de/der-club/referate/ajw/lehrgang-ta/a02/#Aufbau)
- [Skin-Effekt (A)](https://www.darc.de/der-club/referate/ajw/lehrgang-ta/a02/#Skin)

# Spannung und Strom, Wechselspannung

## Elektrische Spannung

- Elektrische Spannung resultiert aus einer elektrischen Potienzialdifferenz
- Elektrische Spannung ist das Ausgleichsbestreben unterschiedlicher elektrischer Ladungen
- Minuspol: Elektronenüberschuss
- Pluspol: Elektronenmangel

```
    o            .
    |  (-)      /_\
  __|__          |
_________        | U [V]
    |            |
    |  (+)       |
    o            |
```

- **Formelzeichen**: `U`
- **Einheit**: Volt `V`
- In Reihe geschaltete Spannungen addieren sich auf

## Elektrischer Strom

- werden zwei unterschiedliche elektrische Potenziale leitend verbunden, so findet ein Ladungsausgleich statt
- Dieser Ladungstransport wird als elektrischer Strom bezeichnet
- Damit Strom fließen kann, muss ein geschlossener Stromkreis vorliegen
- **Formelzeichen**: `I`
- **Einheit**: Ampere `A`

- **Technische Stromrichtung**: Definitionsgemäß vom Pluspol zum Minuspol
- **Physiklische Stromrichtung**: Elektronenfluss vom Minuspol zum Pluspol

## Ladungsmenge

- Die Stromstärke ergibt sich aus dem Fluss einer Ladung `Q` über einen bestimmten Zeitraum
- **Formelzeichen**: `Q`
- **Einheit**: Coulomb `C`, bzw Amperesekunde `As`
- `1 C = 1 As`
- Zusammenhang zur Stromstärke: $Q = I \cdot t$ bzw. $I = \frac{Q}{t}$

## Frequenz

- Gleichstrom &lrarr; Wechselstrom
- Verschiedene Kurvenformen möglich, z.B. Rechteck, Sinus

```
    A
    |     __                __                            ---
U   |    /  \              /  \                            |
    |   /    \            /    \                           | Maximum
    |  /      \          /      \                          |
    |-/--------\--------/--------\----------------->  t   ---
    |           \      /          \
    |            \    /            \    /
    |             \__/              \__/
    |

      |-----------------| Periodendauer
```

- Die Frequenz eines Wechselsignals ergibt sich aus der Periodendauer `T` des Signals
- **Formelzeichen**: `f`
- **Einheit**: Hertz `Hz`
- $1 \text{Hz} = \frac{1}{s}$
- Zusammenhang zur Periodendauer: $f = \frac{1}{T}$
- Netzfrequenz Europa: $50 \text{Hz}$
- Netzfrequenz USA: $60 \text{Hz}$
- Hörbare Frequenz: $20 \text{Hz} - 20 \text{kHz}$
- Sprachübertragung im Amateurfunk: $300 \text{Hz} - 3 \text{kHz}$

## Effektivwert des Wechselstroms

```
A
|     __                      ---                 ---
|    /  \                      |        ---        |
|   /    \                     | U_max   | U_eff   | U_ss
|  /      \                    |         |         |
|-/--------\--------/--->  t  ---       ---        |
|           \      /                               |
|            \    /                                |
|             \__/                                 |
|                                                 ---
```

- Effektifwert: $U_{\text{eff}}$
- Maximalwert/Scheitelwert: $U_{\text{max}}$
- Spitze-Spitze-Wert: $U_{\text{ss}}$
- Bei Sinussignalen: $U_{\text{eff}} = \frac{U_{\text{max}}}{\sqrt{2}}$
- $U_{\text{eff}} \approx 70,7\% \cdot U_{\text{max}}$
- Beim deutschen Wechselstromnetz: $U_{\text{eff}} = 230V$
- Wenn nicht weiter angegeben: Effektivwert

# Ohmsches Gesetz, Leistung, Arbeit

## Widerstand

- Schaltzeichen

```
         ________
    o---|________|---o   R
```

- **Formelzeichen**: `R`
- **Einheit**: Ohm $\Omega$, bzw. $\frac{V}{A}$

- Definitionsgemäß fällt an einem Widerstand von `1 Ohm` bei einem Stromfluss von `1 Ampere` eine Spannung von `1 Volt` ab.
- Ohmsches Gesetz: $U = R \cdot I$
- Oder umgestellt: $R = \frac{U}{I}$ bzw. $I = \frac{U}{R}$

## Innenwiderstand

- Generatoren und Quellen haben einen Innenwiderstand $R_i$
- Bei zunehmender Stromentnahme an der Quelle sinkt deren Spannung entsprechend des Innenwiderstands
- Der Innenwiderstand lässt sich auch der Veränderung $\Delta$ von Strom und Spannung errechnen
- $R_i = \frac{\Delta U}{\Delta I}$

## Elektrische Leistung

- An elektrischen Bauteilen kann Leistung wie thermische oder mechanische Leistung frei werden
- Die Leistung errechnet sich aus dem fließenden Strom und der am Bauteil abfallenden Leistung
- **Formelzeichen**: `P` (power)
- **Einheit**: Watt `W`, bzw. $V \cdot A$
- Berechnung: $P = U \cdot I$
- Gilt grundsätzlich bei Gleichstrom
- Bei Wechselstrom nur für ohmsche Anteile

## Elektrische Arbeit

- die verrichtete Arbeit ergibt sich aus der Leistung und dem Zeitraum, über den sie erbracht wurde
- **Formelzeichen**: `W` (work)
- **Einheit**: Wattsekunde `Ws`, bzw. `VAs`
- Außerdem gängig: Kilowattstunde `kWh`
- "Gespeicherte Arbeit" &rarr; elektrische Energie
