## Ejercicio 1
**Función lógica:**  
**F = A · B + ¬C**

- Usa compuertas AND, OR y NOT.
- Requiere tres entradas: A, B y C.

[Respuesta 1](https://circuitverse.org/simulator/embed/ejercicio-1-b5102557-f180-487d-a979-c22d11e788da)

## Tabla de Verdad

Función lógica: `F = A · B + ¬C`

| A | B | C | A·B | ¬C | F = (A·B) + ¬C |
|---|---|---|-----|----|----------------|
| 0 | 0 | 0 |  0  | 1  |       1        |
| 0 | 0 | 1 |  0  | 0  |       0        |
| 0 | 1 | 0 |  0  | 1  |       1        |
| 0 | 1 | 1 |  0  | 0  |       0        |
| 1 | 0 | 0 |  0  | 1  |       1        |
| 1 | 0 | 1 |  0  | 0  |       0        |
| 1 | 1 | 0 |  1  | 1  |       1        |
| 1 | 1 | 1 |  1  | 0  |       1        |

## Ejercicio 2
**Función lógica:**  
**F = (A + B) · C**

- Usa compuertas OR y AND.
- Requiere tres entradas.

[Respuesta 2](https://circuitverse.org/simulator/embed/ejercicio-2-59c565ae-9ec7-4bf7-a208-8c5ed5beab5a)

## Tabla de Verdad

Función lógica: `F = (A + B) · C`

| A | B | C | A+B | (A+B)·C = F |
|---|---|---|-----|--------------|
| 0 | 0 | 0 |  0  |      0       |
| 0 | 0 | 1 |  0  |      0       |
| 0 | 1 | 0 |  1  |      0       |
| 0 | 1 | 1 |  1  |      1       |
| 1 | 0 | 0 |  1  |      0       |
| 1 | 0 | 1 |  1  |      1       |
| 1 | 1 | 0 |  1  |      0       |
| 1 | 1 | 1 |  1  |      1       |

## Ejercicio 3
**Función lógica:**  
**F = ¬(A · B)**

- Usa una compuerta NAND o una AND seguida de NOT.
- Requiere dos entradas.

[Respuesta 3](https://circuitverse.org/simulator/embed/respuesta-3)

## Tabla de Verdad

Función lógica: `F = ¬(A · B)`

| A | B | A·B | ¬(A·B) = F |
|---|---|-----|-------------|
| 0 | 0 |  0  |      1      |
| 0 | 1 |  0  |      1      |
| 1 | 0 |  0  |      1      |
| 1 | 1 |  1  |      0      |

## Ejercicio 4
**Función lógica:**  
**F = (A ⊕ B) + (¬C · D)**

- Usa compuertas XOR, NOT, AND y OR.
- Cuatro entradas: A, B, C y D.

[Respuesta 4](https://circuitverse.org/simulator/embed/ejercicio-4-47153018-66dc-466f-b940-4af82e9e8bbe)

## Tabla de Verdad

Función lógica: `F = (A ⊕ B) + (¬C · D)`

| A | B | C | D | A⊕B | ¬C | ¬C·D | F = (A⊕B) + (¬C·D) |
|---|---|---|---|-----|----|------|---------------------|
| 0 | 0 | 0 | 0 |  0  |  1 |  0   |         0           |
| 0 | 0 | 0 | 1 |  0  |  1 |  1   |         1           |
| 0 | 0 | 1 | 0 |  0  |  0 |  0   |         0           |
| 0 | 0 | 1 | 1 |  0  |  0 |  0   |         0           |
| 0 | 1 | 0 | 0 |  1  |  1 |  0   |         1           |
| 0 | 1 | 0 | 1 |  1  |  1 |  1   |         1           |
| 0 | 1 | 1 | 0 |  1  |  0 |  0   |         1           |
| 0 | 1 | 1 | 1 |  1  |  0 |  0   |         1           |
| 1 | 0 | 0 | 0 |  1  |  1 |  0   |         1           |
| 1 | 0 | 0 | 1 |  1  |  1 |  1   |         1           |
| 1 | 0 | 1 | 0 |  1  |  0 |  0   |         1           |
| 1 | 0 | 1 | 1 |  1  |  0 |  0   |         1           |
| 1 | 1 | 0 | 0 |  0  |  1 |  0   |         0           |
| 1 | 1 | 0 | 1 |  0  |  1 |  1   |         1           |
| 1 | 1 | 1 | 0 |  0  |  0 |  0   |         0           |
| 1 | 1 | 1 | 1 |  0  |  0 |  0   |         0           |

## Ejercicio 5
**Función lógica:**  
**F = ¬(A + B + C)**

- Usa compuertas OR y NOT o una NOR directa.
- Requiere tres entradas.

[Respuesta 5](https://circuitverse.org/simulator/embed/ejercicio-5-fdd3bb86-04bc-42fa-902a-4b5ca9863a14)

## Tabla de Verdad

Función lógica: `F = ¬(A + B + C)`

| A | B | C | A+B+C | ¬(A+B+C) = F |
|---|---|---|--------|---------------|
| 0 | 0 | 0 |   0    |       1       |
| 0 | 0 | 1 |   1    |       0       |
| 0 | 1 | 0 |   1    |       0       |
| 0 | 1 | 1 |   1    |       0       |
| 1 | 0 | 0 |   1    |       0       |
| 1 | 0 | 1 |   1    |       0       |
| 1 | 1 | 0 |   1    |       0       |
| 1 | 1 | 1 |   1    |       0       |

## Ejercicio 6
**Función lógica:**  
**F = (A · ¬B) + (C ⊕ D)**

- Usa compuertas AND, NOT, OR y XOR.
- Cuatro entradas.

[Respuesta 6](https://circuitverse.org/simulator/embed/ejercicio-6-5548a35c-e259-4576-b639-dbdeb7c02464)

## Tabla de Verdad

Función lógica: `F = (A · ¬B) + (C ⊕ D)`

| A | B | C | D | ¬B | A·¬B | C⊕D | F = (A·¬B) + (C⊕D) |
|---|---|---|---|----|------|------|---------------------|
| 0 | 0 | 0 | 0 |  1 |  0   |  0   |         0           |
| 0 | 0 | 0 | 1 |  1 |  0   |  1   |         1           |
| 0 | 0 | 1 | 0 |  1 |  0   |  1   |         1           |
| 0 | 0 | 1 | 1 |  1 |  0   |  0   |         0           |
| 0 | 1 | 0 | 0 |  0 |  0   |  0   |         0           |
| 0 | 1 | 0 | 1 |  0 |  0   |  1   |         1           |
| 0 | 1 | 1 | 0 |  0 |  0   |  1   |         1           |
| 0 | 1 | 1 | 1 |  0 |  0   |  0   |         0           |
| 1 | 0 | 0 | 0 |  1 |  1   |  0   |         1           |
| 1 | 0 | 0 | 1 |  1 |  1   |  1   |         1           |
| 1 | 0 | 1 | 0 |  1 |  1   |  1   |         1           |
| 1 | 0 | 1 | 1 |  1 |  1   |  0   |         1           |
| 1 | 1 | 0 | 0 |  0 |  0   |  0   |         0           |
| 1 | 1 | 0 | 1 |  0 |  0   |  1   |         1           |
| 1 | 1 | 1 | 0 |  0 |  0   |  1   |         1           |
| 1 | 1 | 1 | 1 |  0 |  0   |  0   |         0           |

## Ejercicio 7
**Función lógica:**  
**F = ((A + B) · C) ⊕ D**

- Usa compuertas OR, AND y XOR.
- Requiere cuatro entradas.

[Respuesta 7](https://circuitverse.org/simulator/embed/ejercicio-7-9172f126-ff6c-4eb3-84fa-ad60d790ecc3)

## Tabla de Verdad

Función lógica: `F = ((A + B) · C) ⊕ D`

| A | B | C | D | A+B | (A+B)·C | F = ((A+B)·C) ⊕ D |
|---|---|---|---|-----|----------|---------------------|
| 0 | 0 | 0 | 0 |  0  |    0     |         0           |
| 0 | 0 | 0 | 1 |  0  |    0     |         1           |
| 0 | 0 | 1 | 0 |  0  |    0     |         0           |
| 0 | 0 | 1 | 1 |  0  |    0     |         1           |
| 0 | 1 | 0 | 0 |  1  |    0     |         0           |
| 0 | 1 | 0 | 1 |  1  |    0     |         1           |
| 0 | 1 | 1 | 0 |  1  |    1     |         1           |
| 0 | 1 | 1 | 1 |  1  |    1     |         0           |
| 1 | 0 | 0 | 0 |  1  |    0     |         0           |
| 1 | 0 | 0 | 1 |  1  |    0     |         1           |
| 1 | 0 | 1 | 0 |  1  |    1     |         1           |
| 1 | 0 | 1 | 1 |  1  |    1     |         0           |
| 1 | 1 | 0 | 0 |  1  |    0     |         0           |
| 1 | 1 | 0 | 1 |  1  |    0     |         1           |
| 1 | 1 | 1 | 0 |  1  |    1     |         1           |
| 1 | 1 | 1 | 1 |  1  |    1     |         0           |

## Ejercicio 8
**Función lógica:**  
**F = ((A · B) ⊙ (C + D))**

- Usa compuertas AND, OR y XNOR.
- Requiere cuatro entradas.

[Respuesta 8](https://circuitverse.org/simulator/embed/ejercicio-8-0367e9aa-0062-4d29-8b27-68efdb4dbadd)

## Tabla de Verdad

Función lógica: `F = ((A · B) ⊙ (C + D))`

| A | B | C | D | A·B | C+D | F = (A·B) ⊙ (C+D) |
|---|---|---|---|-----|-----|--------------------|
| 0 | 0 | 0 | 0 |  0  |  0  |         1          |
| 0 | 0 | 0 | 1 |  0  |  1  |         0          |
| 0 | 0 | 1 | 0 |  0  |  1  |         0          |
| 0 | 0 | 1 | 1 |  0  |  1  |         0          |
| 0 | 1 | 0 | 0 |  0  |  0  |         1          |
| 0 | 1 | 0 | 1 |  0  |  1  |         0          |
| 0 | 1 | 1 | 0 |  0  |  1  |         0          |
| 0 | 1 | 1 | 1 |  0  |  1  |         0          |
| 1 | 0 | 0 | 0 |  0  |  0  |         1          |
| 1 | 0 | 0 | 1 |  0  |  1  |         0          |
| 1 | 0 | 1 | 0 |  0  |  1  |         0          |
| 1 | 0 | 1 | 1 |  0  |  1  |         0          |
| 1 | 1 | 0 | 0 |  1  |  0  |         0          |
| 1 | 1 | 0 | 1 |  1  |  1  |         1          |
| 1 | 1 | 1 | 0 |  1  |  1  |         1          |
| 1 | 1 | 1 | 1 |  1  |  1  |         1          |

## Ejercicio 9
**Función lógica:**  
**F = ¬A · (B + ¬C)**

- Usa compuertas NOT, OR y AND.
- Requiere tres entradas.

[Respuesta 9](https://circuitverse.org/simulator/embed/ejercicio-9-7f39aca2-b402-48ff-acc2-a4b00938ed14)

## Tabla de Verdad

Función lógica: `F = ¬A · (B + ¬C)`

| A | B | C | ¬A | ¬C | B+¬C | F = ¬A · (B + ¬C) |
|---|---|---|----|----|------|--------------------|
| 0 | 0 | 0 |  1 |  1 |  1   |         1          |
| 0 | 0 | 1 |  1 |  0 |  0   |         0          |
| 0 | 1 | 0 |  1 |  1 |  1   |         1          |
| 0 | 1 | 1 |  1 |  0 |  1   |         1          |
| 1 | 0 | 0 |  0 |  1 |  1   |         0          |
| 1 | 0 | 1 |  0 |  0 |  0   |         0          |
| 1 | 1 | 0 |  0 |  1 |  1   |         0          |
| 1 | 1 | 1 |  0 |  0 |  1   |         0          |

## Ejercicio 10
**Función lógica:**  
**F = ((A ⊕ B) · ¬C) + D**

- Usa compuertas XOR, NOT, AND y OR.
- Cuatro entradas.

[Respuesta 10](https://circuitverse.org/simulator/embed/ejercicio-10-b6a0ef5a-6a27-40eb-bdc8-466abb9e952e)

## Tabla de Verdad

Función lógica: `F = ((A ⊕ B) · ¬C) + D`

| A | B | C | D | A⊕B | ¬C | (A⊕B)·¬C | F = ((A⊕B)·¬C) + D |
|---|---|---|---|-----|----|-----------|---------------------|
| 0 | 0 | 0 | 0 |  0  |  1 |     0     |         0           |
| 0 | 0 | 0 | 1 |  0  |  1 |     0     |         1           |
| 0 | 0 | 1 | 0 |  0  |  0 |     0     |         0           |
| 0 | 0 | 1 | 1 |  0  |  0 |     0     |         1           |
| 0 | 1 | 0 | 0 |  1  |  1 |     1     |         1           |
| 0 | 1 | 0 | 1 |  1  |  1 |     1     |         1           |
| 0 | 1 | 1 | 0 |  1  |  0 |     0     |         0           |
| 0 | 1 | 1 | 1 |  1  |  0 |     0     |         1           |
| 1 | 0 | 0 | 0 |  1  |  1 |     1     |         1           |
| 1 | 0 | 0 | 1 |  1  |  1 |     1     |         1           |
| 1 | 0 | 1 | 0 |  1  |  0 |     0     |         0           |
| 1 | 0 | 1 | 1 |  1  |  0 |     0     |         1           |
| 1 | 1 | 0 | 0 |  0  |  1 |     0     |         0           |
| 1 | 1 | 0 | 1 |  0  |  1 |     0     |         1           |
| 1 | 1 | 1 | 0 |  0  |  0 |     0     |         0           |
| 1 | 1 | 1 | 1 |  0  |  0 |     0     |         1           |
