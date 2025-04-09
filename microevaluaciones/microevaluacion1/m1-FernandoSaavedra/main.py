from src.app import iniciar_aplicacion # Importar la función iniciar_aplicacion desde el módulo app

if __name__ == "__main__":
    iniciar_aplicacion()
    import sys 
import os  


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Añadir el directorio padre al path para importar módulos desde allí

from src.app import iniciar_aplicacion




