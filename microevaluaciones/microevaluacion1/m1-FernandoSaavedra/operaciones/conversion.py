def decimal_a_binario(n: int) -> str: 
    """Convierte decimal a binario (32 bits máximo)"""
    return bin(n)[2:].zfill(32)

def binario_a_decimal(b: str) -> int:
    """Convierte binario a decimal"""
    return int(b, 2)

def hexadecimal_a_binario(h: str) -> str:
    """Convierte hexadecimal a binario"""
    return bin(int(h, 16))[2:].zfill(len(h)*4)