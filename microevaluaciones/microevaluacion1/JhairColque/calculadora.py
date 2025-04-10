# Función para convertir un número de base A a base 10
def a_decimal(numero, base_a):
    return int(numero, base_a)

# Función para convertir un número decimal a base B
def de_decimal_a_base(decimal, base_b):
    resultado = ""
    while decimal > 0:
        residuo = decimal % base_b
        resultado = str(residuo) + resultado
        decimal = decimal // base_b
    return resultado or "0"

# Programa principal
numero = input("Ingresa el número a convertir: ")
base_a = int(input("Ingresa la base del número (base A): "))
base_b = int(input("Ingresa la base a la que deseas convertir (base B): "))

# Conversión
decimal = a_decimal(numero, base_a)
resultado = de_decimal_a_base(decimal, base_b)

# Resultado
print(f"El número {numero} en base {base_a} es {resultado} en base {base_b}.")
