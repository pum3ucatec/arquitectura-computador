def sumar_binarios(bin1, bin2):
    try:
        suma = bin(int(bin1, 2) + int(bin2, 2))[2:]
        return suma
    except ValueError:
        return "Error"
