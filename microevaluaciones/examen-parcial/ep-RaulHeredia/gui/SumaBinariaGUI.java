package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import src.SumaBinariaLogic; // Importar la lógica de suma binaria

// Clase para la interfaz gráfica
public class SumaBinariaGUI extends JFrame {
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
