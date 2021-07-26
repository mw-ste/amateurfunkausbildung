# Hochfrequenz-Leitungen

## Wellenwiderstand

- reale Letungen weißen kapazitive und induktive Eigenschaften auf
- diese definieren den Wellenwiderstand einer Leitung
- dabei erscheint:
  - eine Induktivität $L'$ in Reihe (Induktivitätsbelag)
  - eine Kapazität $C'$ parallel (Kapazitätsbelag)
  - ein Leitungswiderstand $R'$ in Reihe
  - ein Isolationswiderstand $R_P$ parallel
- Berechnung des Wellenwiderstands $Z_W = \sqrt{\frac{L'}{C'}}$
- daher ist der Wellenwiderstand unabhängig von der
  - Leitungslänge
  - Frequenz
- Messung
  - $C'$ bei Leerlauf
  - $L'$ bei Kurzschluss

### Paralleldrahtleitung

- $Z_W = \frac{120 \Omega}{\sqrt{\varepsilon_r}} \cdot ln \left( \frac{2a}{d} \right)$
- Mittenabstand $a$, Leiterdurchmesser $d$
- Dielektrizitätszahl $\varepsilon_r$ für Luft: $\varepsilon_r = 1$
- gängige Werte 150$\Omega$ - 600$\Omega$

### Koaxialkabel

- $Z_W = \frac{60 \Omega}{\sqrt{\varepsilon_r}} \cdot ln \left( \frac{D}{d} \right)$
- Innenleiterdurchmesser $d$, Außenleiterdurchmesser $D$
- Dielektrizitätszahl $\varepsilon_r$ für Luft: $\varepsilon_r = 1$
- gängige Werte 50$\Omega$ - 125$\Omega$

### Fehlanpassung

- Fehlanpassung wenn folgende Werte nicht übereinstimmen:
  - Fußpunktwiderstand der Antenne
  - Ausgangswiderstand des Sender
  - Wellenwiderstand des Kabels
- führt zu stehenden Wellen
- Leistung wird reflektiert und nicht übertragen
- bei Anpassung zwischen Leitung und Abschlusswiderstand wird die ganze Leistung abgegeben

## Verkürzungsfaktor

- durch das Dielektrikum erhöht sich die Leitungskapazität
- dadurch sinkt die Ausbreitungsgeschwindigkeit von Strom und Spannung
- Ausbreitungsgeschwindigkeit $v = \frac{1}{\sqrt{L' \cdot C'}}$
- $L'$ in $\frac{H}{m}$, $C'$ in $\frac{F}{m}$
- Verkürzungsfaktor $k = \frac{v}{c}$, $k = \frac{1}{\sqrt·{\varepsilon_r}}$

- Gängige Werte
  - $k = 0.66$: Koaxialkabel
  - $k = 0.85$: Koaxialkabel mit Luftisolation
  - $k = 0.98$: offene $600 \Omega$ Speißeleitung
  - $k = 0.82$: $300 \Omega$ Flachleitung

## Dämpfung

- Angabe in $\frac{dB}{m}$
- die Dämpfung in dB verändert sich mit der Wurzel der Frequenzverhältnisse
- $n = \sqrt{\frac{f_{hoch}}{f_{niedrig}}}$

## SWR
* Standing Wave Ratio SWR
* gleichbedeutend: Voltage Standing Wave Ratio VSWR
* bei Fehlanpassung wird Leistung am Abschluss des Kables reflektiert
* die reflektierte Welle überlagert das eingehende Signal
* aus der Überlagerung bildet sich eine stehende Welle
* das SWR berechnet sich aus Maximum und Minimum der stehenden Welle
* $SWR = \frac{U_{max}}{U_{min}}$
  * für $R_A \geq Z_W$: $SWR = \frac{U_{R_A}}{Z_W}$
  * für $R_A \leq Z_W$: $SWR = \frac{Z_W}{U_{R_A}}$

## Lecherleitung

* Sonderfall einer Transformationsleitung
* kurzes verlustloses Leiterstück, zwei parallele Drähte
* in Leerlauf oder Kurzschluss betrieben
* zur Untersuchung von Hochfrequenzverhalten


## $\lambda$/4-Leitung

#![](https://www.darc.de/fileadmin/filemounts/referate/ajw/Onlinelehrgang/a10/Bild10-8.gif)

* $\frac{N \cdot \lambda}{4}$ für $N$ ungerade
* transformiert niedrige in hohe Widerstände und umgekehrt
* bewirkt eine Phasenverschiebung von 90°

* ein **Kurzschluss** wirkt daher wie ein **unendlich hoher Widerstand**
* ein **Leerlauf** wirkt daher wie ein **unendlich kleiner Widerstand**
* wird die Frequenz variiert so ist es keine exakte $\lambda$/4-Leitung mehr
* der Widerstand beginnt zu steigen bzw. zu sinken
* so betrachtet wirkt der **Kurzschluss** wie eine **Bandsperre / Parallelschwingkreis**
* so betrachtet wirkt der **Leerlauf** wie ein **Bandpass / Serienschwingkreis**

## $\lambda$/2-Leitung

* $\frac{N \cdot \lambda}{4}$ für $N$ gerade
* transformiert Widerstände 1:1
* keine Phasenverschiebung