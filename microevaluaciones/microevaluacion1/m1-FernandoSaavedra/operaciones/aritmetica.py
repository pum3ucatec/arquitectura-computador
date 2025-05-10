def sumar_binario(a: str, b: str) -> str: #Función para sumar dos números binarios
    max_len = max(len(a), len(b)) #Encuentra la longitud máxima de los dos números binarios
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    resultado = [] #Lista para almacenar el resultado
    carry = 0
    
    for i in range(max_len-1, -1, -1): #Itera desde el último bit hasta el primero
        bit_a = int(a[i]) #Convierte el bit a entero
        bit_b = int(b[i])
        suma = bit_a + bit_b + carry
        resultado.append(str(suma % 2))
        carry = suma // 2
    
    if carry != 0:
        resultado.append(str(carry))
        
    return ''.join(reversed(resultado))

def restar_binario(a: str, b: str) -> str: #Función para restar dos números binarios
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    resultado = []
    prestamo = 0
    
    for i in range(max_len-1, -1, -1): #Itera desde el último bit hasta el primero
        bit_a = int(a[i]) #Convierte el bit a entero
        bit_b = int(b[i]) 
        
        if prestamo:
            bit_a -= 1
            prestamo = 0
            
        if bit_a < bit_b:
            bit_a += 2
            prestamo = 1
            
        resultado.append(str(bit_a - bit_b))
    
    return ''.join(reversed(resultado)).lstrip('0') or '0'