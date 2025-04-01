# 📚 ÁLGEBRA DE BOOLE EXPLICADA PARA PRINCIPIANTES

## 🔍 ¿QUÉ ES EL ÁLGEBRA DE BOOLE?
Es como el "idioma" de las computadoras. Trabaja solo con:
- **2 números**: 0 (Falso/Apagado) y 1 (Verdadero/Encendido)
- **3 operaciones básicas**:

| Operación | Símbolo | Ejemplo | Explicación |
|-----------|---------|---------|-------------|
| **AND** (Y) | · | A·B | Solo es 1 si AMBOS son 1 |
| **OR** (O) | + | A+B | Es 1 si AL MENOS UNO es 1 |
| **NOT** (NO) | ¬ | ¬A | Invierte el valor (1→0, 0→1) |

## 📝 LEYES BÁSICAS (CON EJEMPLOS)

### 1️⃣ Leyes de Identidad
- **A + 0 = A**  
  Ejemplo: Si A=1 → 1+0=1 (como decir "1 o nada = 1")
  
- **A · 1 = A**  
  Ejemplo: Si A=0 → 0·1=0 (como "0 y 1 = 0")

### 2️⃣ Leyes de Anulación
- **A + 1 = 1**  
  Ejemplo: 0+1=1 (si hay un 1, el OR siempre es 1)

- **A · 0 = 0**  
  Ejemplo: 1·0=0 (un AND con 0 siempre da 0)

### 3️⃣ Leyes de Idempotencia
- **A + A = A**  
  Ejemplo: 1+1=1 (no suma normal, es "1 o 1 = 1")

- **A · A = A**  
  Ejemplo: 0·0=0 (0 y 0 sigue siendo 0)

## 🧩 EJEMPLOS DETALLADOS

### Ejemplo 1: Simplificar (A + ¬A·B)
**Paso a paso:**
1. Aplicar Distributiva:  
   = (A + ¬A)·(A + B)  
   *(Como en matemáticas: x + y·z = (x+y)·(x+z))*
   
2. Resolver (A + ¬A):  
   = 1·(A + B)  
   *(Porque A o no-A siempre es 1)*
   
3. Aplicar identidad:  
   = A + B  
   *(1 y cualquier cosa = esa cosa)*

**Resultado final:** A + B

### Ejemplo 2: Aplicar De Morgan ¬(A·B)
**Ley:** ¬(A·B) = ¬A + ¬B

**Demostración con tabla:**

| A | B | A·B | ¬(A·B) | ¬A + ¬B |
|---|---|-----|--------|---------|
| 0 | 0 |  0  |   1    |   1+1=1  |
| 0 | 1 |  0  |   1    |   1+0=1  |
| 1 | 0 |  0  |   1    |   0+1=1  |
| 1 | 1 |  1  |   0    |   0+0=0  |

*¡Ambas columnas son iguales!*

### Ejemplo 3: Circuito Real
**Problema:** Diseñar un circuito para "Alarma si puerta abierta (A) O ventana abierta (B) Y no hay código de seguridad (¬C)"

**Expresión booleana:**  
Alarma = (A + B)·¬C

**Tabla de verdad:**

| A | B | C | Alarma |
|---|---|---|--------|
| 0 | 0 | 0 | (0+0)·1 = 0 |
| 0 | 1 | 0 | (0+1)·1 = 1 |
| 1 | 0 | 1 | (1+0)·0 = 0 |
| 1 | 1 | 0 | (1+1)·1 = 1 |

## 🎯 ¿POR QUÉ ES IMPORTANTE?
- Optimiza circuitos electrónicos
- Reduce componentes en hardware
- Base de la programación lógica
- Usado en:
  - Sistemas de seguridad
  - Procesadores
  - Redes lógicas

