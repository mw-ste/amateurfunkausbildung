# Widerstände

## Bauformen von Widerständen

- Festwiderstände
- Einstellbare Widerstände (z.B. mechanisch einstellbar: Potentiometer)
- Veränderliche Widerstände (z.B. abhängig von Temperatur oder Lichteinstrahlung)

![widerstaende](https://www.darc.de/fileadmin/filemounts/referate/ajw/Onlinelehrgang/e04/Bild04-01.gif)

- A: Festwiderstand
- B: Von außen einstellbarer Widerstand (Potentiometer)
- C: Interner einstellbarer Widerstand (Trimmer)
- D: Allgemeines Schaltzeichen für einstellbaren Widerstand

![widerstaende](https://www.darc.de/fileadmin/filemounts/referate/ajw/Onlinelehrgang/e04/Bild04-04.gif)

- A: PTC (positive temp coefficient), Widerstand steigt mit der Temperatur
- B: NTC (negative temp coefficient), Widerstand sinkt mit der Temperatur
- C: VDR (voltage dependend resistor), spannungsgesteuerter Widerstand
- D: LDR (light dependend resistor), Photoresistor

## Festwiderstände

- Kohleschichtwiderstände:
  - dünne Kohleschicht als Widerstandsmaterial
  - billig, aber große Herstellungstoleranz
  - Belastbarkeit zwischen 0.1 bis 2 Watt
- Metallschichtwiderstände:
  - (Edel-) Metallschicht als Widerstandsmaterial
  - Präzisionswiderstände
  - Induktionsarm
  - höhere Belastbarkeit
- Metalloxidwiderstände:
  - besonders für Hochfrequenz geeignet
- Drahtwiderstände:
  - auf keramischen Isolierkörper gewickelter Widerstandsdraht als Widerstandsmaterial
  - Hochlastwiderstände
  - nur im Niederfrequenzbereich (wegen Frequenzabhängigkeit durch Induktivität)

## Spezifischer Widerstand

- der Widerstand eines Leiter ist abhängig vom Leiterquerschnitt, der Leiterlänge und dem Material aus dem der Leiter gefertigt ist
- die Materialabhängigkeit wird durch den spezifischen Widerstand $\rho$ charakterisiert
- die Einheit des spezifischen Widerstands ist $\frac{\Omega \cdot mm^2}{m} = \frac{A \cdot m}{V \cdot mm^2}$
- der Widerstand steigt mit zunehmender Länge, zunehmendem spezifischen Widerstand und abnehmendem Querschnitt
- der Kehrwert des spezifischen Widerstands ist die elektrische Leitfähigkeit $\kappa = \frac{1}{\rho}$

| Material    | spezifischer Widerstand $\left[ \frac{\Omega \cdot mm^2}{m} \right]$ | Leitfähigkeit $\left[ \frac{m}{\Omega \cdot mm^2} \right]$ |
| ----------- | -------------------------------------------------------------------- | ---------------------------------------------------------- |
| Silber      | 0.016                                                                | 63                                                         |
| Kupfer      | 0.0178                                                               | 58                                                         |
| Gold        | 0.022                                                                | 45                                                         |
| Aluminium   | 0.027                                                                | 37                                                         |
| Eisen       | 0.10                                                                 | 10                                                         |
| Zinn        | 0.115                                                                | 8                                                          |
| Blei        | 0.208                                                                | 5                                                          |
| Quecksilber | 0.958                                                                | 1                                                          |

- Widerstand eines Leiter nach der obigen Tabelle: $R = \frac{\rho \cdot l}{A}$
- Leiterdurchmesser $A$ in $mm^2$

## Temperaturkoeffizienten
