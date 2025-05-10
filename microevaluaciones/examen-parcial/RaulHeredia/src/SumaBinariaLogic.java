package src;

// Clase para la lógica de la suma binaria
public class SumaBinariaLogic {

    // Método para validar si una cadena es un número binario válido
    public boolean esBinarioValido(String numero) {
        for (char c : numero.toCharArray()) {
            if (c != '0' && c != '1') {
                return false;
            }
        }
        return !numero.isEmpty(); // No debe estar vacío
    }

    // Método para sumar dos números binarios
    public String sumarBinarios(String binario1, String binario2) {
        // Convertir los números binarios a enteros
        int numero1 = Integer.parseInt(binario1, 2);
        int numero2 = Integer.parseInt(binario2, 2);

        // Realizar la suma
        int suma = numero1 + numero2;

        // Convertir el resultado a binario
        return Integer.toBinaryString(suma);
    }
}
