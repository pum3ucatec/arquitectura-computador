using System;
using System.Numerics;

namespace p1_conversor.Models
{
    public class BaseConverter
    {
        public string Number { get; set; }
        public int FromBase { get; set; } = 10;
        public int ToBase { get; set; } = 2;

        public string Convert()
        {
            if (string.IsNullOrWhiteSpace(Number))
                return "Ingrese un número válido";

            if (FromBase < 2 || FromBase > 36 || ToBase < 2 || ToBase > 36)
                return "Las bases deben estar entre 2 y 36";

            try
            {
                // Convertir el número a decimal desde cualquier base (2 a 36)
                BigInteger decimalValue = ConvertToDecimal(Number, FromBase);

                // Convertir de decimal a la base deseada
                return ConvertFromDecimal(decimalValue, ToBase);
            }
            catch (FormatException)
            {
                return $"El número '{Number}' no es válido en la base {FromBase}";
            }
            catch (OverflowException)
            {
                return "Número demasiado grande para convertir";
            }
            catch (Exception ex)
            {
                return $"Error inesperado: {ex.Message}";
            }
        }

        private BigInteger ConvertToDecimal(string number, int fromBase)
        {
            const string chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            BigInteger result = 0;
            foreach (char c in number.ToUpper())
            {
                int value = chars.IndexOf(c);
                if (value == -1 || value >= fromBase)
                    throw new FormatException($"Carácter inválido '{c}' para la base {fromBase}");

                result = result * fromBase + value;
            }
            return result;
        }

        private string ConvertFromDecimal(BigInteger number, int toBase)
        {
            const string chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            if (number == 0) return "0";

            string result = "";
            while (number > 0)
            {
                result = chars[(int)(number % toBase)] + result;
                number /= toBase;
            }

            return result;
        }
    }
}
