1. Enlace simulador de la [respuesta 1](https://circuitverse.org/users/308909/projects/respuesta-1)

# Tabla de Verdad para la Función Lógica
**Función:** F = A · B + ¬C

Esta función tiene tres variables de entrada: A, B y C. Se utilizan las siguientes operaciones:
- `·` → AND (multiplicación lógica)
- `+` → OR (suma lógica)
- `¬` → NOT (negación lógica)

---

## Tabla de Verdad

| A | B | C | A·B | ¬C | F = A·B + ¬C |
|---|---|---|-----|----|--------------|
| 0 | 0 | 0 |  0  | 1  |      1       |
| 0 | 0 | 1 |  0  | 0  |      0       |
| 0 | 1 | 0 |  0  | 1  |      1       |
| 0 | 1 | 1 |  0  | 0  |      0       |
| 1 | 0 | 0 |  0  | 1  |      1       |
| 1 | 0 | 1 |  0  | 0  |      0       |
| 1 | 1 | 0 |  1  | 1  |      1       |
| 1 | 1 | 1 |  1  | 0  |      1       |

---

## Explicación
- La salida **F** será igual a 1 cuando:
  - **A y B** sean ambos 1 (A·B = 1), **o**
  - **C** sea 0 (¬C = 1).
- En otras palabras, la función se activa si:
  - A y B están activados simultáneamente, o
  - C está desactivado.

------------------------

2. Enlace simulador de la [respuesta 2](https://circuitverse.org/users/309145/projects/respuesta-2-a8bfea0b-38d4-4d41-bcfd-343fe6c6c696)

# Tabla de Verdad para la Función 
**Función**: F = (A + B) · C 

Esta función tiene tres variables de entrada: A, B y C. Se utilizan las siguientes operaciones:

+ → OR (suma lógica)

· → AND (multiplicación lógica)

## ----♠-Tabla de Verdad---♠---
----------------------------------------
| A | B | C  | A + B | (A + B) · C = F |
|---|---|----|-------|-----------------|
| 0 | 0 | 0  |   0   |        0        |
| 0 | 0 | 1  |   0   |        0        |
| 0 | 1 | 0  |   1   |        0        |
| 0 | 1 | 1  |   1   |        1        |
| 1 | 0 | 0  |   1   |        0        |
| 1 | 0 | 1  |   1   |        1        |
| 1 | 1 | 0  |   1   |        0        |
| 1 | 1 | 1  |   1   |        1        |
----------------------------------------
# Explicación
Primero se hace la suma lógica: A + B

Luego se multiplica ese resultado con C

La salida F será igual a 1 solamente cuando C sea 1 y al menos uno de A o B también sea 1.

Es decir, C activa la salida solo si A o B está activo.


---------------------------
3. Enlace simulador de la [respuesta 3](https://circuitverse.org/users/309145/projects/respuesta-3-091ce02b-8c0b-4be0-a7d2-eceec7386965)

# Tabla de Verdad para la Función 
**Función**: F = ¬(A · B)

Esta función tiene dos variables de entrada: A y B. Se utilizan las siguientes operaciones:

· → AND (multiplicación lógica)

¬ → NOT (negación lógica)

# Tabla de Verdad para la Función NAND: **F = ¬(A · B)**
-----------------------------------------------------
|   A   |   B   |   A · B   |   F = ¬(A · B)   |
|:-----:|:-----:|:---------:|:----------------:|
|   0   |   0   |     0     |        1         |
|   0   |   1   |     0     |        1         |
|   1   |   0   |     0     |        1         |
|   1   |   1   |     1     |        0         |
------------------------------------------------------------
## Explicación
Primero se hace la multiplicación lógica: A · B

Luego se aplica la negación: ¬(A · B)

La salida F será igual a 1 en todos los casos excepto cuando A y B sean ambos 1.

Esta función también se puede implementar directamente con una compuerta NAND.

--------------
4. Enlace simulador de la [respuesta 4](https://circuitverse.org/users/309145/projects/respuesta-4-520cabd3-1b70-47ca-a6ac-19bf47c59ff2)

# Tabla de Verdad para la Función Lógica
Función: F = (A ⊕ B) + (¬C · D)

Variables de entrada: A, B, C, D
Operaciones utilizadas:

⊕ → XOR (suma exclusiva)

¬ → NOT (negación)

· → AND (multiplicación lógica)

+ → OR (suma lógica)

# Tabla de Verdad para la Función: F = (A ⊕ B) + (¬C · D)

| A | B | C | D | A ⊕ B (XOR) | ¬C (NOT) | ¬C · D (AND)| F = (A ⊕ B) + (¬C · D) (OR)|
|:-:|:-:|:-:|:-:|:-----------:|:--------:|:------------:|:---------------------------:|
| 0 | 0 | 0 | 0 |      0      |    1     |      0       |              0             |
| 0 | 0 | 0 | 1 |      0      |    1     |      1       |              1             |
| 0 | 0 | 1 | 0 |      0      |    0     |      0       |              0             |
| 0 | 0 | 1 | 1 |      0      |    0     |      0       |              0             |
| 0 | 1 | 0 | 0 |      1      |    1     |      0       |              1             |
| 0 | 1 | 0 | 1 |      1      |    1     |      1       |              1             |
| 0 | 1 | 1 | 0 |      1      |    0     |      0       |              1             |
| 0 | 1 | 1 | 1 |      1      |    0     |      0       |              1             |
| 1 | 0 | 0 | 0 |      1      |    1     |      0       |              1             |
| 1 | 0 | 0 | 1 |      1      |    1     |      1       |              1             |
| 1 | 0 | 1 | 0 |      1      |    0     |      0       |              1             |
| 1 | 0 | 1 | 1 |      1      |    0     |      0       |              1             |
| 1 | 1 | 0 | 0 |      0      |    1     |      0       |              0             |
| 1 | 1 | 0 | 1 |      0      |    1     |      1       |              1             |
| 1 | 1 | 1 | 0 |      0      |    0     |      0       |              0             |
| 1 | 1 | 1 | 1 |      0      |    0     |      0       |              0             |

# Explicación
A ⊕ B se activa si A y B son diferentes.

¬C · D se activa si C = 0 y D = 1.

El resultado F será 1 si al menos una de estas dos condiciones se cumple.

---------------------



5. Enlace simulador de la [respuesta 5](https://circuitverse.org/users/309145/projects/respuesta-5-21a43a86-d27f-4b53-bbc5-4e05583f7a3b)

# Tabla de Verdad para la Función Lógica
**Función**: F = ¬(A + B + C)

Variables de entrada: A, B, C
Operaciones utilizadas:

+ → OR (suma lógica)

¬ → NOT (negación lógica)

# Tabla de Verdad para la Función: F = ¬(A + B + C)

| A | B | C | A + B + C (OR) | F = ¬(A + B + C) (NOR) |
|:-:|:-:|:-:|:--------------:|:----------------------:|
| 0 | 0 | 0 |       0        |           1            |
| 0 | 0 | 1 |       1        |           0            |
| 0 | 1 | 0 |       1        |           0            |
| 0 | 1 | 1 |       1        |           0            |
| 1 | 0 | 0 |       1        |           0            |
| 1 | 0 | 1 |       1        |           0            |
| 1 | 1 | 0 |       1        |           0            |
| 1 | 1 | 1 |       1        |           0            |


# Explicación
La operación A + B + C activa la salida si cualquiera de las entradas es 1.

Luego, ¬(A + B + C) será 1 solo si todas las entradas son 0.

Esta función también se puede implementar directamente con una compuerta NOR.

--------

6. Enlace simulador de la [respuesta 6](https://circuitverse.org/users/309145/projects/respuesta-6-1c1f7e8d-08b5-4583-a2b2-f14804660f9b)

# Tabla de Verdad para la Función Lógica
Función: F = (A · ¬B) + (C ⊕ D)

Variables de entrada: A, B, C, D
Operaciones utilizadas:

· → AND

¬ → NOT

+ → OR

⊕ → XOR

# Tabla de Verdad para la Función: F = (A · ¬B) + (C ⊕ D)

| A | B | C | D | ¬B | A · ¬B | C ⊕ D | F = (A · ¬B) + (C ⊕ D) |
|:-:|:-:|:-:|:-:|:--:|:------:|:-----:|:----------------------:|
| 0 | 0 | 0 | 0 | 1  |   0    |   0   |           0            |
| 0 | 0 | 0 | 1 | 1  |   0    |   1   |           1            |
| 0 | 0 | 1 | 0 | 1  |   0    |   1   |           1            |
| 0 | 0 | 1 | 1 | 1  |   0    |   0   |           0            |
| 0 | 1 | 0 | 0 | 0  |   0    |   0   |           0            |
| 0 | 1 | 0 | 1 | 0  |   0    |   1   |           1            |
| 0 | 1 | 1 | 0 | 0  |   0    |   1   |           1            |
| 0 | 1 | 1 | 1 | 0  |   0    |   0   |           0            |
| 1 | 0 | 0 | 0 | 1  |   1    |   0   |           1            |
| 1 | 0 | 0 | 1 | 1  |   1    |   1   |           1            |
| 1 | 0 | 1 | 0 | 1  |   1    |   1   |           1            |
| 1 | 0 | 1 | 1 | 1  |   1    |   0   |           1            |
| 1 | 1 | 0 | 0 | 0  |   0    |   0   |           0            |
| 1 | 1 | 0 | 1 | 0  |   0    |   1   |           1            |
| 1 | 1 | 1 | 0 | 0  |   0    |   1   |           1            |
| 1 | 1 | 1 | 1 | 0  |   0    |   0   |           0            |

# Explicación
A · ¬B se activa si A = 1 y B = 0

C ⊕ D se activa si C y D son diferentes

La salida F es 1 si al menos una de esas dos condiciones es verdadera


-------------------
7. Enlace simulador de la [respuesta 7](https://circuitverse.org/users/309145/projects/respuesta-7-9c8a8e0a-4603-43ae-a5c0-4ebef8057177)

# Tabla de Verdad para la Función Lógica
Función: F = ((A + B) · C) ⊕ D

Variables: A, B, C, D
Operaciones:

+ → OR

· → AND

⊕ → XOR

# Tabla de Verdad para la Función: F = ((A + B) · C) ⊕ D

| A | B | C | D | A + B | (A + B) · C | F = ((A + B) · C) ⊕ D |
|:-:|:-:|:-:|:-:|:-----:|:-----------:|:---------------------:|
| 0 | 0 | 0 | 0 |   0   |      0      |           0           |
| 0 | 0 | 0 | 1 |   0   |      0      |           1           |
| 0 | 0 | 1 | 0 |   0   |      0      |           0           |
| 0 | 0 | 1 | 1 |   0   |      0      |           1           |
| 0 | 1 | 0 | 0 |   1   |      0      |           0           |
| 0 | 1 | 0 | 1 |   1   |      0      |           1           |
| 0 | 1 | 1 | 0 |   1   |      1      |           1           |
| 0 | 1 | 1 | 1 |   1   |      1      |           0           |
| 1 | 0 | 0 | 0 |   1   |      0      |           0           |
| 1 | 0 | 0 | 1 |   1   |      0      |           1           |
| 1 | 0 | 1 | 0 |   1   |      1      |           1           |
| 1 | 0 | 1 | 1 |   1   |      1      |           0           |
| 1 | 1 | 0 | 0 |   1   |      0      |           0           |
| 1 | 1 | 0 | 1 |   1   |      0      |           1           |
| 1 | 1 | 1 | 0 |   1   |      1      |           1           |
| 1 | 1 | 1 | 1 |   1   |      1      |           0           |

## Explicación
Primero se hace A + B, luego se multiplica con C

Después se hace XOR del resultado con D

La salida será 1 cuando los valores de ((A+B)·C) y D sean diferentes

-------------
-----

8. Enlace simulador de la [respuesta 8](https://circuitverse.org/users/309145/projects/respuesta-8-8f1460dc-d530-4791-a780-92fa0220002d)


# Tabla de Verdad para la Función Lógica
**Función**: F = (A · B) ⊙ (C + D)

Variables: A, B, C, D
Operaciones:

· → AND

+ → OR

⊙ → XNOR (complemento de XOR)


# Tabla de Verdad para la Función: F = (A · B) ⊙ (C + D)

| A | B | C | D | A · B | C + D | F = (A · B) ⊙ (C + D) |
|:-:|:-:|:-:|:-:|:-----:|:-----:|:---------------------:|
| 0 | 0 | 0 | 0 |   0   |   0   |           1           |
| 0 | 0 | 0 | 1 |   0   |   1   |           0           |
| 0 | 0 | 1 | 0 |   0   |   1   |           0           |
| 0 | 0 | 1 | 1 |   0   |   1   |           0           |
| 0 | 1 | 0 | 0 |   0   |   0   |           1           |
| 0 | 1 | 0 | 1 |   0   |   1   |           0           |
| 0 | 1 | 1 | 0 |   0   |   1   |           0           |
| 0 | 1 | 1 | 1 |   0   |   1   |           0           |
| 1 | 0 | 0 | 0 |   0   |   0   |           1           |
| 1 | 0 | 0 | 1 |   0   |   1   |           0           |
| 1 | 0 | 1 | 0 |   0   |   1   |           0           |
| 1 | 0 | 1 | 1 |   0   |   1   |           0           |
| 1 | 1 | 0 | 0 |   1   |   0   |           0           |
| 1 | 1 | 0 | 1 |   1   |   1   |           1           |
| 1 | 1 | 1 | 0 |   1   |   1   |           1           |
| 1 | 1 | 1 | 1 |   1   |   1   |           1           |

# Explicación
El resultado será 1 si A·B y C+D tienen el mismo valor (ambos 0 o ambos 1)

Esto es lo que hace la compuerta XNOR

-------------------
--------------

9. Enlace simulador de la [respuesta 9](https://circuitverse.org/users/309145/projects/respuesta-9-45675e1b-4952-41b8-86c8-ff074cdc8aac)

# Tabla de Verdad para la Función 
**Función**: F = ¬A · (B + ¬C)

Variables: A, B, C
Operaciones:

¬ → NOT

+ → OR

· → AND

# Tabla de Verdad para la Función: F = ¬A · (B + ¬C)

| A | B | C | ¬A | ¬C | B + ¬C | F = ¬A · (B + ¬C) |
|:-:|:-:|:-:|:--:|:--:|:------:|:----------------:|
| 0 | 0 | 0 | 1  | 1  |   1    |        1         |
| 0 | 0 | 1 | 1  | 0  |   0    |        0         |
| 0 | 1 | 0 | 1  | 1  |   1    |        1         |
| 0 | 1 | 1 | 1  | 0  |   1    |        1         |
| 1 | 0 | 0 | 0  | 1  |   1    |        0         |
| 1 | 0 | 1 | 0  | 0  |   0    |        0         |
| 1 | 1 | 0 | 0  | 1  |   1    |        0         |
| 1 | 1 | 1 | 0  | 0  |   1    |        0         |

# Explicación
Se activa cuando A = 0 y al menos una de estas condiciones se cumple:

B = 1

C = 0


**-*-*-*-*-*-*-**
---------***--

10. Enlace simulador de la [respuesta 10](https://circuitverse.org/users/309145/projects/respuesta-10-b58e2c89-4aac-4d93-b0ae-4f6b34f01edb)

# Tabla de Verdad para la Función Lógica
**Función**: F = ((A ⊕ B) · ¬C) + D

Variables: A, B, C, D
Operaciones:

⊕ → XOR

¬ → NOT

· → AND

+ → OR

# Tabla de Verdad para la Función: F = ((A ⊕ B) · ¬C) + D

| A | B | C | D | A ⊕ B | ¬C | (A ⊕ B)·¬C | F = ((A ⊕ B)·¬C) + D |
|:-:|:-:|:-:|:-:|:-----:|:--:|:----------:|:---------------------:|
| 0 | 0 | 0 | 0 |   0   | 1  |     0      |           0           |
| 0 | 0 | 0 | 1 |   0   | 1  |     0      |           1           |
| 0 | 0 | 1 | 0 |   0   | 0  |     0      |           0           |
| 0 | 0 | 1 | 1 |   0   | 0  |     0      |           1           |
| 0 | 1 | 0 | 0 |   1   | 1  |     1      |           1           |
| 0 | 1 | 0 | 1 |   1   | 1  |     1      |           1           |
| 0 | 1 | 1 | 0 |   1   | 0  |     0      |           0           |
| 0 | 1 | 1 | 1 |   1   | 0  |     0      |           1           |
| 1 | 0 | 0 | 0 |   1   | 1  |     1      |           1           |
| 1 | 0 | 0 | 1 |   1   | 1  |     1      |           1           |
| 1 | 0 | 1 | 0 |   1   | 0  |     0      |           0           |
| 1 | 0 | 1 | 1 |   1   | 0  |     0      |           1           |
| 1 | 1 | 0 | 0 |   0   | 1  |     0      |           0           |
| 1 | 1 | 0 | 1 |   0   | 1  |     0      |           1           |
| 1 | 1 | 1 | 0 |   0   | 0  |     0      |           0           |
| 1 | 1 | 1 | 1 |   0   | 0  |     0      |           1           |
# Explicación
Se activa si:

A y B son diferentes y C = 0, o

D = 1

---------------------


# --------------------------------------------------------------
# ----------------AUTOR: FERNANDO SAAVEDRA------------
# --------------------------------------------------------------