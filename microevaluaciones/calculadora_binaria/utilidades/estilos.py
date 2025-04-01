from tkinter import ttk

def configurar_estilos():
    estilo = ttk.Style()
    estilo.theme_use('clam')
    
    # Configuraciones generales de estilo 
    estilo.configure('TFrame', background='#F0F0F0')
    estilo.configure('TButton', font=('Arial', 12), padding=10)
    estilo.configure('TLabel', font=('Arial', 12), background='#F0F0F0')
    estilo.configure('TEntry', font=('Courier New', 14), padding=5)
    
    # Estilos personalizados para los botones de operación
    estilo.map('Operacion.TButton',
        foreground=[('active', 'white'), ('!disabled', 'black')],
        background=[('active', '#0078D4'), ('!disabled', '#E1E1E1')]
    )