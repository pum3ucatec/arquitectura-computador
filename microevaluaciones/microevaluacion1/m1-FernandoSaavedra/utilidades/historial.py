import json # Utilidad para manejar el historial de operaciones
from datetime import datetime # Librería para manejar fechas y horas

ARCHIVO_HISTORIAL = "historial.json"

def guardar_operacion(operacion: str, resultado: str):
    registro = {
        'fecha': datetime.now().isoformat(),
        'operacion': operacion,
        'resultado': resultado
    }
    
    try:
        with open(ARCHIVO_HISTORIAL, 'r') as f:
            datos = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        datos = []
    
    datos.append(registro)
    
    with open(ARCHIVO_HISTORIAL, 'w') as f:
        json.dump(datos, f, indent=2)

def cargar_historial() -> list:
    try:
        with open(ARCHIVO_HISTORIAL, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []