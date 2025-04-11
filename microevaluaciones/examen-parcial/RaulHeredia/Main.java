
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main {
    public static void main(String[] args) {
        // Crear y mostrar la interfaz gráfica
        SwingUtilities.invokeLater(() -> {
            SumaBinariaGUI app = new SumaBinariaGUI();
            app.setVisible(true);
        });
    }
}

// Clase para la lógica de la suma binaria
class SumaBinariaLogic {

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

// Clase para la interfaz gráfica
class SumaBinariaGUI extends JFrame {
    private JTextField campoBinario1;
    private JTextField campoBinario2;
    private JTextField campoResultado;
    private JButton botonSumar;

    private final SumaBinariaLogic logica; // Instancia de la lógica

    public SumaBinariaGUI() {
        // Inicializar la lógica
        logica = new SumaBinariaLogic();

        // Configuración básica de la ventana
        setTitle("Suma Binaria");
        setSize(400, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(4, 2, 10, 10));
        setLocationRelativeTo(null);

        // Componentes de la interfaz
        add(new JLabel("Número Binario 1:"));
        campoBinario1 = new JTextField();
        add(campoBinario1);

        add(new JLabel("Número Binario 2:"));
        campoBinario2 = new JTextField();
        add(campoBinario2);

        botonSumar = new JButton("Sumar");
        add(botonSumar);

        add(new JLabel("Resultado (Binario):"));
        campoResultado = new JTextField();
        campoResultado.setEditable(false); // Solo lectura
        add(campoResultado);

        // Acción del botón
        botonSumar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String binario1 = campoBinario1.getText().trim();
                String binario2 = campoBinario2.getText().trim();

                // Validar que los números sean binarios
                if (!logica.esBinarioValido(binario1) || !logica.esBinarioValido(binario2)) {
                    JOptionPane.showMessageDialog(SumaBinariaGUI.this,
                            "Por favor, ingrese números binarios válidos (solo 0s y 1s).",
                            "Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }

                // Realizar la suma usando la lógica
                String resultadoBinario = logica.sumarBinarios(binario1, binario2);

                // Mostrar el resultado
                campoResultado.setText(resultadoBinario);
            }
        });
    }
}