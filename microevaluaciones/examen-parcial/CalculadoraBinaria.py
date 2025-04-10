def es_binario(cadena):
    return all(char in '01' for char in cadena)

def pedir_binario(mensaje):
    while True:
        entrada = input(mensaje)
        if es_binario(entrada):
            return entrada
        else:
            print("❌ Entrada inválida. Ingrese solo 0 y 1.")

def suma_binaria(bin1, bin2):
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    suma = num1 + num2
    return bin(suma)[2:]

def pruebas_suma_binaria():
    print("\n🧪 Ejecutando pruebas automáticas...\n")
    pruebas = [
        ("1010", "1100", "10110"),
        ("1111", "0001", "10000"),
        ("0", "0", "0"),
        ("1", "1", "10"),
        ("100", "100", "1000"),
        ("101010", "110011", "1011101"),
        ("11111111", "1", "100000000"),
        ("1001", "111", "10000"),
        ("101", "11", "1000"),
        ("11100", "11100", "111000")
    ]
    
    for i, (b1, b2, esperado) in enumerate(pruebas, 1):
        resultado = suma_binaria(b1, b2)
        if resultado == esperado:
            print(f"✅ Prueba {i}: {b1} + {b2} = {resultado}")
        else:
            print(f"❌ Prueba {i}: {b1} + {b2} = {resultado} (esperado: {esperado})")

if __name__ == "__main__":
    print("🧮 Calculadora de Suma Binaria")
    modo = input("¿Querés usar la calculadora (c) o correr pruebas (t)? [c/t]: ").lower()

    if modo == 't':
        pruebas_suma_binaria()
    else:
        b1 = pedir_binario("Ingrese el primer número binario: ")
        b2 = pedir_binario("Ingrese el segundo número binario: ")
        resultado = suma_binaria(b1, b2)
        print(f"\n✅ La suma de {b1} + {b2} es: {resultado}")
