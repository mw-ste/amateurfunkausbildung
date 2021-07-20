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
