# README - Programa de Suma Binaria en Java

## 📝 Descripción
Este programa implementa una calculadora de suma binaria con interfaz gráfica en Java. Permite sumar dos números binarios ingresados por el usuario y muestra el resultado en formato binario.

## 🛠️ Características principales
- **Interfaz gráfica** intuitiva y fácil de usar
- **Validación de entrada** para asegurar que solo se ingresen números binarios (0s y 1s)
- **Conversión automática** de números binarios a decimales para realizar la suma
- **Resultado en binario** mostrado en un campo de solo lectura

## 🚀 Cómo ejecutar el programa

### Requisitos previos
- Java Development Kit (JDK) 8 o superior instalado

### Pasos para ejecutar:
1. Copiar el código completo en un archivo llamado `Main.java`
2. Abrir una terminal en la ubicación del archivo
3. Compilar el programa con:
   ```bash
   javac Main.java
   ```
4. Ejecutar el programa con:
   ```bash
   java Main
   ```

## 🖥️ Interfaz de usuario
La aplicación muestra una ventana con:
- Dos campos de texto para ingresar los números binarios
- Un botón "Sumar" para realizar la operación
- Un campo de resultado que muestra la suma en binario

## ⚠️ Validaciones
El programa verifica que:
- Ambos campos contengan datos
- Los datos ingresados sean solo 0s y 1s
- Los números no estén vacíos

## 📊 Ejemplo de uso
1. Ingresar `1010` en el primer campo (equivalente a 10 en decimal)
2. Ingresar `1100` en el segundo campo (equivalente a 12 en decimal)
3. Hacer clic en "Sumar"
4. El resultado mostrará `10110` (equivalente a 22 en decimal)

## 📁 Estructura del código
El programa contiene tres clases internas:
1. **Main**: Punto de entrada de la aplicación
2. **SumaBinariaLogic**: Maneja la lógica de validación y suma binaria
3. **SumaBinariaGUI**: Implementa la interfaz gráfica de usuario

## 📄 Licencia
Este proyecto es de código abierto y puede ser utilizado libremente para fines educativos.

```
javac -d bin $(find . -name "*.java")
```

```
java -cp bin Main
```
