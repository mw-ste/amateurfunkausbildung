# Hochfrequenz-Leitungen

## Wellenwiderstand

* reale Letungen weißen kapazitive und induktive Eigenschaften auf
* diese definieren den Wellenwiderstand einer Leitung
* dabei erscheint:
    * eine Induktivität $L'$ in Reihe (Induktivitätsbelag)
    * eine Kapazität $C'$ parallel (Kapazitätsbelag)
    * ein Leitungswiderstand $R'$ in Reihe
    * ein Isolationswiderstand $R_P$ parallel
* Berechnung des Wellenwiderstands $Z_W = \sqrt{\frac{L'}{C'}}$
* daher ist der Wellenwiderstand unabhängig von der
    * Leitungslänge
    * Frequenz
* Messung
    * $C'$ bei Leerlauf
    * $L'$ bei Kurzschluss
* Geometrische Berechnung
    * Paralleldrahtleitung $Z_W = \frac{120 \Omega}{\sqrt{\varepsilon_r}} \cdot ln \left( \frac{2a}
{d} \right)$
    * Mittenabstand $a$, Leiterdurchmesser $d$
    * Koaxialkabel $Z_W = \frac{60 \Omega}{\sqrt{\varepsilon_r}} \cdot ln \left( \frac{D}{d} \right)$
    * Innenleiterdurchmesser $d$, Außenleiterdurchmesser $D$
    * Dielektrizitätszahl $\varepsilon_r$ für Luft: $\varepsilon_r = 1$

### Fehlanpassung
* Fehlanpassung wenn folgende Werte nicht übereinstimmen:
    * Fußpunktwiderstand der Antenne
    * Ausgangswiderstand des Sender
    * Wellenwiderstand des Kabels
* führt zu stehenden Wellen
* Leistung wird reflektiert und nicht übertragen
* bei Anpassung zwischen Leitung und Abschlusswiderstand wird die ganze Leistung abgegeben