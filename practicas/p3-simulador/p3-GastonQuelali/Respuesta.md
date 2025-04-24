1. Enlace simulador de la [respuesta 1}(https://circuitverse.org/users/308909/projects/respuesta-1)

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

---

