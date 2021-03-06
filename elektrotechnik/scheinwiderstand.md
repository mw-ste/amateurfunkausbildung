# Scheinwiderstand

## Kondensator

```
      | |     _____
 o----| |----|_____|-----o
      | |
       C        R
```

- der Scheinwiderstand $Z$ setzt sich aus Blindwiderstand $X_C$ und Wirkwiderstand $R$ zusammen
- da der Strom am Kondensator um 90° voraus eilt, ergibt sich folgendes Widerstandsdreieck

```
               R
      +------->
      | *
      |   *
      |     *
X_C   V       * Z
```

- $Z = \sqrt{R^2 + {X_C}^2}$

## Spule

```
                   _____
 o----)()()()(----|_____|-----o
          L          R
```

- der Scheinwiderstand $Z$ setzt sich aus Blindwiderstand $X_L$ und Wirkwiderstand $R$ zusammen
- da der Strom an der Spule um 90° nach eilt, ergibt sich folgendes Widerstandsdreieck

```
X_L   A       * Z
      |     *
      |   *
      | *
      +------->
               R
```

- $Z = \sqrt{R^2 + {X_L}^2}$

## R-L-C Schaltung

```
      | |                 _____
o-----| |----)()()()(----|_____|-----o
      | |
       C        L           R
```

```
X_L   A
      |
      |
      |
      +------->  R                  +------->  R
      |                             |   *
      |                       X_ges v       * Z
      |
      |
      |
X_C   V
```
- der Scheinwiderstand $Z$ setzt sich aus der Summe der entgegengerichteten Blindwiderstande $X_L$ und $X_C$ und dem Wirkwiderstand $R$ zusammen
- im dargestellten Fall überwiegt der kapazitive Anteil