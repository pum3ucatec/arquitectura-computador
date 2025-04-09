# SISTEMAS NUMÉRICOS Y CÓDIGOS

 # 2.1. Conversión de Binario a Decimal
Los números binarios están compuestos solo por 0 y 1 ⚫⚪. Para convertirlos a decimal, se usa la potencia de 2 en cada dígito según su posición.

✅ Ejemplo: Convertir el binario 1011 a decimal:
1 × 2³ + 0 × 2² + 1 × 2¹ + 1 × 2⁰
= 8 + 0 + 2 + 1
= 11
📌 Regla clave: Multiplica cada bit por 2 elevado a su posición, y luego suma los resultados.

# 2.2. Conversión de Decimal a Binario
Para pasar de decimal a binario, se divide el número entre 2 hasta obtener un cociente de 0, y se leen los residuos de abajo hacia arriba 📈.

✅ Ejemplo: Convertir el decimal 13 a binario:
13 ÷ 2  → Cociente: 6   Residuo: 1  
6  ÷ 2  → Cociente: 3   Residuo: 0  
3  ÷ 2  → Cociente: 1   Residuo: 1  
1  ÷ 2  → Cociente: 0   Residuo: 1  
✔ Resultado final: 1101 🖥️

📌 Regla clave: Divide entre 2 y guarda los residuos, luego léelos en orden inverso 🔄.

📊 Conclusión:
Las conversiones entre binario y decimal son fundamentales en la computación 💻, ya que las computadoras procesan información en código binario. ¡Dominarlas te hará comprender mejor cómo funciona la tecnología! 🚀


# 📌 2.3. Sistemas de Numeración Octal

## Introducción

El sistema de numeración octal es un sistema de base 8 que utiliza los dígitos del 0 al 7 para representar números. Es especialmente útil en el ámbito de la informática y la programación, ya que permite representar números binarios de manera más compacta agrupando bits en conjuntos de tres.

El sistema octal se utiliza en aplicaciones donde la manipulación de bits es fundamental, como en sistemas embebidos, programación a bajo nivel y desarrollo de software relacionado con sistemas operativos.

## ¿Por qué usar el sistema octal?

El sistema octal resulta útil en situaciones donde es necesario simplificar cadenas largas de números binarios. Dado que cada dígito octal corresponde exactamente a tres bits binarios, su conversión es directa y eficiente.

## 📝 Ejemplo:

Binario: 110 101 -> Octal: 65

# 📌 2.4. Sistemas de Numeración Hexadecimal

## Introducción

El sistema de numeración hexadecimal es un sistema de base 16 que utiliza los dígitos del 0 al 9 y las letras de la A a la F para representar números. Es ampliamente utilizado en informática y programación debido a su capacidad para representar números binarios de manera más compacta, agrupando bits en conjuntos de cuatro.

El sistema hexadecimal es común en el desarrollo de software de bajo nivel, depuración, representación de direcciones de memoria y codificación de colores en diseño web.

## ¿Por qué usar el sistema hexadecimal?

El sistema hexadecimal resulta útil porque permite expresar números binarios largos de forma más compacta y legible. Cada dígito hexadecimal equivale a cuatro bits binarios, lo que simplifica su conversión y manipulación.

## 📝 Ejemplo:

Binario: 1010 1111 -> Hexadecimal: AF

## 📌 2.5 Códigos BCD (Binary-Coded Decimal)
El código BCD es un sistema de representación de números decimales en formato binario. Cada dígito decimal (del 0 al 9) se codifica utilizando 4 bits. Por ejemplo:

- Decimal 5 → BCD: 0101
- Decimal 9 → BCD: 1001

Este sistema es útil porque facilita la conversión entre números decimales y binarios, especialmente en aplicaciones como pantallas de 7 segmentos y sistemas electrónicos. Sin embargo, no es tan eficiente como el binario puro, ya que utiliza más bits para representar los mismos valores.
## 📌 2.6 Como integrar los distintos elementos    
Integrar los distintos elementos de sistemas numéricos y códigos implica combinar las representaciones y mecanismos que permiten operar con datos de manera eficiente y estructurada. Esto incluye:
- Sistemas Numéricos: Utilizar formatos como binario, decimal, octal o hexadecimal para representar valores numéricos y operar con ellos dentro de un sistema digital.
- Codificación: Traducir información mediante códigos como ASCII, Unicode, o sistemas de compresión para comunicación, almacenamiento y procesamiento.
- Elementos Electrónicos y Lógicos: Incorporar hardware como puertas lógicas, circuitos integrados y otros componentes que ejecuten las operaciones basadas en estos sistemas.
- Sincronización: Establecer reglas o protocolos que coordinen cómo los datos y operaciones fluyen entre los diferentes elementos.

