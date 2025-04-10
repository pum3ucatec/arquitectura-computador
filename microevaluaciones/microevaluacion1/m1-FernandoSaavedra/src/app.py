import tkinter as tk # Importar tkinter como tk para crear la interfaz gráfica
from utilidades.estilos import configurar_estilos # Importar la función configurar_estilos desde el módulo utilidades.estilos
from .calculadora import CalculadoraBinaria

def iniciar_aplicacion(): # Función para iniciar la aplicación de la calculadora binaria
    root = tk.Tk()
    configurar_estilos()
    app = CalculadoraBinaria(root)
    root.mainloop()