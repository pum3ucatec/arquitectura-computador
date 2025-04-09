def validar_binario(binario: str) -> bool: #Validación de entradas binarias para verificar si es binario o no
    return all(c in '01' for c in binario) and len(binario) > 0

def validar_decimal(decimal: str) -> bool: #Validación de entradas decimales para verificar si es decimal o no
    return decimal.isdigit()