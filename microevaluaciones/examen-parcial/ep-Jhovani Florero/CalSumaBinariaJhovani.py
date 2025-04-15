import tkinter as tk

def sumar_binarios():
    try:
        binario1 = entrada_binario1.get()
        binario2 = entrada_binario2.get()

        # Validar que las entradas sean números binarios
        if not all(bit in '01' for bit in binario1) or not all(bit in '01' for bit in binario2):
            resultado_label.config(text="Error: Ingrese números binarios válidos.")
            return

        # Convertir los binarios a enteros
        decimal1 = int(binario1, 2)
        decimal2 = int(binario2, 2)

        # Sumar los enteros
        suma_decimal = decimal1 + decimal2

        # Convertir la suma decimal a binario
        resultado_binario = bin(suma_decimal)[2:]  # [2:] para quitar el "0b" inicial

        resultado_label.config(text=f"Suma Binaria: {resultado_binario}")

    except ValueError:
        resultado_label.config(text="Error: Ingrese números binarios válidos.")
    except Exception as e:
        resultado_label.config(text=f"Ocurrió un error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("SUMADOR DE BINARIOS")
ventana.geometry("400x250")

# Crear etiquetas y entradas para los números binarios
tk.Label(ventana, text="Primer Binario:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada_binario1 = tk.Entry(ventana, width=30)
entrada_binario1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(ventana, text="Segundo Binario:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_binario2 = tk.Entry(ventana, width=30)
entrada_binario2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Botón para sumar
sumar_boton = tk.Button(ventana, text="Sumar Binarios", command=sumar_binarios)
sumar_boton.grid(row=2, column=0, columnspan=2, pady=20)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Suma Binaria: ")
resultado_label.grid(row=3, column=0, columnspan=2, pady=10)

# Configurar el comportamiento de redimensionado de columnas
ventana.grid_columnconfigure(1, weight=1)

ventana.mainloop()