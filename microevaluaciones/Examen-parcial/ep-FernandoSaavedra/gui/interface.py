import tkinter as tk
from tkinter import messagebox
from controller.calculator import sumar_binarios
from utils.validator import es_binario

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Calculadora Binaria de Suma")
    ventana.geometry("400x250")

    tk.Label(ventana, text="Primer número binario:").pack()
    entrada1 = tk.Entry(ventana)
    entrada1.pack()

    tk.Label(ventana, text="Segundo número binario:").pack()
    entrada2 = tk.Entry(ventana)
    entrada2.pack()

    resultado_label = tk.Label(ventana, text="Resultado: ", font=('Arial', 14))
    resultado_label.pack(pady=10)

    def calcular():
        bin1 = entrada1.get()
        bin2 = entrada2.get()
        if not es_binario(bin1) or not es_binario(bin2):
            messagebox.showerror("Error", "Por favor ingresa solo números binarios (0 y 1).")
            return
        resultado = sumar_binarios(bin1, bin2)
        resultado_label.config(text=f"Resultado: {resultado}")

    boton = tk.Button(ventana, text="Sumar", command=calcular)
    boton.pack(pady=10)

    ventana.mainloop()
