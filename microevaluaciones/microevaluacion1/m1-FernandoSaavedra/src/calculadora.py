import tkinter as tk #Es la importacion de la biblioteca Tkinter para la interfaz gráfica, con alias tk para abreviar.
from tkinter import ttk, messagebox #Importa ttk y messagebox de tkinter para crear widgets y mostrar mensajes emergentes.
from operaciones.aritmetica import sumar_binario, restar_binario #Importa las funciones de suma y resta binaria desde el módulo operaciones.aritmetica.
from operaciones.conversion import decimal_a_binario, binario_a_decimal #Importa las funciones de conversión entre decimal y binario desde el módulo operaciones.conversion.
from utilidades.validacion import validar_binario, validar_decimal #Importa funciones de validación desde el módulo utilidades.validacion.

class CalculadoraBinaria: 
    def __init__(self, root): #Constructor de la clase CalculadoraBinaria, inicializa la interfaz gráfica y el historial.
        self.root = root
        self.configurar_interfaz()
        self.historial = []
        
    def configurar_interfaz(self):
        self.root.title("Calculadora Binaria")
        self.root.geometry("800x600") #Establece el título y tamaño de la ventana principal.
        
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(expand=True, fill='both') #Crea un marco principal con relleno y lo expande para llenar la ventana.
        
        # Sección binaria 
        ttk.Label(main_frame, text="Calculadora Binaria").grid(row=0, column=0, columnspan=4)
        
        self.entrada_bin1 = ttk.Entry(main_frame)
        self.entrada_bin1.grid(row=1, column=0, padx=5, pady=5)
        
        self.entrada_bin2 = ttk.Entry(main_frame)
        self.entrada_bin2.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(main_frame, text="+", command=self.sumar, style='Operacion.TButton').grid(row=1, column=2, padx=5)
        ttk.Button(main_frame, text="-", command=self.restar, style='Operacion.TButton').grid(row=1, column=3, padx=5)
        
        # Sección conversión
        ttk.Label(main_frame, text="Conversión Decimal ↔ Binario").grid(row=2, column=0, columnspan=4, pady=10)
        
        self.entrada_decimal = ttk.Entry(main_frame)
        self.entrada_decimal.grid(row=3, column=0, padx=5)
        ttk.Button(main_frame, text="→ Bin", command=self.dec_a_bin).grid(row=3, column=1, padx=5)
        
        self.entrada_binario = ttk.Entry(main_frame)
        self.entrada_binario.grid(row=3, column=2, padx=5)
        ttk.Button(main_frame, text="→ Dec", command=self.bin_a_dec).grid(row=3, column=3, padx=5)
        
        # Resultados de la operación
        self.resultado = ttk.Label(main_frame, text="Resultado: ", font=('Arial', 14))
        self.resultado.grid(row=4, column=0, columnspan=4, pady=20)
        
        # Historial de las operaciones realizadas
        self.historial_text = tk.Text(main_frame, height=5, width=50)
        self.historial_text.grid(row=5, column=0, columnspan=4)
        
    def sumar(self):
        self.realizar_operacion(sumar_binario, " + ")
        
    def restar(self):
        self.realizar_operacion(restar_binario, " - ")
        
    def realizar_operacion(self, operacion, simbolo): #Método para realizar la operación binaria (suma o resta) y mostrar el resultado.
        try: #Validación de entradas
            if not self.entrada_bin1.get() or not self.entrada_bin2.get(): #Verifica si las entradas están vacías
                raise ValueError("Ambas entradas son requeridas")
            bin1 = self.entrada_bin1.get()
            bin2 = self.entrada_bin2.get() 
            
            if not (validar_binario(bin1) and validar_binario(bin2)): #Validación de entradas binarias
                raise ValueError("Entradas binarias inválidas")
            
            resultado = operacion(bin1, bin2)
            dec_result = binario_a_decimal(resultado)
            
            self.mostrar_resultado(f"{bin1}{simbolo}{bin2} = {resultado} (Dec: {dec_result})")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def dec_a_bin(self):
        try:
            dec = self.entrada_decimal.get()
            if not validar_decimal(dec):
                raise ValueError("Decimal inválido")
                
            binario = decimal_a_binario(int(dec))
            self.mostrar_resultado(f"Dec {dec} → Bin {binario}")
            
        except Exception as e: #Manejo de excepciones para entradas inválidas
            messagebox.showerror("Error", str(e))
    
    def bin_a_dec(self):
        try:
            binario = self.entrada_binario.get()
            if not validar_binario(binario):
                raise ValueError("Binario inválido")
                
            decimal = binario_a_decimal(binario)
            self.mostrar_resultado(f"Bin {binario} → Dec {decimal}")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def mostrar_resultado(self, texto):
        self.resultado.config(text=texto)
        self.historial.insert(0, texto)
        self.actualizar_historial()
    
    def actualizar_historial(self):
        self.historial_text.delete(1.0, tk.END)
        self.historial_text.insert(tk.END, "\n".join(self.historial[:5]))