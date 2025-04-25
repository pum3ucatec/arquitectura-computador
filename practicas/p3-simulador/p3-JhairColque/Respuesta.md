
# Práctica 3 - Funciones Lógicas con Compuertas

**Nombre:** Jhair Colque  
**Rama:** JhairColque/practica3

---

## Ejercicio 1

**Enlace al simulador:** [CircuitVerse - Ejercicio 1](https://circuitverse.org/users/309346/projects/respuesta-1-cc6a0341-5454-4f66-a091-f484886f5718)

### Expresión booleana:

```
F = A · B + ¬C
```

Esta es una función lógica combinacional compuesta por tres variables de entrada: A, B, C y una salida F.  
La expresión incluye una conjunción (AND), una disyunción (OR) y una negación (NOT).

### Tabla de verdad:

| A | B | C | ¬C | A · B | F = (A · B) + ¬C |
|---|---|---|----|-------|------------------|
| 0 | 0 | 0 |  1 |   0   |        1         |
| 0 | 0 | 1 |  0 |   0   |        0         |
| 0 | 1 | 0 |  1 |   0   |        1         |
| 0 | 1 | 1 |  0 |   0   |        0         |
| 1 | 0 | 0 |  1 |   0   |        1         |
| 1 | 0 | 1 |  0 |   0   |        0         |
| 1 | 1 | 0 |  1 |   1   |        1         |
| 1 | 1 | 1 |  0 |   1   |        1         |

### Análisis paso a paso:

1. `¬C (NOT C)`: Se invierte el valor de C.  
2. `A · B (AND)`: Solo es 1 si ambos A y B son 1.  
3. `(A · B) + ¬C (OR)`: La salida F será 1 si al menos una de las dos expresiones es 1.

---

## Ejercicio 2

**Enlace al simulador:** [CircuitVerse - Ejercicio 2](https://circuitverse.org/users/309346/projects/respuesta-2-85640182-6c89-4bc6-96ee-36ae69a614372)

### Expresión booleana:

F = (A + B) · C


Esta función lógica combinacional utiliza tres variables de entrada: A, B y C.  
La operación combina una disyunción (OR) entre A y B, seguida de una conjunción (AND) con C.

### Tabla de verdad:

| A | B | C | A + B | F = (A + B) · C |
|---|---|---|--------|------------------|
| 0 | 0 | 0 |   0    |        0         |
| 0 | 0 | 1 |   0    |        0         |
| 0 | 1 | 0 |   1    |        0         |
| 0 | 1 | 1 |   1    |        1         |
| 1 | 0 | 0 |   1    |        0         |
| 1 | 0 | 1 |   1    |        1         |
| 1 | 1 | 0 |   1    |        0         |
| 1 | 1 | 1 |   1    |        1         |

### Análisis paso a paso:

1. `A + B (OR)`: Devuelve 1 si al menos una de las entradas A o B es 1.  
2. `(A + B) · C (AND)`: La salida F será 1 solo si la salida del OR es 1 **y** C también es 1.

---

## Ejercicio 3

**Enlace al simulador:** [CircuitVerse - Ejercicio 3](https://circuitverse.org/users/309346/projects/respuesta)

### Expresión booleana:

F = ¬(A · B)


Esta función lógica utiliza dos variables de entrada: A y B.  
Aplica una conjunción (AND) seguida de una negación (NOT), representando una operación NAND.

### Tabla de verdad:

| A | B | A · B | F = ¬(A · B) |
|---|---|------|--------------|
| 0 | 0 |  0   |      1       |
| 0 | 1 |  0   |      1       |
| 1 | 0 |  0   |      1       |
| 1 | 1 |  1   |      0       |

### Análisis paso a paso:

1. `A · B (AND)`: La operación AND resulta 1 solo si A y B son ambos 1.  
2. `¬(A · B) (NOT)`: La negación convierte el resultado: será 1 si A · B fue 0, y será 0 si A · B fue 1.

---

## Ejercicio 4

**Enlace al simulador:** [CircuitVerse - Ejercicio 4](https://circuitverse.org/users/309346/projects/respuesta-4-27db6fe3-3783-4c21-b5d9-c33a2b9a4eb2)

### Expresión booleana:

F = (A ⊕ B) + (¬C · D)


Esta función lógica utiliza cuatro variables de entrada: A, B, C y D.  
Combina una operación XOR, una negación (NOT), una conjunción (AND) y una disyunción (OR).

### Tabla de verdad:

| A | B | C | D | A ⊕ B | ¬C | ¬C · D | F = (A ⊕ B) + (¬C · D) |
|---|---|---|---|--------|----|--------|------------------------|
| 0 | 0 | 0 | 0 |   0    |  1 |   0    |           0            |
| 0 | 0 | 0 | 1 |   0    |  1 |   1    |           1            |
| 0 | 0 | 1 | 0 |   0    |  0 |   0    |           0            |
| 0 | 0 | 1 | 1 |   0    |  0 |   0    |           0            |
| 0 | 1 | 0 | 0 |   1    |  1 |   0    |           1            |
| 0 | 1 | 0 | 1 |   1    |  1 |   1    |           1            |
| 0 | 1 | 1 | 0 |   1    |  0 |   0    |           1            |
| 0 | 1 | 1 | 1 |   1    |  0 |   0    |           1            |
| 1 | 0 | 0 | 0 |   1    |  1 |   0    |           1            |
| 1 | 0 | 0 | 1 |   1    |  1 |   1    |           1            |
| 1 | 0 | 1 | 0 |   1    |  0 |   0    |           1            |
| 1 | 0 | 1 | 1 |   1    |  0 |   0    |           1            |
| 1 | 1 | 0 | 0 |   0    |  1 |   0    |           0            |
| 1 | 1 | 0 | 1 |   0    |  1 |   1    |           1            |
| 1 | 1 | 1 | 0 |   0    |  0 |   0    |           0            |
| 1 | 1 | 1 | 1 |   0    |  0 |   0    |           0            |

### Análisis paso a paso:

1. `A ⊕ B (XOR)`: Da 1 si A y B son diferentes.  
2. `¬C (NOT)`: Invierte el valor de C.  
3. `¬C · D (AND)`: Da 1 solo si C es 0 y D es 1.  
4. `(A ⊕ B) + (¬C · D) (OR)`: La salida F será 1 si cualquiera de las dos condiciones es verdadera.

---

## Ejercicio 5

**Enlace al simulador:** [CircuitVerse - Ejercicio 5](https://circuitverse.org/users/309346/projects/respuesta-5-7f1f3b7e-cb4b-4852-a1dc-7f1494b117ec)

### Expresión booleana:

F = ¬(A + B + C)


Esta función lógica combinacional utiliza tres variables de entrada: A, B y C.  
Realiza una disyunción (OR) entre las tres variables, seguida de una negación (NOT), funcionando como una compuerta NOR de tres entradas.

### Tabla de verdad:

| A | B | C | A + B + C | F = ¬(A + B + C) |
|---|---|---|-----------|-----------------|
| 0 | 0 | 0 |     0     |        1        |
| 0 | 0 | 1 |     1     |        0        |
| 0 | 1 | 0 |     1     |        0        |
| 0 | 1 | 1 |     1     |        0        |
| 1 | 0 | 0 |     1     |        0        |
| 1 | 0 | 1 |     1     |        0        |
| 1 | 1 | 0 |     1     |        0        |
| 1 | 1 | 1 |     1     |        0        |

### Análisis paso a paso:

1. `A + B + C (OR)`: Da 1 si al menos una de las entradas A, B o C es 1.  
2. `¬(A + B + C) (NOT)`: La negación convierte la salida: será 1 solo si todas las entradas son 0.

---

## Ejercicio 6

**Enlace al simulador:** [CircuitVerse - Ejercicio 6](https://circuitverse.org/users/309346/projects/respuesta-6-a08b3ed1-be0a-4a3b-bdc7-411f45a7c9d1)

### Expresión booleana:

F = (A · ¬B) + (C ⊕ D)


Esta función lógica combinacional involucra cuatro variables de entrada: A, B, C y D.  
Utiliza una conjunción (AND), una negación (NOT), una disyunción exclusiva (XOR) y una disyunción (OR).

### Tabla de verdad:

| A | B | C | D | ¬B | A · ¬B | C ⊕ D | F = (A · ¬B) + (C ⊕ D) |
|---|---|---|---|----|--------|-------|------------------------|
| 0 | 0 | 0 | 0 |  1 |   0    |   0   |           0            |
| 0 | 0 | 0 | 1 |  1 |   0    |   1   |           1            |
| 0 | 0 | 1 | 0 |  1 |   0    |   1   |           1            |
| 0 | 0 | 1 | 1 |  1 |   0    |   0   |           0            |
| 0 | 1 | 0 | 0 |  0 |   0    |   0   |           0            |
| 0 | 1 | 0 | 1 |  0 |   0    |   1   |           1            |
| 0 | 1 | 1 | 0 |  0 |   0    |   1   |           1            |
| 0 | 1 | 1 | 1 |  0 |   0    |   0   |           0            |
| 1 | 0 | 0 | 0 |  1 |   1    |   0   |           1            |
| 1 | 0 | 0 | 1 |  1 |   1    |   1   |           1            |
| 1 | 0 | 1 | 0 |  1 |   1    |   1   |           1            |
| 1 | 0 | 1 | 1 |  1 |   1    |   0   |           1            |
| 1 | 1 | 0 | 0 |  0 |   0    |   0   |           0            |
| 1 | 1 | 0 | 1 |  0 |   0    |   1   |           1            |
| 1 | 1 | 1 | 0 |  0 |   0    |   1   |           1            |
| 1 | 1 | 1 | 1 |  0 |   0    |   0   |           0            |

### Análisis paso a paso:

1. `¬B (NOT B)`: Invierte el valor de B.  
2. `A · ¬B (AND)`: Da 1 solo si A es 1 y B es 0.  
3. `C ⊕ D (XOR)`: Da 1 si C y D son diferentes.  
4. `(A · ¬B) + (C ⊕ D) (OR)`: La salida F será 1 si al menos una de las dos condiciones es 1.

---

## Ejercicio 7

**Enlace al simulador:** [CircuitVerse - Ejercicio 7](https://circuitverse.org/users/309346/projects/respuesta-7-df95433b-9cb7-4408-b887-13747be1fbd9)

### Expresión booleana:

F = ((A + B) · C) ⊕ D


Esta función lógica combinacional involucra cuatro variables de entrada: A, B, C y D.  
Realiza primero una disyunción (OR) entre A y B, luego una conjunción (AND) con C, y finalmente una disyunción exclusiva (XOR) con D.

### Tabla de verdad:

| A | B | C | D | A + B | (A + B) · C | F = ((A + B) · C) ⊕ D |
|---|---|---|---|-------|--------------|-----------------------|
| 0 | 0 | 0 | 0 |   0   |      0       |          0            |
| 0 | 0 | 0 | 1 |   0   |      0       |          1            |
| 0 | 0 | 1 | 0 |   0   |      0       |          0            |
| 0 | 0 | 1 | 1 |   0   |      0       |          1            |
| 0 | 1 | 0 | 0 |   1   |      0       |          0            |
| 0 | 1 | 0 | 1 |   1   |      0       |          1            |
| 0 | 1 | 1 | 0 |   1   |      1       |          1            |
| 0 | 1 | 1 | 1 |   1   |      1       |          0            |
| 1 | 0 | 0 | 0 |   1   |      0       |          0            |
| 1 | 0 | 0 | 1 |   1   |      0       |          1            |
| 1 | 0 | 1 | 0 |   1   |      1       |          1            |
| 1 | 0 | 1 | 1 |   1   |      1       |          0            |
| 1 | 1 | 0 | 0 |   1   |      0       |          0            |
| 1 | 1 | 0 | 1 |   1   |      0       |          1            |
| 1 | 1 | 1 | 0 |   1   |      1       |          1            |
| 1 | 1 | 1 | 1 |   1   |      1       |          0            |

### Análisis paso a paso:

1. `A + B (OR)`: Da 1 si A o B son 1.  
2. `(A + B) · C (AND)`: Da 1 solo si el resultado del OR es 1 **y** C también es 1.  
3. `((A + B) · C) ⊕ D (XOR)`: La salida será 1 si el resultado anterior y D son diferentes.

---

## Ejercicio 8

**Enlace al simulador:** [CircuitVerse - Ejercicio 8](https://circuitverse.org/users/309346/projects/respuesta-8-81c95ecb-b630-4690-bdea-2279dc0ae564)

### Expresión booleana:

F = (A · B) ⊙ (C + D)

Esta función lógica combinacional involucra cuatro variables de entrada: A, B, C y D.  
Realiza una conjunción (AND) entre A y B, una disyunción (OR) entre C y D, y finalmente una equivalencia lógica (XNOR) entre los resultados.

### Tabla de verdad:

| A | B | C | D | A · B | C + D | F = (A · B) ⊙ (C + D) |
|---|---|---|---|-------|--------|----------------------|
| 0 | 0 | 0 | 0 |   0   |   0    |          1           |
| 0 | 0 | 0 | 1 |   0   |   1    |          0           |
| 0 | 0 | 1 | 0 |   0   |   1    |          0           |
| 0 | 0 | 1 | 1 |   0   |   1    |          0           |
| 0 | 1 | 0 | 0 |   0   |   0    |          1           |
| 0 | 1 | 0 | 1 |   0   |   1    |          0           |
| 0 | 1 | 1 | 0 |   0   |   1    |          0           |
| 0 | 1 | 1 | 1 |   0   |   1    |          0           |
| 1 | 0 | 0 | 0 |   0   |   0    |          1           |
| 1 | 0 | 0 | 1 |   0   |   1    |          0           |
| 1 | 0 | 1 | 0 |   0   |   1    |          0           |
| 1 | 0 | 1 | 1 |   0   |   1    |          0           |
| 1 | 1 | 0 | 0 |   1   |   0    |          0           |
| 1 | 1 | 0 | 1 |   1   |   1    |          1           |
| 1 | 1 | 1 | 0 |   1   |   1    |          1           |
| 1 | 1 | 1 | 1 |   1   |   1    |          1           |

### Análisis paso a paso:

1. `A · B (AND)`: Da 1 solo si A y B son ambos 1.  
2. `C + D (OR)`: Da 1 si al menos uno entre C o D es 1.  
3. `(A · B) ⊙ (C + D) (XNOR)`: La salida será 1 si ambos resultados son iguales, y 0 si son diferentes.

---

## Ejercicio 9

**Enlace al simulador:** [CircuitVerse - Ejercicio 9](https://circuitverse.org/users/309346/projects/respuesta-9-894debab-403b-49a9-b2a3-adda270f1753)

### Expresión booleana:

F = ¬A · (B + ¬C)


Esta función lógica combinacional utiliza tres variables de entrada: A, B y C.  
Aplica una negación (NOT) a A, una negación (NOT) a C, una disyunción (OR) entre B y ¬C, y finalmente una conjunción (AND) entre ¬A y el resultado del OR.

### Tabla de verdad:

| A | B | C | ¬A | ¬C | B + ¬C | F = ¬A · (B + ¬C) |
|---|---|---|----|----|--------|------------------|
| 0 | 0 | 0 |  1 |  1 |   1    |        1         |
| 0 | 0 | 1 |  1 |  0 |   0    |        0         |
| 0 | 1 | 0 |  1 |  1 |   1    |        1         |
| 0 | 1 | 1 |  1 |  0 |   1    |        1         |
| 1 | 0 | 0 |  0 |  1 |   1    |        0         |
| 1 | 0 | 1 |  0 |  0 |   0    |        0         |
| 1 | 1 | 0 |  0 |  1 |   1    |        0         |
| 1 | 1 | 1 |  0 |  0 |   1    |        0         |

### Análisis paso a paso:

1. `¬A (NOT)`: Invierte el valor de A.  
2. `¬C (NOT)`: Invierte el valor de C.  
3. `B + ¬C (OR)`: Da 1 si B es 1 o ¬C es 1.  
4. `¬A · (B + ¬C) (AND)`: Da 1 solo si ¬A es 1 **y** (B + ¬C) es 1.

---

## Ejercicio 10

**Enlace al simulador:** [CircuitVerse - Ejercicio 10](https://circuitverse.org/users/309346/projects/respuesta-10-c0d8b2dc-526c-4473-9de5-056ca02f8172)

### Expresión booleana:

F = ((A ⊕ B) · ¬C) + D


Esta función lógica combinacional utiliza cuatro variables de entrada: A, B, C y D.  
Primero realiza una disyunción exclusiva (XOR) entre A y B, después una conjunción (AND) con la negación de C, y finalmente una disyunción (OR) con D.

### Tabla de verdad:

| A | B | C | D | A ⊕ B | ¬C | (A ⊕ B) · ¬C | F = ((A ⊕ B) · ¬C) + D |
|---|---|---|---|--------|----|--------------|------------------------|
| 0 | 0 | 0 | 0 |   0    |  1 |      0       |           0            |
| 0 | 0 | 0 | 1 |   0    |  1 |      0       |           1            |
| 0 | 0 | 1 | 0 |   0    |  0 |      0       |           0            |
| 0 | 0 | 1 | 1 |   0    |  0 |      0       |           1            |
| 0 | 1 | 0 | 0 |   1    |  1 |      1       |           1            |
| 0 | 1 | 0 | 1 |   1    |  1 |      1       |           1            |
| 0 | 1 | 1 | 0 |   1    |  0 |      0       |           0            |
| 0 | 1 | 1 | 1 |   1    |  0 |      0       |           1            |
| 1 | 0 | 0 | 0 |   1    |  1 |      1       |           1            |
| 1 | 0 | 0 | 1 |   1    |  1 |      1       |           1            |
| 1 | 0 | 1 | 0 |   1    |  0 |      0       |           0            |
| 1 | 0 | 1 | 1 |   1    |  0 |      0       |           1            |
| 1 | 1 | 0 | 0 |   0    |  1 |      0       |           0            |
| 1 | 1 | 0 | 1 |   0    |  1 |      0       |           1            |
| 1 | 1 | 1 | 0 |   0    |  0 |      0       |           0            |
| 1 | 1 | 1 | 1 |   0    |  0 |      0       |           1            |

### Análisis paso a paso:

1. `A ⊕ B (XOR)`: Da 1 si A y B son diferentes.  
2. `¬C (NOT)`: Invierte el valor de C.  
3. `(A ⊕ B) · ¬C (AND)`: Da 1 si A ⊕ B es 1 **y** ¬C es 1.  
4. `((A ⊕ B) · ¬C) + D (OR)`: La salida será 1 si (A ⊕ B) · ¬C es 1 **o** si D es 1.

---