## 2.7 Código Gray

### 📌 Definición

El **código Gray** es un sistema de codificación binaria en el cual **dos números consecutivos difieren únicamente en un solo bit**. También se conoce como **código binario reflejado**, y es ampliamente utilizado en sistemas donde se desea **minimizar errores durante la transición** entre estados.

### 🎯 Propósito

- Reducir errores de lectura en sistemas donde los bits cambian rápidamente.
- Asegurar una transición **segura y controlada** entre estados binarios.

### 🧪 Ejemplo Comparativo

| Decimal | Binario | Código Gray |
|---------|---------|-------------|
| 0       | 000     | 000         |
| 1       | 001     | 001         |
| 2       | 010     | 011         |
| 3       | 011     | 010         |
| 4       | 100     | 110         |
| 5       | 101     | 111         |
| 6       | 110     | 101         |
| 7       | 111     | 100         |

> 💡 **Nota:** En cada transición, solo **un bit cambia** respecto al anterior.

### ✅ Ventajas

- Disminuye la probabilidad de errores de transición.
- Ideal para **encoders rotatorios**, **conversores ADC**, y sensores digitales.

### 📍 Aplicaciones

- Sistemas de medición angular (encoders ópticos).
- Equipos industriales con movimiento rotativo.
- Conversores analógicos a digitales (ADC).

---

## 2.8 Códigos Alfanuméricos

### 📌 Definición

Los **códigos alfanuméricos** son sistemas binarios diseñados para representar **letras, números y símbolos especiales**. Permiten que los sistemas digitales puedan **leer, escribir y procesar texto**.

### 💻 Código ASCII (American Standard Code for Information Interchange)

Es el estándar más común. Utiliza **7 bits** (o 8 bits en su versión extendida) para representar hasta **128** o **256** caracteres, incluyendo letras, números, signos de puntuación y caracteres de control.

### 🧪 Ejemplo de Tabla ASCII

| Carácter | Decimal | Binario    |
|----------|---------|------------|
| A        | 65      | 01000001   |
| B        | 66      | 01000010   |
| 1        | 49      | 00110001   |
| !        | 33      | 00100001   |
| espacio  | 32      | 00100000   |

### 🔠 Otros Códigos Alfanuméricos

- **EBCDIC:** Utilizado en sistemas IBM.
- **Unicode:** Código moderno y universal que permite representar símbolos de **todos los idiomas del mundo**, emojis, símbolos científicos, etc.

### ✅ Ventajas

- Posibilita el uso de texto en sistemas digitales.
- Facilita la **interoperabilidad entre sistemas** mediante el uso de estándares comunes.

### 📍 Aplicaciones

- Comunicación entre computadoras y periféricos.
- Almacenamiento y edición de texto.
- Programación de sistemas embebidos.
- Visualización de datos en pantallas digitales.

---

# 2.9. Método de Paridad para Detección de Errores

## Resumen

El método de paridad detecta errores en datos transmitidos añadiendo un bit extra (paridad) para que el total de bits "1" sea par o impar.

## Tipos

* **Paridad par:** Total de "1" debe ser par.
* **Paridad impar:** Total de "1" debe ser impar.

## Funcionamiento

1.  **Emisor:** Calcula y añade el bit de paridad.
2.  **Receptor:** Verifica si la paridad es correcta; si no, detecta error.

## Limitaciones

* Solo detecta errores, no los corrige.
* No detecta errores de múltiples bits.
* Ineficiente para errores de un bit.

## Casos de Uso

* Comunicaciones seriales simples.
* Memorias.
* Sistemas de bajo costo.

## Alternativas

* Códigos de Hamming (corrección de errores).
* CRC (detección de errores múltiples).
* Códigos Reed-Solomon (corrección de errores múltiples).
