/****************************************************************
OBJETIVO: Crear una calculadora de suma de numeros binarios y decimales
AUTOR: Carlos Enrique Michel Figueroa
VERSIÓN: 1.0.0
FECHA DE CREACIÓN: 10/04/2025
******************************************************************/

document.addEventListener("DOMContentLoaded", () => {
    const titulo = document.querySelector(".header h1");
    titulo.textContent += "1.0.0";
});
document.addEventListener("DOMContentLoaded", () => {
    const titulo = document.querySelector(".footer h2");
    titulo.textContent += " Arq. Carlos Enrique Michel Figueroa";
});

function limpiar_pantalla() {
    document.getElementById("num1_bi").value = "";
    document.getElementById("num1_dec").value = ""; 
    document.getElementById("num2_bi").value = ""; 
    document.getElementById("num2_dec").value = "";
    document.getElementById("resultado").value = ""; 
    document.getElementById("resultado_dec").value = "";
}

function validar_entrada() {
    const num1_bi = document.getElementById("num1_bi").value;
    const num1_dec = document.getElementById("num1_dec").value;
    const num2_bi = document.getElementById("num2_bi").value;
    const num2_dec = document.getElementById("num2_dec").value;

    if (num1_bi === "" && num1_dec === "" && num2_bi === "" && num2_dec === "") {
        alert("Por favor, ingrese al menos un número en binario o decimal.");
        return false;
    }
    return true;
}

function verificar_binario(num) {
    const regex = /^[01]+$/;
    return regex.test(num);
}

function verificar_decimal(num) {
    const regex = /^[0-9]+$/;
    return regex.test(num);
}

// convertidor 
function convertir_a_decimal() {
    const num1_bi = document.getElementById("num1_bi").value;
    if (verificar_binario(num1_bi)) {
        const decimal = parseInt(num1_bi, 2);
        document.getElementById("num1_dec").value = decimal; // Actualiza el campo decimal
    } else if (num1_bi !== "") {
        alert("El numero binario no es valido.");
    }
}

function convertir_a_binario() {
    const num1_dec = document.getElementById("num1_dec").value;
    if (verificar_decimal(num1_dec)) {
        const binario = (parseInt(num1_dec, 10)).toString(2);
        document.getElementById("num1_bi").value = binario; // Actualiza el campo binario
    } else if (num1_dec !== "") {
        alert("El numero decimal no es valido.");
    }
}

function convertir_a_decimal_2() {
    const num2_bi = document.getElementById("num2_bi").value;
    if (verificar_binario(num2_bi)) {
        const decimal = parseInt(num2_bi, 2);
        document.getElementById("num2_dec").value = decimal; // Actualiza el campo decimal
    } else if (num2_bi !== "") {
        alert("El número binario no es válido.");
    }
}

function convertir_a_binario_2() {
    const num2_dec = document.getElementById("num2_dec").value;
    if (verificar_decimal(num2_dec)) {
        const binario = (parseInt(num2_dec, 10)).toString(2);
        document.getElementById("num2_bi").value = binario; // Actualiza el campo binario
    } else if (num2_dec !== "") {
        alert("El número decimal no es válido.");
    }
}

function sumar() {
    const num1_dec = document.getElementById("num1_dec").value;
    const num2_dec = document.getElementById("num2_dec").value;

    if (verificar_decimal(num1_dec) && verificar_decimal(num2_dec)) {
        const numero1 = parseInt(num1_dec, 10);
        const numero2 = parseInt(num2_dec, 10);

        const suma_decimal = numero1 + numero2;
        const suma_binaria = suma_decimal.toString(2);

        document.getElementById("resultado_dec").value = suma_decimal; // Muestra el resultado en decimal
        document.getElementById("resultado").value = suma_binaria; // Convierte y muestra el resultado en binario
    } else {
        alert("Por favor, ingrese numeros validos.");
    }
}

function sacarResultado() {
    if (validar_entrada()) {
        sumar();
    }
}



