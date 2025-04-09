def operacion_logica(a: str, b: str, operador: str) -> str: #Función base para operaciones lógicas
    """Función base para operaciones lógicas"""
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    ops = { 
        'AND': lambda x, y: x & y, 
        'OR': lambda x, y: x | y,
        'XOR': lambda x, y: x ^ y
    }
    
    return ''.join(
        str(ops[operador](int(a_bit), int(b_bit)))
        for a_bit, b_bit in zip(a, b)
    )

def and_binario(a: str, b: str) -> str: 
    return operacion_logica(a, b, 'AND')

def or_binario(a: str, b: str) -> str:
    return operacion_logica(a, b, 'OR')

def xor_binario(a: str, b: str) -> str:
    return operacion_logica(a, b, 'XOR')

def not_binario(a: str) -> str:
    return ''.join('1' if bit == '0' else '0' for bit in a)