## TEMA 1


![Electronica Digital](/doc/images/electronica-digital.jpg)

# 1. INTRODUCCION A LA ELECTRONICA DIGITAL

La electrónica digital es una rama de la electrónica que trabaja con señales digitales en lugar de analógicas. 
Las señales digitales solo tienen dos estados posibles: alto (1) y bajo (0).
Estos estados se representan comúnmente como números binarios y son la base de sistemas como computadoras, teléfonos móviles y otros dispositivos electrónicos modernos.
    
Alto (1): Representa un nivel de voltaje más alto en el circuito digital. Este estado está asociado con "encendido" o un estado activo.
Bajo (0): Corresponde a un nivel de voltaje más bajo. Este estado se asocia con "apagado" o inactividad.

En un sistema digital, los componentes clave son los circuitos digitales, que están formados por **puertas lógicas**. 
Estas puertas lógicas procesan las señales binarias siguiendo reglas específicas para realizar operaciones como sumas, comparaciones, etc.
Por ejemplo, el procesador de una computadora es un circuito digital muy complejo que realiza millones de operaciones basadas en combinaciones de los estados alto y bajo.


# 2. REPRESENTACIÓN NUMÉRICA EN COMPUTACIÓN

## 🔢 SISTEMAS NUMÉRICOS

En computación y matemáticas, un sistema numérico es un conjunto de reglas y símbolos utilizados para representar números. Existen varios sistemas 
numéricos, pero los más comunes son:

1. Decimal (Base 10): Es el sistema que usamos en la vida cotidiana, basado en diez dígitos (0-9).
2. Binario (Base 2): Utilizado en computación, emplea solo dos dígitos: 0 y 1.
3. Octal (Base 8): Usa ocho dígitos (0-7) y a veces se usa en programación.
4. Hexadecimal (Base 16): Usa dieciséis símbolos (0-9 y A-F) y es común en informática para representar direcciones de memoria y colores en HTML.

## 🔄 CONVERSIONES RÁPIDAS

- Binario → Octal: Agrupar de 3 en 3 bits  
  `110101₂ → 110 101 → 65₈`  
- Binario → Hex: Agrupar de 4 en 4 bits  
  `11011010₂ → 1101 1010 → DA₁₆`  

## 📊 TABLA COMPARATIVA

| Sistema | Base | Dígitos | Ejemplo | Aplicación |
|---------|------|---------|---------|------------|
| Binario | 2 | 0,1 | 1011₂ | Operaciones CPU |
| Octal | 8 | 0-7 | 34₈ | Permisos Linux |
| Decimal | 10 | 0-9 | 25₁₀ | Uso diario |
| Hexadecimal | 16 | 0-F | A3₁₆ | Memoria/Colores |

## 📝 EJERCICIOS RESUELTOS

1. 110101₂ → 32 + 16 + 4 + 1 = 53₁₀  
2. 27₁₀ → Binario: 11011₂, Hex: 1B₁₆  
3. 3F₁₆ → 3×16 + 15 = 63₁₀  

## 💡 APLICACIONES PRÁCTICAS

- Binario: Lenguaje máquina (ej: 1011b)  
- Octal: chmod 755 (permisos archivos)  
- Hex: #FFFFFF (colores web), 0x7FFF (direcciones memoria)  

# 📌 3. Conversiones entre Sistemas Numéricos

## Sitemas numéricos 

La conversión entre sistemas numéricos es una habilidad esencial para los informáticos y matemáticos. Implica el proceso de convertir un número de una base a otra. Exinten varios pero los mas comunes son:

**BINARIO (Base 2)**  
   - Dígitos: 0, 1  
   - Ejemplo: 1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11₁₀  

 **OCTAL (Base 8)**  
   - Dígitos: 0-7  
   - Ejemplo: 34₈ = 3×8¹ + 4×8⁰ = 24 + 4 = 28₁₀  

 **DECIMAL (Base 10)**  
   - Dígitos: 0-9  
   - Conversión a binario:  
     25 ÷ 2 = 12 (1)  
     12 ÷ 2 = 6 (0)  
     6 ÷ 2 = 3 (0)  
     3 ÷ 2 = 1 (1)  
     1 ÷ 2 = 0 (1) → 11001₂  

 **HEXADECIMAL (Base 16)**  
   - Dígitos: 0-9, A-F  
   - Ejemplos:  
     - A3₁₆ = 10×16 + 3 = 163₁₀  
     - 45₁₀ → 2D₁₆ (45÷16=2 resto 13(D), 2÷16=0 resto 2) 

## Importancia de las conversiones

La conversión entre estos sistemas es fundamental en programación, electrónica digital y redes de computadoras. Por ejemplo, un programador puede necesitar convertir un número decimal a binario para entender mejor cómo lo procesa una computadora.

## 📝 Métodos de Conversión

Las conversiones entre sistemas numéricos pueden realizarse de varias maneras:

