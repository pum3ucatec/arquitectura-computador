1. **Función:** F = A · B + ¬C
Enlace del simulador 
[respuesta 1](https://circuitverse.org/users/308924/projects/resp1)

# Tabla de Verdad para la Función Lógica
| A | B | C | ¬C | A · B | F = (A · B) + ¬C |
|---|---|---|----|-------|-------------------|
| 0 | 0 | 0 | 1  | 0     | 1                 |
| 0 | 0 | 1 | 0  | 0     | 0                 |
| 0 | 1 | 0 | 1  | 0     | 1                 |
| 0 | 1 | 1 | 0  | 0     | 0                 |
| 1 | 0 | 0 | 1  | 0     | 1                 |
| 1 | 0 | 1 | 0  | 0     | 0                 |
| 1 | 1 | 0 | 1  | 1     | 1                 |
| 1 | 1 | 1 | 0  | 1     | 1                 |

**Explicación de las columnas:**

* **A, B, C:** Son las tres entradas de la función lógica.
* **¬C:** Es la negación de la entrada C (compuerta NOT). Si C es 0, ¬C es 1, y viceversa.
* **A · B:** Es la operación AND entre las entradas A y B (compuerta AND). El resultado es 1 solo si tanto A como B son 1.
* **F = (A · B) + ¬C:** Es la operación OR entre el resultado de (A · B) y ¬C (compuerta OR). El resultado final F es 1 si (A · B) es 1 o si ¬C es 1 (o ambos).

2. **Función:** F = (A + B) · C
Enlace del simulador 
[respuesta 2](https://circuitverse.org/users/308924/projects/resp2)

# Tabla de Verdad para la Función Lógica
| A | B | C | A + B | F = (A + B) · C |
|---|---|---|-------|-----------------|
| 0 | 0 | 0 | 0     | 0               |
| 0 | 0 | 1 | 0     | 0               |
| 0 | 1 | 0 | 1     | 0               |
| 0 | 1 | 1 | 1     | 1               |
| 1 | 0 | 0 | 1     | 0               |
| 1 | 0 | 1 | 1     | 1               |
| 1 | 1 | 0 | 1     | 0               |
| 1 | 1 | 1 | 1     | 1               |

**Explicación de las columnas:**

* **A, B, C:** Son las tres entradas de la función lógica.
* **A + B:** Es la operación OR entre las entradas A y B (compuerta OR). El resultado es 1 si A es 1 o si B es 1 (o ambos).
* **F = (A + B) · C:** Es la operación AND entre el resultado de (A + B) y la entrada C (compuerta AND). El resultado final F es 1 solo si (A + B) es 1 *Y* C es 1.

3. **Función:** F = ¬(A · B)
Enlace del simulador 
[respuesta 3](https://circuitverse.org/users/308924/projects/resp3)

# Tabla de Verdad para la Función Lógica
| A | B | A · B | F = ¬(A · B) |
|---|---|-------|--------------|
| 0 | 0 | 0     | 1            |
| 0 | 1 | 0     | 1            |
| 1 | 0 | 0     | 1            |
| 1 | 1 | 1     | 0            |

**Explicación de las columnas:**

* **A, B:** Son las dos entradas de la función lógica.
* **A · B:** Es la operación AND entre las entradas A y B (compuerta AND). El resultado es 1 solo si tanto A como B son 1.
* **F = ¬(A · B):** Es la negación del resultado de la operación AND (compuerta NOT). Esta función también se implementa directamente con una compuerta NAND. El resultado final F es 1 si la salida de la AND es 0, y 0 si la salida de la AND es 1.

4. **Función:** F = (A ⊕ B) + (¬C · D)
Enlace del simulador 
[respuesta 4](https://circuitverse.org/users/308924/projects/resp4)

# Tabla de Verdad para la Función Lógica
| A | B | C | D | A ⊕ B | ¬C | ¬C · D | F = (A ⊕ B) + (¬C · D) |
|---|---|---|---|-------|----|--------|-------------------------|
| 0 | 0 | 0 | 0 | 0     | 1  | 0      | 0                       |
| 0 | 0 | 0 | 1 | 0     | 1  | 1      | 1                       |
| 0 | 0 | 1 | 0 | 0     | 0  | 0      | 0                       |
| 0 | 0 | 1 | 1 | 0     | 0  | 0      | 0                       |
| 0 | 1 | 0 | 0 | 1     | 1  | 0      | 1                       |
| 0 | 1 | 0 | 1 | 1     | 1  | 1      | 1                       |
| 0 | 1 | 1 | 0 | 1     | 0  | 0      | 1                       |
| 0 | 1 | 1 | 1 | 1     | 0  | 0      | 1                       |
| 1 | 0 | 0 | 0 | 1     | 1  | 0      | 1                       |
| 1 | 0 | 0 | 1 | 1     | 1  | 1      | 1                       |
| 1 | 0 | 1 | 0 | 1     | 0  | 0      | 1                       |
| 1 | 0 | 1 | 1 | 1     | 0  | 0      | 1                       |
| 1 | 1 | 0 | 0 | 0     | 1  | 0      | 0                       |
| 1 | 1 | 0 | 1 | 0     | 1  | 1      | 1                       |
| 1 | 1 | 1 | 0 | 0     | 0  | 0      | 0                       |
| 1 | 1 | 1 | 1 | 0     | 0  | 0      | 0                       |

**Explicación de las columnas:**

* **A, B, C, D:** Son las cuatro entradas de la función lógica.
* **A ⊕ B:** Es la operación XOR (compuerta XOR) entre las entradas A y B. El resultado es 1 si A y B son diferentes, y 0 si son iguales.
* **¬C:** Es la negación de la entrada C (compuerta NOT). Si C es 0, ¬C es 1, y si C es 1, ¬C es 0.
* **¬C · D:** Es la operación AND (compuerta AND) entre ¬C y la entrada D. El resultado es 1 solo si tanto ¬C como D son 1.
* **F = (A ⊕ B) + (¬C · D):** Es la operación OR (compuerta OR) entre el resultado de (A ⊕ B) y el resultado de (¬C · D). El resultado final F es 1 si (A ⊕ B) es 1 o si (¬C · D) es 1 (o ambos).

5. **Función:** F = ¬(A + B + C)
Enlace del simulador 
[respuesta 5](https://circuitverse.org/users/308924/projects/resp5)

# Tabla de Verdad para la Función Lógica
| A | B | C | A + B + C | F = ¬(A + B + C) |
|---|---|---|-----------|-----------------|
| 0 | 0 | 0 | 0         | 1               |
| 0 | 0 | 1 | 1         | 0               |
| 0 | 1 | 0 | 1         | 0               |
| 0 | 1 | 1 | 1         | 0               |
| 1 | 0 | 0 | 1         | 0               |
| 1 | 0 | 1 | 1         | 0               |
| 1 | 1 | 0 | 1         | 0               |
| 1 | 1 | 1 | 1         | 0               |

**Explicación de las columnas:**

* **A, B, C:** Son las tres entradas de la función lógica.
* **A + B + C:** Es la operación OR (compuerta OR) entre las entradas A, B y C. El resultado es 1 si al menos una de las entradas es 1.
* **F = ¬(A + B + C):** Es la negación del resultado de la operación OR (compuerta NOT). Esta función también se implementa directamente con una compuerta NOR. El resultado final F es 1 solo si la salida de la OR es 0 (es decir, cuando A, B y C son todas 0), y 0 en cualquier otro caso.

6. **Función:** F = (A · ¬B) + (C ⊕ D)
Enlace del simulador 
[respuesta 6](https://circuitverse.org/users/308924/projects/resp6)

# Tabla de Verdad para la Función Lógica
| A | B | C | D | ¬B | A · ¬B | C ⊕ D | F = (A · ¬B) + (C ⊕ D) |
|---|---|---|---|----|--------|-------|--------------------------|
| 0 | 0 | 0 | 0 | 1  | 0      | 0     | 0                        |
| 0 | 0 | 0 | 1 | 1  | 0      | 1     | 1                        |
| 0 | 0 | 1 | 0 | 1  | 0      | 1     | 1                        |
| 0 | 0 | 1 | 1 | 1  | 0      | 0     | 0                        |
| 0 | 1 | 0 | 0 | 0  | 0      | 0     | 0                        |
| 0 | 1 | 0 | 1 | 0  | 0      | 1     | 1                        |
| 0 | 1 | 1 | 0 | 0  | 0      | 1     | 1                        |
| 0 | 1 | 1 | 1 | 0  | 0      | 0     | 0                        |
| 1 | 0 | 0 | 0 | 1  | 1      | 0     | 1                        |
| 1 | 0 | 0 | 1 | 1  | 1      | 1     | 1                        |
| 1 | 0 | 1 | 0 | 1  | 1      | 1     | 1                        |
| 1 | 0 | 1 | 1 | 1  | 1      | 0     | 1                        |
| 1 | 1 | 0 | 0 | 0  | 0      | 0     | 0                        |
| 1 | 1 | 0 | 1 | 0  | 0      | 1     | 1                        |
| 1 | 1 | 1 | 0 | 0  | 0      | 1     | 1                        |
| 1 | 1 | 1 | 1 | 0  | 0      | 0     | 0                        |

**Explicación de las columnas:**

* **A, B, C, D:** Son las cuatro entradas de la función lógica.
* **¬B:** Es la negación de la entrada B (compuerta NOT). Si B es 0, ¬B es 1, y si B es 1, ¬B es 0.
* **A · ¬B:** Es la operación AND (compuerta AND) entre la entrada A y ¬B. El resultado es 1 solo si tanto A como ¬B son 1.
* **C ⊕ D:** Es la operación XOR (compuerta XOR) entre las entradas C y D. El resultado es 1 si C y D son diferentes, y 0 si son iguales.
* **F = (A · ¬B) + (C ⊕ D):** Es la operación OR (compuerta OR) entre el resultado de (A · ¬B) y el resultado de (C ⊕ D). El resultado final F es 1 si (A · ¬B) es 1 o si (C ⊕ D) es 1 (o ambos).

7. **Función:** F = ((A + B) · C) ⊕ D
Enlace del simulador 
[respuesta 7](https://circuitverse.org/users/308924/projects/resp7)

# Tabla de Verdad para la Función Lógica
| A | B | C | D | A + B | (A + B) · C | F = ((A + B) · C) ⊕ D |
|---|---|---|---|-------|-------------|-------------------------|
| 0 | 0 | 0 | 0 | 0     | 0           | 0                       |
| 0 | 0 | 0 | 1 | 0     | 0           | 1                       |
| 0 | 0 | 1 | 0 | 0     | 0           | 0                       |
| 0 | 0 | 1 | 1 | 0     | 0           | 1                       |
| 0 | 1 | 0 | 0 | 1     | 0           | 0                       |
| 0 | 1 | 0 | 1 | 1     | 0           | 1                       |
| 0 | 1 | 1 | 0 | 1     | 1           | 1                       |
| 0 | 1 | 1 | 1 | 1     | 1           | 0                       |
| 1 | 0 | 0 | 0 | 1     | 0           | 0                       |
| 1 | 0 | 0 | 1 | 1     | 0           | 1                       |
| 1 | 0 | 1 | 0 | 1     | 1           | 1                       |
| 1 | 0 | 1 | 1 | 1     | 1           | 0                       |
| 1 | 1 | 0 | 0 | 1     | 0           | 0                       |
| 1 | 1 | 0 | 1 | 1     | 0           | 1                       |
| 1 | 1 | 1 | 0 | 1     | 1           | 1                       |
| 1 | 1 | 1 | 1 | 1     | 1           | 0                       |

**Explicación de las columnas:**

* **A, B, C, D:** Son las cuatro entradas de la función lógica.
* **A + B:** Es la operación OR (compuerta OR) entre las entradas A y B. El resultado es 1 si A es 1 o si B es 1 (o ambos).
* **(A + B) · C:** Es la operación AND (compuerta AND) entre el resultado de (A + B) y la entrada C. El resultado es 1 solo si tanto (A + B) como C son 1.
* **F = ((A + B) · C) ⊕ D:** Es la operación XOR (compuerta XOR) entre el resultado de ((A + B) · C) y la entrada D. El resultado final F es 1 si ((A + B) · C) y D son diferentes, y 0 si son iguales.

8. **Función:** F = ((A · B) ⊙ (C + D))
Enlace del simulador 
[respuesta 8](https://circuitverse.org/users/308924/projects/resp8)

# Tabla de Verdad para la Función Lógica
| A | B | C | D | A · B | C + D | F = ((A · B) ⊙ (C + D)) |
|---|---|---|---|-------|-------|---------------------------|
| 0 | 0 | 0 | 0 | 0     | 0     | 1                         |
| 0 | 0 | 0 | 1 | 0     | 1     | 0                         |
| 0 | 0 | 1 | 0 | 0     | 1     | 0                         |
| 0 | 0 | 1 | 1 | 0     | 1     | 0                         |
| 0 | 1 | 0 | 0 | 0     | 0     | 1                         |
| 0 | 1 | 0 | 1 | 0     | 1     | 0                         |
| 0 | 1 | 1 | 0 | 0     | 1     | 0                         |
| 0 | 1 | 1 | 1 | 0     | 1     | 0                         |
| 1 | 0 | 0 | 0 | 0     | 0     | 1                         |
| 1 | 0 | 0 | 1 | 0     | 1     | 0                         |
| 1 | 0 | 1 | 0 | 0     | 1     | 0                         |
| 1 | 0 | 1 | 1 | 0     | 1     | 0                         |
| 1 | 1 | 0 | 0 | 1     | 0     | 0                         |
| 1 | 1 | 0 | 1 | 1     | 1     | 1                         |
| 1 | 1 | 1 | 0 | 1     | 1     | 1                         |
| 1 | 1 | 1 | 1 | 1     | 1     | 1                         |

**Explicación de las columnas:**

* **A, B, C, D:** Son las cuatro entradas de la función lógica.
* **A · B:** Es la operación AND (compuerta AND) entre las entradas A y B. El resultado es 1 solo si tanto A como B son 1.
* **C + D:** Es la operación OR (compuerta OR) entre las entradas C y D. El resultado es 1 si C es 1 o si D es 1 (o ambos).
* **F = ((A · B) ⊙ (C + D)):** Es la operación XNOR (compuerta XNOR) entre el resultado de (A · B) y el resultado de (C + D). El resultado final F es 1 si (A · B) y (C + D) son iguales (ambos 0 o ambos 1), y 0 si son diferentes.

9. **Función:** F = ¬A · (B + ¬C)
Enlace del simulador 
[respuesta 9](https://circuitverse.org/users/308924/projects/resp9)

# Tabla de Verdad para la Función Lógica
| A | B | C | ¬A | ¬C | B + ¬C | F = ¬A · (B + ¬C) |
|---|---|---|----|----|--------|--------------------|
| 0 | 0 | 0 | 1  | 1  | 1      | 1                  |
| 0 | 0 | 1 | 1  | 0  | 0      | 0                  |
| 0 | 1 | 0 | 1  | 1  | 1      | 1                  |
| 0 | 1 | 1 | 1  | 0  | 1      | 1                  |
| 1 | 0 | 0 | 0  | 1  | 1      | 0                  |
| 1 | 0 | 1 | 0  | 0  | 0      | 0                  |
| 1 | 1 | 0 | 0  | 1  | 1      | 0                  |
| 1 | 1 | 1 | 0  | 0  | 1      | 0                  |

**Explicación de las columnas:**

* **A, B, C:** Son las tres entradas de la función lógica.
* **¬A:** Es la negación de la entrada A (compuerta NOT). Si A es 0, ¬A es 1, y si A es 1, ¬A es 0.
* **¬C:** Es la negación de la entrada C (compuerta NOT). Si C es 0, ¬C es 1, y si C es 1, ¬C es 0.
* **B + ¬C:** Es la operación OR (compuerta OR) entre la entrada B y ¬C. El resultado es 1 si B es 1 o si ¬C es 1 (o ambos).
* **F = ¬A · (B + ¬C):** Es la operación AND (compuerta AND) entre ¬A y el resultado de (B + ¬C). El resultado final F es 1 solo si tanto ¬A como (B + ¬C) son 1.

10.**Función:**  F = ((A ⊕ B) · ¬C) + D 
Enlace del simulador 
[respuesta 10](https://circuitverse.org/users/308924/projects/resp10)

# Tabla de Verdad para la Función Lógica
| A | B | C | D | A ⊕ B | ¬C | (A ⊕ B) · ¬C | F = ((A ⊕ B) · ¬C) + D |
|---|---|---|---|-------|----|--------------|--------------------------|
| 0 | 0 | 0 | 0 | 0     | 1  | 0            | 0                        |
| 0 | 0 | 0 | 1 | 0     | 1  | 0            | 1                        |
| 0 | 0 | 1 | 0 | 0     | 0  | 0            | 0                        |
| 0 | 0 | 1 | 1 | 0     | 0  | 0            | 1                        |
| 0 | 1 | 0 | 0 | 1     | 1  | 1            | 1                        |
| 0 | 1 | 0 | 1 | 1     | 1  | 1            | 1                        |
| 0 | 1 | 1 | 0 | 1     | 0  | 0            | 0                        |
| 0 | 1 | 1 | 1 | 1     | 0  | 0            | 1                        |
| 1 | 0 | 0 | 0 | 1     | 1  | 1            | 1                        |
| 1 | 0 | 0 | 1 | 1     | 1  | 1            | 1                        |
| 1 | 0 | 1 | 0 | 1     | 0  | 0            | 0                        |
| 1 | 0 | 1 | 1 | 1     | 0  | 0            | 1                        |
| 1 | 1 | 0 | 0 | 0     | 1  | 0            | 0                        |
| 1 | 1 | 0 | 1 | 0     | 1  | 0            | 1                        |
| 1 | 1 | 1 | 0 | 0     | 0  | 0            | 0                        |
| 1 | 1 | 1 | 1 | 0     | 0  | 0            | 1                        |

**Explicación de las columnas:**

* **A, B, C, D:** Son las cuatro entradas de la función lógica.
* **A ⊕ B:** Es la operación XOR (compuerta XOR) entre las entradas A y B. El resultado es 1 si A y B son diferentes, y 0 si son iguales.
* **¬C:** Es la negación de la entrada C (compuerta NOT). Si C es 0, ¬C es 1, y si C es 1, ¬C es 0.
* **(A ⊕ B) · ¬C:** Es la operación AND (compuerta AND) entre el resultado de (A ⊕ B) y ¬C. El resultado es 1 solo si tanto (A ⊕ B) como ¬C son 1.
* **F = ((A ⊕ B) · ¬C) + D:** Es la operación OR (compuerta OR) entre el resultado de ((A ⊕ B) · ¬C) y la entrada D. El resultado final F es 1 si ((A ⊕ B) · ¬C) es 1 o si D es 1 (o ambos).