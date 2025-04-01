from calculadora import CalculadoraApp # Importar la clase CalculadoraApp desde el módulo calculadora
from utilidades.estilos import configurar_estilos # Importar la función configurar_estilos desde el módulo utilidades.estilos
import tkinter as tk # Importar tkinter como tk para crear la interfaz gráfica

def iniciar_app():
    root = tk.Tk()
    configurar_estilos()
    app = CalculadoraApp(root)
    root.mainloop()