1.	De Decimal a Otra Base: Dividiendo sucesivamente entre la base de destino y anotando los residuos.
2.	De Otra Base a Decimal: Multiplicando cada dígito por la base elevada a su posición correspondiente.
3.	Entre Bases Diferentes (Binario, Octal, Hexadecimal): Usando conversiones intermedias a decimal o mediante reglas directas.


 # 4. Códigos Binarios ✨🔋
La electrónica digital es la base de todos los dispositivos modernos 🖥️📱. Se encarga de procesar información en forma de señales binarias (0 y 1), que representan dos estados: apagado (0) y encendido (1) 🔴🟢.

📌 ¿Qué son los códigos binarios?
Un código binario es un sistema de representación donde cada número o dato se expresa con ceros y unos (bits) 🏁. Es la base de la comunicación entre los circuitos electrónicos y los procesadores.

🔢 Tipos de códigos binarios más usados
✅ Código BCD (Decimal Codificado en Binario): Representa números decimales usando 4 bits por dígito. Ejemplo: el 9 en BCD es 1001.
✅ Código ASCII: Asigna valores binarios a caracteres como letras y símbolos ✍️💾.
✅ Código Gray: Se usa en sensores y telecomunicaciones porque solo cambia un bit entre valores consecutivos 🔄.
✅ Código Excess-3: Una variante del BCD utilizada en algunos sistemas digitales.

⚡ Importancia de los códigos binarios
📡 Permiten la comunicación entre dispositivos electrónicos.
🖥️ Son la base del almacenamiento y procesamiento de datos.
🔍 Se utilizan en sistemas digitales como computadoras, teléfonos y circuitos lógicos.

La electrónica digital y los códigos binarios hacen posible la tecnología moderna 🚀🤖. ¡Todo lo que ves en pantallas o dispositivos electrónicos funciona gracias a ellos!

 # 5. Códigos Detectores

Los códigos detectores son secuencias de bits agregadas a los datos transmitidos con el objetivo de detectar e incluso corregir errores que puedan ocurrir durante la transmisión o almacenamiento. Estos códigos son fundamentales para garantizar la integridad de la información en sistemas digitales.

🧠 ¿Cómo Funcionan?
Transmisión:
 El transmisor agrega bits adicionales (de paridad o corrección) al mensaje original según el tipo de código usado.

Recepción:
 El receptor analiza estos bits agregados para verificar la integridad de los datos y detectar posibles errores.

Corrección (en algunos casos):
 Algunos códigos permiten no solo detectar errores, sino corregir automáticamente aquellos que sean simples.

🧩 Tipos Comunes de Códigos Detectores
✔️ 1. Código de Paridad
Agrega un solo bit de control (bit de paridad) al conjunto de datos.

El bit de paridad puede ser par (even) o impar (odd):

Paridad par: El número total de 1s (incluido el bit de paridad) debe ser par.

Paridad impar: El número total de 1s debe ser impar.

Capacidad: Detecta errores de un solo bit.

Limitación: No puede corregir errores, ni detectar errores múltiples.

🛠️ 2. Código de Hamming
Introduce varios bits de control en posiciones específicas.
Permite:

Detección de errores de uno o más bits.

Corrección automática de errores de un solo bit.

Usa una técnica de verificación cruzada entre múltiples posiciones.

📦 3. Códigos de Bloque
Agrupan los datos en bloques de longitud fija.
Se añaden bits de verificación a cada bloque.
Capaces de:

Detectar errores múltiples.

Corregir múltiples errores dependiendo de la estructura usada (por ejemplo, códigos Reed-Solomon).

Muy utilizados en sistemas que manejan grandes volúmenes de datos.

🚀 Aplicaciones
Los códigos detectores son fundamentales en áreas donde la confiabilidad de los datos es crítica:
Redes de comunicación digital (Wi-Fi, Ethernet, etc.)

Memorias RAM y ROM

Discos duros y SSDs

Comunicaciones por satélite

Transmisiones multimedia (audio/video digital)

Sistemas embebidos y microcontroladores

✅ Ventajas
Fiabilidad: Aseguran que los datos no se corrompan durante la transmisión o almacenamiento.

Corrección automática: Algunos códigos permiten corregir errores sin intervención externa, mejorando la eficiencia del sistema.

Detección rápida: Identifican errores de manera inmediata, evitando procesamiento adicional de datos corruptos.

❌ Desventajas
Sobrecarga de datos: La adición de bits extra incrementa el tamaño de la transmisión, lo que puede afectar el rendimiento.

Complejidad: Algunos métodos como Hamming o Reed-Solomon requieren procesamiento adicional y hardware/software más complejo para su implementación.

Limitación en detección: Ciertos códigos no pueden detectar errores múltiples o corregir más de un bit.

## Bibliografia

![Organización y arquitectura de computadores](/doc/images/libro-referencia.png)
