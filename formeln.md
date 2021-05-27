# Mathematik und Formeln

## Allgemein

| Kürzel | Name  | Zehnerpotenz |
| ------ | ----- | ------------ |
| p      | Pico  | $10^{-12}$   |
| n      | Nano  | $10^{-9}$    |
| µ      | Mikro | $10^{-6}$    |
| m      | Milli | $10^{-3}$    |
|        |       | $10^{0}$     |
| k      | Kilo  | $10^{3}$     |
| M      | Mega  | $10^{6}$     |
| G      | Giga  | $10^{9}$     |
| T      | Tera  | $10^{12}$    |

## Formeln

### Lichtgeschwindigkeit

Lichtgeschwindigkeit: $c_0 = 2.99 \cdot 10^8 \frac{m}{s}$

Zusammenhang Frequenz und Wellenlänge:

- $\lambda = \frac{c_0}{f}$
- $f = \frac{c_0}{\lambda}$

Umrechnung Wellenlänge in `m` zu Frequenz in `MHz`:

- $\lambda = \frac{299 \frac{m}{\mu s}}{f_{\text{MHz}}}$
- $f_{\text{MHz}} = \frac{299 \frac{m}{\mu s}}{\lambda}$

### MUF

- $\text{MUF} \approx \frac{f_k}{sin \left( \alpha \right)} |_{\alpha \ge 40°}$
- $\text{MUF} \approx \frac{f_k}{sin \left( \alpha \right)} = \frac{f_k}{cos \left( \varphi \right)}$
- $\alpha$ Abstrahlungswinkel über der Horizontalen
- $\varphi$ Winkel zwischen Einstrahlwinkel und Senkrechter an F2
- $f_{opt} \approx 0.85 \cdot \text{MUF}$

### Widerstand und Leistung

- $U = R \cdot I$
- $P = U \cdot I$
- $P = I^2 \cdot R$
- $P = \frac{U^2}{R}$

### Dämpfung

- Leistung
  - Dämpfung $a_P = 10 \cdot log \left( \frac{P_I}{P_O} \right) \text{dB}$
  - Verstärkung $g = 10 \cdot log \left( \frac{P_O}{P_I} \right) \text{dB}$
- Spannung
  - Dämpfung $a_U = 20 \cdot log \left( \frac{U_I}{U_O} \right) \text{dB}$

### Kreis
* Fläche $A = r^2 \cdot \pi$