# SISTEMAS NUMÉRICOS Y CÓDIGOS

# 📌 2.3. Sistemas de Numeración Octal

## Introducción

El sistema de numeración octal es un sistema de base 8 que utiliza los dígitos del 0 al 7 para representar números. Es especialmente útil en el ámbito de la informática y la programación, ya que permite representar números binarios de manera más compacta agrupando bits en conjuntos de tres.

El sistema octal se utiliza en aplicaciones donde la manipulación de bits es fundamental, como en sistemas embebidos, programación a bajo nivel y desarrollo de software relacionado con sistemas operativos.

## ¿Por qué usar el sistema octal?

El sistema octal resulta útil en situaciones donde es necesario simplificar cadenas largas de números binarios. Dado que cada dígito octal corresponde exactamente a tres bits binarios, su conversión es directa y eficiente.

## 📝 Ejemplo:

Binario: 110 101 -> Octal: 65

Además, el sistema octal es más compacto que el binario y más fácil de manejar visualmente al trabajar con datos en bajo nivel.

# 📌 2.4. Sistemas de Numeración Hexadecimal

## Introducción

El sistema de numeración hexadecimal es un sistema de base 16 que utiliza los dígitos del 0 al 9 y las letras de la A a la F para representar números. Es ampliamente utilizado en informática y programación debido a su capacidad para representar números binarios de manera más compacta, agrupando bits en conjuntos de cuatro.

El sistema hexadecimal es común en el desarrollo de software de bajo nivel, depuración, representación de direcciones de memoria y codificación de colores en diseño web.

## ¿Por qué usar el sistema hexadecimal?

El sistema hexadecimal resulta útil porque permite expresar números binarios largos de forma más compacta y legible. Cada dígito hexadecimal equivale a cuatro bits binarios, lo que simplifica su conversión y manipulación.

## 📝 Ejemplo:

Binario: 1010 1111 -> Hexadecimal: AF

Además, su uso es fundamental al trabajar con registros, direcciones de memoria y datos en el contexto de sistemas y programación a bajo nivel.







# 2.9. Método de Paridad para Detección de Errores

El método de paridad es una técnica simple pero fundamental en la transmisión de datos para detectar errores. Se basa en añadir un bit extra, llamado **bit de paridad**, a un conjunto de bits de datos. Este bit se calcula de tal manera que el número total de bits "1" en el conjunto (datos + bit de paridad) cumpla con una regla predefinida: ser par o impar.

## Conceptos Clave

* **Bit de Paridad:** Un bit adicional añadido a un conjunto de datos para detectar errores.
* **Paridad par:** El número total de bits "1" debe ser par.
* **Paridad impar:** El número total de bits "1" debe ser impar.

## Tipos de Paridad en Detalle

* **Paridad par:**
    * El bit de paridad se establece en "0" si el número de bits "1" en los datos es par.
    * El bit de paridad se establece en "1" si el número de bits "1" en los datos es impar.
    * Resultado: el número total de bits "1" transmitidos (datos + bit de paridad) siempre será par.
* **Paridad impar:**
    * El bit de paridad se establece en "1" si el número de bits "1" en los datos es par.
    * El bit de paridad se establece en "0" si el número de bits "1" en los datos es impar.
    * Resultado: el número total de bits "1" transmitidos (datos + bit de paridad) siempre será impar.

## Funcionamiento Paso a Paso con Ejemplos

1.  **Emisor:**
    * **Ejemplo con paridad par:**
        * Datos a transmitir: "1011001"
        * Número de bits "1": 4 (par)
        * Bit de paridad: 0
        * Datos transmitidos: "10110010"
    * **Ejemplo con paridad impar:**
        * Datos a transmitir: "1011001"
        * Número de bits "1": 4 (par)
        * Bit de paridad: 1
        * Datos transmitidos: "10110011"
2.  **Receptor:**
    * **Ejemplo de recepción sin errores (paridad par):**
        * Datos recibidos: "10110010"
        * Número de bits "1": 4 (par)
        * Verificación: coincide con la paridad esperada.
        * Resultado: no se detecta error.
    * **Ejemplo de recepción con error (paridad par):**
        * Datos recibidos: "10110110" (un bit "0" se cambió a "1")
        * Número de bits "1": 5 (impar)
        * Verificación: no coincide con la paridad esperada.
        * Resultado: se detecta error.

## Limitaciones Detalladas

* **Detección vs. Corrección:**
    * La paridad solo indica que ocurrió un error, pero no dónde.
    * No es posible corregir el error automáticamente con este método.
* **Errores Múltiples:**
    * Si dos bits cambian durante la transmisión, el número total de bits "1" podría seguir siendo par (o impar), y el error no se detectaría.
    * Ejemplo: si "10110010" se convierte en "10101110", el número de bits "1" sigue siendo 4.
* **Eficiencia:**
    * El método de paridad es muy simple, pero a su vez muy ineficiente, ya que solo detecta errores de un bit, y gasta un bit por cada byte enviado.

## Casos de Uso

* **Comunicaciones seriales:**
    * En conexiones seriales simples, como las que se utilizaban para conectar módems o impresoras, la paridad se utilizaba para verificar la integridad de los datos.
* **Memorias:**
    * Algunos sistemas de memoria utilizan bits de paridad para detectar errores de un solo bit en los datos almacenados.
* **Sistemas simples:**
    * En sistemas que requieren una detección de errores muy simple y de bajo costo, la paridad puede ser una opción viable.

## Alternativas

Para aplicaciones que requieren mayor fiabilidad, existen técnicas más avanzadas como:

* **Códigos de Hamming:**
    * Permiten detectar y corregir errores de un solo bit.
* **CRC (Cyclic Redundancy Check):**
    * Detecta errores múltiples con alta probabilidad.
* **Códigos de Reed-Solomon:**
    * Usados en CD, DVD, y discos duros, puede corregir multiples errores.




