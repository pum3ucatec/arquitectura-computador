# Sumador de Binarios con Interfaz Gráfica

Este proyecto implementa una sencilla interfaz gráfica de usuario (GUI) para sumar dos números binarios. La aplicación está desarrollada utilizando la biblioteca `tkinter` de Python, lo que la hace fácil de usar y entender.

## Funcionalidades

* **Entrada de Binarios:** Permite al usuario ingresar dos números binarios a través de campos de texto dedicados.
* **Validación de Entrada:** Verifica que los datos ingresados en ambos campos sean cadenas válidas compuestas únicamente por los caracteres '0' y '1'.
* **Cálculo de la Suma:** Convierte los números binarios ingresados a sus equivalentes decimales, realiza la suma de estos valores decimales y luego convierte el resultado nuevamente a su representación binaria.
* **Visualización del Resultado:** Muestra el resultado de la suma binaria de forma clara en una etiqueta dentro de la ventana de la aplicación.
* **Manejo de Errores:** Proporciona mensajes de error informativos en caso de que el usuario ingrese datos no válidos (que no sean números binarios).

## Requisitos

* **Python 3.x:** Este código está escrito en Python 3 y requiere un intérprete de Python 3 para su ejecución.
* **tkinter:** La biblioteca `tkinter` es la interfaz gráfica estándar para Python. Generalmente viene incluida con las instalaciones estándar de Python, por lo que no se requiere una instalación adicional en la mayoría de los casos.

## Cómo Utilizar

1.  **Clona o Descarga el Repositorio:** Si este código está en un repositorio de GitHub, puedes clonarlo a tu máquina local usando `git clone <URL_DEL_REPOSITORIO>`. Alternativamente, puedes descargar el archivo `.py` directamente.

2.  **Ejecuta el Script:** Abre una terminal o símbolo del sistema, navega hasta el directorio donde guardaste el archivo y ejecuta el script usando el comando:

    ```bash
    python CalSumaBinariaJhovani.py
    ```

3.  **Interactúa con la Interfaz:**
    * Una ventana titulada "SUMADOR DE BINARIOS" aparecerá en tu pantalla.
    * En el campo etiquetado como "Primer Binario:", ingresa el primer número binario que deseas sumar.
    * En el campo etiquetado como "Segundo Binario:", ingresa el segundo número binario que deseas sumar.
    * Haz clic en el botón "Sumar Binarios".
    * El resultado de la suma binaria se mostrará en la etiqueta debajo del botón, que dirá "Suma Binaria: [resultado]".
    * Si ingresas valores no válidos (caracteres diferentes de '0' o '1'), se mostrará un mensaje de error indicando que ingreses números binarios válidos.