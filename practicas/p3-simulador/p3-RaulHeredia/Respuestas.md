# Respuesta Uno

## Enlace al simulador:
[CircuitVerse - Respuesta Uno](https://circuitverse.org/users/309169/projects/respuesta-1-dd3309de-3e06-408f-ac7b-7429c8c41986)

---

## Expresión booleana:
**F = A · B + ¬C**

Esta es una función lógica combinacional compuesta por tres variables de entrada: **A**, **B**, y **C**, y una salida **F**.  
La expresión incluye una conjunción (AND), una disyunción (OR) y una negación (NOT).

---

## Tabla de verdad:

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

---

## Análisis paso a paso:

1. **¬C (NOT C):** Se invierte el valor de C.
2. **A · B (AND):** Solo es 1 si ambos A y B son 1.
3. **(A · B) + ¬C (OR):** La salida F será 1 si al menos una de las dos expresiones es 1.

---

## Conclusión:
La función F es verdadera (1) cuando:
- A y B son ambos 1, sin importar el valor de C.
- O cuando C es 0, sin importar los valores de A y B.

Esto se refleja tanto en la tabla como en la simulación enlazada arriba.





# Respuesta Dos

## Enlace al simulador:
[CircuitVerse - Respuesta Dos](https://circuitverse.org/users/309169/projects/respuesta-2)

---

## Expresión booleana:
**F = (A + B) · C**

Esta función lógica está compuesta por tres variables de entrada: **A**, **B**, y **C**, y una salida **F**.  
La expresión utiliza una disyunción (OR), una conjunción (AND), y paréntesis para establecer el orden de evaluación.

---

## Tabla de verdad:

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

---

## Análisis paso a paso:

1. **A + B (OR):** El resultado es 1 si al menos uno de los dos es 1.
2. **(A + B) · C (AND):** La salida F será 1 solo si la suma (A + B) es 1 **y** C también es 1.

---

## Conclusión:
La función F es verdadera (1) únicamente cuando:
- A o B (o ambos) son 1, **y**
- C también es 1.

Este comportamiento se confirma con la tabla de verdad y puede visualizarse en el simulador enlazado.





# Respuesta Tres

## Enlace al simulador:
[CircuitVerse - Respuesta Tres](https://circuitverse.org/users/309169/projects/respuesta-3-19d12be3-1f2d-4ca5-a1bb-9894e55ab8cb)

---

## Expresión booleana:
**F = ¬(A · B)**

Esta función lógica involucra dos variables de entrada: **A** y **B**, y una salida **F**.  
La expresión aplica una conjunción (AND) seguida de una negación (NOT), lo que representa una compuerta **NAND**.

---

## Tabla de verdad:

| A | B | A · B | F = ¬(A · B) |
|---|---|--------|--------------|
| 0 | 0 |   0    |      1       |
| 0 | 1 |   0    |      1       |
| 1 | 0 |   0    |      1       |
| 1 | 1 |   1    |      0       |

---

## Análisis paso a paso:

1. **A · B (AND):** Solo es 1 si **ambos** A y B son 1.
2. **¬(A · B) (NOT):** La salida F será 1 cuando A · B sea 0, y 0 cuando A · B sea 1.

---

## Conclusión:
Esta expresión es una operación **NAND**, la cual es **falsa (0)** **solo** cuando ambas entradas A y B son 1.  
En todos los demás casos, la salida es verdadera (1). Esto se verifica en la tabla de verdad y el simulador.





# Respuesta Cuatro

## Enlace al simulador:
[CircuitVerse - Respuesta Cuatro](https://circuitverse.org/users/309169/projects/respuesta-4-49d3f55f-2870-45f5-938c-c02f77ce9c2c)

---

## Expresión booleana:
**F = (A ⊕ B) + (¬C · D)**

Esta función lógica combinacional incluye cuatro variables de entrada: **A**, **B**, **C**, **D**, y una salida **F**.  
Se compone de una operación XOR, una negación, una conjunción y una disyunción.

---

## Tabla de verdad:

| A | B | C | D | A ⊕ B | ¬C | ¬C · D | F = (A ⊕ B) + (¬C · D) |
|---|---|---|---|--------|----|--------|-------------------------|
| 0 | 0 | 0 | 0 |   0    | 1  |   0    |           0             |
| 0 | 0 | 0 | 1 |   0    | 1  |   1    |           1             |
| 0 | 0 | 1 | 0 |   0    | 0  |   0    |           0             |
| 0 | 0 | 1 | 1 |   0    | 0  |   0    |           0             |
| 0 | 1 | 0 | 0 |   1    | 1  |   0    |           1             |
| 0 | 1 | 0 | 1 |   1    | 1  |   1    |           1             |
| 0 | 1 | 1 | 0 |   1    | 0  |   0    |           1             |
| 0 | 1 | 1 | 1 |   1    | 0  |   0    |           1             |
| 1 | 0 | 0 | 0 |   1    | 1  |   0    |           1             |
| 1 | 0 | 0 | 1 |   1    | 1  |   1    |           1             |
| 1 | 0 | 1 | 0 |   1    | 0  |   0    |           1             |
| 1 | 0 | 1 | 1 |   1    | 0  |   0    |           1             |
| 1 | 1 | 0 | 0 |   0    | 1  |   0    |           0             |
| 1 | 1 | 0 | 1 |   0    | 1  |   1    |           1             |
| 1 | 1 | 1 | 0 |   0    | 0  |   0    |           0             |
| 1 | 1 | 1 | 1 |   0    | 0  |   0    |           0             |

---

## Análisis paso a paso:

1. **A ⊕ B (XOR):** Devuelve 1 si A y B son diferentes.
2. **¬C (NOT C):** Invierte el valor de C.
3. **¬C · D (AND):** Es 1 solo si ¬C es 1 y D también es 1.
4. **(A ⊕ B) + (¬C · D) (OR):** La salida F es 1 si al menos una de las dos expresiones anteriores es 1.

---

## Conclusión:
La salida F es 1 en los siguientes casos:
- Cuando A y B son diferentes (XOR = 1).
- O cuando C es 0 **y** D es 1 (¬C · D = 1).

Esto se puede comprobar con la tabla de verdad y en el simulador enlazado.





# Respuesta Cinco

## Enlace al simulador:
[CircuitVerse - Respuesta Cinco](https://circuitverse.org/users/309169/projects/respuesta-5)

---

## Expresión booleana:
**F = ¬(A + B + C)**

Esta función lógica se basa en una disyunción (OR) de tres variables de entrada (**A**, **B**, y **C**) seguida de una negación (NOT).  
En otras palabras, es una **NOR** de tres entradas.

---

## Tabla de verdad:

| A | B | C | A + B + C | F = ¬(A + B + C) |
|---|---|---|------------|------------------|
| 0 | 0 | 0 |     0      |        1         |
| 0 | 0 | 1 |     1      |        0         |
| 0 | 1 | 0 |     1      |        0         |
| 0 | 1 | 1 |     1      |        0         |
| 1 | 0 | 0 |     1      |        0         |
| 1 | 0 | 1 |     1      |        0         |
| 1 | 1 | 0 |     1      |        0         |
| 1 | 1 | 1 |     1      |        0         |

---

## Análisis paso a paso:

1. **A + B + C (OR):** La operación devuelve 1 si **al menos una** de las variables es 1.
2. **¬(A + B + C):** La negación hace que la salida F sea 1 **solo** si todas las variables son 0.

---

## Conclusión:
Esta expresión implementa una compuerta **NOR** de tres entradas.  
La salida **F será 1 únicamente cuando A, B y C sean 0 al mismo tiempo**.  
En todos los demás casos, la salida es 0. Esto se puede verificar en la tabla de verdad y en el simulador enlazado.





# Respuesta Seis

## Enlace al simulador:
[CircuitVerse - Respuesta Seis](https://circuitverse.org/users/309169/projects/respuesta-6)

---

## Expresión booleana:
**F = (A · ¬B) + (C ⊕ D)**

Esta función lógica utiliza cuatro variables de entrada: **A**, **B**, **C**, **D**, y una salida **F**.  
Incluye operaciones AND, NOT, XOR y OR.

---

## Tabla de verdad:

| A | B | C | D | ¬B | A · ¬B | C ⊕ D | F = (A · ¬B) + (C ⊕ D) |
|---|---|---|---|----|--------|--------|-------------------------|
| 0 | 0 | 0 | 0 |  1 |   0    |   0    |           0             |
| 0 | 0 | 0 | 1 |  1 |   0    |   1    |           1             |
| 0 | 0 | 1 | 0 |  1 |   0    |   1    |           1             |
| 0 | 0 | 1 | 1 |  1 |   0    |   0    |           0             |
| 0 | 1 | 0 | 0 |  0 |   0    |   0    |           0             |
| 0 | 1 | 0 | 1 |  0 |   0    |   1    |           1             |
| 0 | 1 | 1 | 0 |  0 |   0    |   1    |           1             |
| 0 | 1 | 1 | 1 |  0 |   0    |   0    |           0             |
| 1 | 0 | 0 | 0 |  1 |   1    |   0    |           1             |
| 1 | 0 | 0 | 1 |  1 |   1    |   1    |           1             |
| 1 | 0 | 1 | 0 |  1 |   1    |   1    |           1             |
| 1 | 0 | 1 | 1 |  1 |   1    |   0    |           1             |
| 1 | 1 | 0 | 0 |  0 |   0    |   0    |           0             |
| 1 | 1 | 0 | 1 |  0 |   0    |   1    |           1             |
| 1 | 1 | 1 | 0 |  0 |   0    |   1    |           1             |
| 1 | 1 | 1 | 1 |  0 |   0    |   0    |           0             |

---

## Análisis paso a paso:

1. **¬B (NOT B):** Invierte el valor de B.
2. **A · ¬B (AND):** Es 1 solo cuando A es 1 y B es 0.
3. **C ⊕ D (XOR):** Es 1 si C y D son diferentes.
4. **(A · ¬B) + (C ⊕ D) (OR):** La salida F es 1 si al menos una de las dos expresiones es 1.

---

## Conclusión:
La función devuelve 1 en varios casos:
- Si **A es 1 y B es 0**, o
- Si **C y D son diferentes**.

Este comportamiento se confirma tanto en la tabla de verdad como en el simulador enlazado.





# Respuesta Siete

## Enlace al simulador:
[CircuitVerse - Respuesta Siete](https://circuitverse.org/users/309169/projects/respuesta-7)

---

## Expresión booleana:
**F = ((A + B) · C) ⊕ D**

Esta expresión involucra cuatro variables de entrada: **A**, **B**, **C**, **D**, y una salida **F**.  
Combina operaciones OR, AND y XOR, lo que la hace una función compuesta.

---

## Tabla de verdad:

| A | B | C | D | A + B | (A + B) · C | ((A + B) · C) ⊕ D | F |
|---|---|---|---|--------|--------------|---------------------|---|
| 0 | 0 | 0 | 0 |   0    |      0       |         0           | 0 |
| 0 | 0 | 0 | 1 |   0    |      0       |         1           | 1 |
| 0 | 0 | 1 | 0 |   0    |      0       |         0           | 0 |
| 0 | 0 | 1 | 1 |   0    |      0       |         1           | 1 |
| 0 | 1 | 0 | 0 |   1    |      0       |         0           | 0 |
| 0 | 1 | 0 | 1 |   1    |      0       |         1           | 1 |
| 0 | 1 | 1 | 0 |   1    |      1       |         1           | 1 |
| 0 | 1 | 1 | 1 |   1    |      1       |         0           | 0 |
| 1 | 0 | 0 | 0 |   1    |      0       |         0           | 0 |
| 1 | 0 | 0 | 1 |   1    |      0       |         1           | 1 |
| 1 | 0 | 1 | 0 |   1    |      1       |         1           | 1 |
| 1 | 0 | 1 | 1 |   1    |      1       |         0           | 0 |
| 1 | 1 | 0 | 0 |   1    |      0       |         0           | 0 |
| 1 | 1 | 0 | 1 |   1    |      0       |         1           | 1 |
| 1 | 1 | 1 | 0 |   1    |      1       |         1           | 1 |
| 1 | 1 | 1 | 1 |   1    |      1       |         0           | 0 |

---

## Análisis paso a paso:

1. **A + B (OR):** Devuelve 1 si A o B es 1.
2. **(A + B) · C (AND):** Devuelve 1 solo si A + B es 1 **y** C también es 1.
3. **((A + B) · C) ⊕ D (XOR):** Devuelve 1 si el resultado anterior es **diferente** de D.

---

## Conclusión:
La salida **F** será 1 cuando la expresión **((A + B) · C)** sea diferente del valor de **D**.  
Esta operación compuesta combina condiciones que dependen de múltiples entradas, y se puede comprobar paso a paso en la tabla de verdad y el simulador enlazado.





# Respuesta Ocho

## Enlace al simulador:
[CircuitVerse - Respuesta Ocho](https://circuitverse.org/users/309169/projects/respuesta-8-1948e5f0-d362-4341-a50f-df41b3d2f8b8)

---

## Expresión booleana:
**F = ((A · B) ⊙ (C + D))**

Esta expresión usa las siguientes operaciones lógicas:
- `·` (AND)
- `+` (OR)
- `⊙` (XNOR), también conocida como **equivalencia lógica**

---

## Tabla de verdad:

| A | B | C | D | A · B | C + D | F = (A · B) ⊙ (C + D) |
|---|---|---|---|-------|--------|------------------------|
| 0 | 0 | 0 | 0 |   0   |   0    |           1            |
| 0 | 0 | 0 | 1 |   0   |   1    |           0            |
| 0 | 0 | 1 | 0 |   0   |   1    |           0            |
| 0 | 0 | 1 | 1 |   0   |   1    |           0            |
| 0 | 1 | 0 | 0 |   0   |   0    |           1            |
| 0 | 1 | 0 | 1 |   0   |   1    |           0            |
| 0 | 1 | 1 | 0 |   0   |   1    |           0            |
| 0 | 1 | 1 | 1 |   0   |   1    |           0            |
| 1 | 0 | 0 | 0 |   0   |   0    |           1            |
| 1 | 0 | 0 | 1 |   0   |   1    |           0            |
| 1 | 0 | 1 | 0 |   0   |   1    |           0            |
| 1 | 0 | 1 | 1 |   0   |   1    |           0            |
| 1 | 1 | 0 | 0 |   1   |   0    |           0            |
| 1 | 1 | 0 | 1 |   1   |   1    |           1            |
| 1 | 1 | 1 | 0 |   1   |   1    |           1            |
| 1 | 1 | 1 | 1 |   1   |   1    |           1            |

---

## Análisis paso a paso:

1. **A · B (AND):** Es 1 solo si A y B son ambos 1.
2. **C + D (OR):** Es 1 si al menos uno de C o D es 1.
3. **XNOR (⊙):** Compara los dos resultados anteriores; da 1 si **ambos son iguales**, y 0 si **son diferentes**.

---

## Conclusión:
La salida **F** será 1 solamente cuando el valor de **(A · B)** sea **igual** al de **(C + D)**.  
Esta función implementa una **comparación lógica entre una conjunción y una disyunción**, usando la operación **XNOR**. Puedes verificar su comportamiento en el simulador enlazado.





# Respuesta Nueve

## Enlace al simulador:
[CircuitVerse - Respuesta Nueve](https://circuitverse.org/users/309169/projects/respuesta-9)

---

## Expresión booleana:
**F = ¬A · (B + ¬C)**

Esta expresión combina las operaciones:
- **¬** (NOT)
- **+** (OR)
- **·** (AND)

Con tres variables de entrada: **A**, **B**, **C** y una salida **F**.

---

## Tabla de verdad:

| A | B | C | ¬A | ¬C | B + ¬C | F = ¬A · (B + ¬C) |
|---|---|---|----|----|--------|--------------------|
| 0 | 0 | 0 |  1 |  1 |   1    |         1          |
| 0 | 0 | 1 |  1 |  0 |   0    |         0          |
| 0 | 1 | 0 |  1 |  1 |   1    |         1          |
| 0 | 1 | 1 |  1 |  0 |   1    |         1          |
| 1 | 0 | 0 |  0 |  1 |   1    |         0          |
| 1 | 0 | 1 |  0 |  0 |   0    |         0          |
| 1 | 1 | 0 |  0 |  1 |   1    |         0          |
| 1 | 1 | 1 |  0 |  0 |   1    |         0          |

---

## Análisis paso a paso:

1. **¬A:** Devuelve 1 si A es 0.
2. **¬C:** Devuelve 1 si C es 0.
3. **B + ¬C (OR):** Da 1 si B o ¬C es 1.
4. **¬A · (B + ¬C):** La salida F es 1 **solo si A es 0** **y** **(B + ¬C) es 1**.

---

## Conclusión:
La función **F** devuelve 1 en los casos en los que **A es 0** y al menos una de las condiciones **B = 1** o **C = 0** se cumple.  
Es una expresión que filtra ciertos casos específicos y se puede verificar completamente en el simulador enlazado.





# Respuesta Diez

## Enlace al simulador:
[CircuitVerse - Respuesta Diez](https://circuitverse.org/users/309169/projects/respuesta-10)

---

## Expresión booleana:
**F = ((A ⊕ B) · ¬C) + D**

Esta función utiliza las siguientes operaciones:
- **⊕** (XOR)
- **¬** (NOT)
- **·** (AND)
- **+** (OR)

Con cuatro variables: **A**, **B**, **C**, **D**.

---

## Tabla de verdad:

| A | B | C | D | A ⊕ B | ¬C | (A ⊕ B) · ¬C | F = ((A ⊕ B) · ¬C) + D |
|---|---|---|---|--------|----|---------------|--------------------------|
| 0 | 0 | 0 | 0 |   0    | 1  |      0        |            0             |
| 0 | 0 | 0 | 1 |   0    | 1  |      0        |            1             |
| 0 | 0 | 1 | 0 |   0    | 0  |      0        |            0             |
| 0 | 0 | 1 | 1 |   0    | 0  |      0        |            1             |
| 0 | 1 | 0 | 0 |   1    | 1  |      1        |            1             |
| 0 | 1 | 0 | 1 |   1    | 1  |      1        |            1             |
| 0 | 1 | 1 | 0 |   1    | 0  |      0        |            0             |
| 0 | 1 | 1 | 1 |   1    | 0  |      0        |            1             |
| 1 | 0 | 0 | 0 |   1    | 1  |      1        |            1             |
| 1 | 0 | 0 | 1 |   1    | 1  |      1        |            1             |
| 1 | 0 | 1 | 0 |   1    | 0  |      0        |            0             |
| 1 | 0 | 1 | 1 |   1    | 0  |      0        |            1             |
| 1 | 1 | 0 | 0 |   0    | 1  |      0        |            0             |
| 1 | 1 | 0 | 1 |   0    | 1  |      0        |            1             |
| 1 | 1 | 1 | 0 |   0    | 0  |      0        |            0             |
| 1 | 1 | 1 | 1 |   0    | 0  |      0        |            1             |

---

## Análisis paso a paso:

1. **A ⊕ B (XOR):** Devuelve 1 si A y B son diferentes.
2. **¬C:** Es 1 si C es 0.
3. **(A ⊕ B) · ¬C:** Devuelve 1 si A y B son distintos **y** C es 0.
4. **F = ((A ⊕ B) · ¬C) + D:** F será 1 si el resultado anterior es 1 **o** si D es 1.

---

## Conclusión:
La función **F** es verdadera cuando:
- A y B son diferentes **y** C es 0,  
- **o** cuando D es 1.  

Esta es una función lógica compuesta que responde a múltiples combinaciones y puede ser explorada completamente en el simulador enlazado.
