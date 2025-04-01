## TEMA 1

# INTRODUCCION A LA ELECTRONICA DIGITAL


# 1.- REPRESENTACIÓN NUMÉRICA EN COMPUTACIÓN

## 🔢 SISTEMAS NUMÉRICOS

 **BINARIO (Base 2)**  
   - Dígitos: 0, 1  
   - Ejemplo: 1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11₁₀  

 **OCTAL (Base 8)**  
   - Dígitos: 0-7  
   - Ejemplo: 34₈ = 3×8¹ + 4×8⁰ = 24 + 4 = 28₁₀  

 **DECIMAL (Base 10)**  
   - Dígitos: 0-9  
   - Conversión a binario:  
     25 ÷ 2 = 12 (1)  
     12 ÷ 2 = 6 (0)  
     6 ÷ 2 = 3 (0)  
     3 ÷ 2 = 1 (1)  
     1 ÷ 2 = 0 (1) → 11001₂  

 **HEXADECIMAL (Base 16)**  
   - Dígitos: 0-9, A-F  
   - Ejemplos:  
     - A3₁₆ = 10×16 + 3 = 163₁₀  
     - 45₁₀ → 2D₁₆ (45÷16=2 resto 13(D), 2÷16=0 resto 2)  

## 🔄 CONVERSIONES RÁPIDAS

- Binario → Octal: Agrupar de 3 en 3 bits  
  `110101₂ → 110 101 → 65₈`  
- Binario → Hex: Agrupar de 4 en 4 bits  
  `11011010₂ → 1101 1010 → DA₁₆`  

## 📊 TABLA COMPARATIVA

| Sistema | Base | Dígitos | Ejemplo | Aplicación |
|---------|------|---------|---------|------------|
| Binario | 2 | 0,1 | 1011₂ | Operaciones CPU |
| Octal | 8 | 0-7 | 34₈ | Permisos Linux |
| Decimal | 10 | 0-9 | 25₁₀ | Uso diario |
| Hexadecimal | 16 | 0-F | A3₁₆ | Memoria/Colores |

## 📝 EJERCICIOS RESUELTOS

1. 110101₂ → 32 + 16 + 4 + 1 = 53₁₀  
2. 27₁₀ → Binario: 11011₂, Hex: 1B₁₆  
3. 3F₁₆ → 3×16 + 15 = 63₁₀  

## 💡 APLICACIONES PRÁCTICAS

- Binario: Lenguaje máquina (ej: 1011b)  
- Octal: chmod 755 (permisos archivos)  
- Hex: #FFFFFF (colores web), 0x7FFF (direcciones memoria)  

