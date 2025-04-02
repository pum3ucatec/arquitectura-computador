# SISTEMAS NUMÉRICOS Y CÓDIGOS

## 2.5 Códigos BCD (Binary-Coded Decimal)
    El código BCD es un sistema de representación de números decimales en formato binario. Cada dígito decimal (del 0 al 9) se codifica utilizando 4 bits. Por ejemplo:
    Decimal 5 → BCD: 0101
    Decimal 9 → BCD: 1001
    Este sistema es útil porque facilita la conversión entre números decimales y binarios, especialmente en aplicaciones como pantallas de 7 segmentos y sistemas electrónicos. Sin embargo, no es tan eficiente como el binario puro, ya que utiliza más bits para representar los mismos valores.
## 2.6 Como integrar los distintos elementos    
    Integrar los distintos elementos de sistemas numéricos y códigos implica combinar las representaciones y mecanismos que permiten operar con datos de manera eficiente y estructurada. Esto incluye:
        - Sistemas Numéricos: Utilizar formatos como binario, decimal, octal o hexadecimal para representar valores numéricos y operar con ellos dentro de un sistema digital.
        - Codificación: Traducir información mediante códigos como ASCII, Unicode, o sistemas de compresión para comunicación, almacenamiento y procesamiento.
        - Elementos Electrónicos y Lógicos: Incorporar hardware como puertas lógicas, circuitos integrados y otros componentes que ejecuten las operaciones basadas en estos sistemas.
        - Sincronización: Establecer reglas o protocolos que coordinen cómo los datos y operaciones fluyen entre los diferentes elementos.










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




