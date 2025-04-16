# suma_binaria.py

def suma_binaria(bin1, bin2):
    suma = bin(int(bin1, 2) + int(bin2, 2))
    return suma[2:]  # quitamos el '0b' del inicio

if __name__ == "__main__":
    b1 = input("Ingresa el primer número binario: ")
    b2 = input("Ingresa el segundo número binario: ")
    resultado = suma_binaria(b1, b2)
    print(f"La suma binaria es: {resultado}")
