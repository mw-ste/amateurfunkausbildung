# Dämpfung

## Dämpfungsfaktor

- Dämpfungsfaktor $D_P$ gibt das Verhältnis zwischen Eingangsleistung $P_I$ und Ausgangsleitung $P_O$ an
- $D_P = \frac{P_I}{P_O}$
- bei mehreren Einzeldämpfungen in Serie müssen die Dämpfungsfaktoren miteinander multipliziert werden

## Logarithmus

- $lg = log_{10}$
- $ln = log_{e}$
- $ld = log_{2}$
- $log \left( a \cdot b \right) = log \left( a \right) + log \left( b \right)$
- $log \left( \frac{a}{b} \right) = log \left( a \right) - log \left( b \right)$

## Dämpfungsmaß in `dB`

- zur einfacheren Berechnung der Gesamtdämpfung kann die Dämpfung $a_P$ in `dB` berechnet werden
- dabei werden die Einzeldämpfungen in `dB` addiert
- Berechnung: $a_P = 10 \cdot log \left( \frac{P_I}{P_O} \right) \text{dB}$
- die Dämpfung wird hierbei auf die Leistung bezogen

## Verstärkung in `db`

- Analog zur Dämpfung kann auch die Verstärkung $g$ in `dB` berechnet werden
- Berechnung: $g = 10 \cdot log \left( \frac{P_O}{P_I} \right) \text{dB}$
- die Verstärkung wird hierbei auf die Leistung bezogen

## Verrechnung

- bei der Verrechnung von Dämpfung und Verstärkung wird die Dämpfung als negative Verstärkung behandelt

## Umrechnung in Faktor

- `0dB` entsprechen einem Faktor `1`
- `3dB` entsprechen einem Faktor `2`
- `6dB` entsprechen einem Faktor `4`
- `10dB` entsprechen einem Faktor `10`
- `20dB` entsprechen einem Faktor `100` ($10 dB + 10 dB = 10 \cdot 10$)

## Spannungsdämpfungsmaß in `dB`

- die Dämpfung in `dB` bezieht sich auf die Leistung
- für die Dämpfungsberechnung der Spannung gilt ein anderer Vorfaktor
- Berechnung: $a_U = 20 \cdot log \left( \frac{U_I}{U_O} \right) \text{dB}$
- durch den geänderten Faktor ergeben sich andere Faktoren
- `6dB` entsprechen einem Faktor `2`
- `12dB` entsprechen einem Faktor `4`
- `20dB` entsprechen einem Faktor `10`

## S-Stufen

- zur Angabe der Empfangsfeldstärke im RST-System
- bezogen auf die Empfangsspannung am $50 \Omega$ Eingang
- eine S-Stufen entspricht 6dB, also Faktor 2 (Spannungsdämpfung!)
- `S9` entspricht:
  - $50 \mu V$ bei KW
  - $5 \mu V$ bei UKW

|      | KW           | UKW          |
| ---- | ------------ | ------------ |
| `S9` | $50 \mu V$   | $5 \mu V$    |
| `S8` | $25 \mu V$   | $2.5 \mu V$  |
| `S7` | $12.5 \mu V$ | $1.25 \mu V$ |
| `S6` | $6.25 \mu V$ | $0.62 \mu V$ |
| `S5` | $3.12 \mu V$ | $0.31 \mu V$ |
| `S4` | $1.56 \mu V$ | $0.16 \mu V$ |
| `S3` | $0.78 \mu V$ | $0.08 \mu V$ |
| `S2` | $0.39 \mu V$ | $0.04 \mu V$ |
| `S1` | $0.2 \mu V$  | $0.02 \mu V$ |
