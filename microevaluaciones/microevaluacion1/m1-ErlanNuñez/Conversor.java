import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Conversor {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Conversor Numérico");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new GridLayout(5, 2, 5, 5));

        JLabel labelNumero = new JLabel("Número a convertir:");
        JTextField campoNumero = new JTextField();

        JLabel labelOrigen = new JLabel("Sistema de origen:");
        String[] opciones = {"Decimal", "Binario", "Octal", "Hexadecimal"};
        JComboBox<String> comboOrigen = new JComboBox<>(opciones);

        JLabel labelDestino = new JLabel("Sistema de destino:");
        JComboBox<String> comboDestino = new JComboBox<>(opciones);

        JButton botonConvertir = new JButton("Convertir");
        JLabel labelResultado = new JLabel("Resultado: ");

        botonConvertir.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    String numero = campoNumero.getText();
                    int opcionOrigen = comboOrigen.getSelectedIndex() + 1;
                    int numeroDecimal = convertirADecimal(numero, opcionOrigen);
                    int opcionDestino = comboDestino.getSelectedIndex() + 1;
                    String resultado = convertirDesdeDecimal(numeroDecimal, opcionDestino);
                    labelResultado.setText("Resultado: " + resultado);
                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(frame, "Error: " + ex.getMessage());
                }
            }
        });

        frame.add(labelNumero);
        frame.add(campoNumero);
        frame.add(labelOrigen);
        frame.add(comboOrigen);
        frame.add(labelDestino);
        frame.add(comboDestino);
        frame.add(botonConvertir);
        frame.add(labelResultado);

        frame.setVisible(true);
    }

    public static int convertirADecimal(String numero, int base) {
        switch (base) {
            case 1: return Integer.parseInt(numero); 
            case 2: return Integer.parseInt(numero, 2); 
            case 3: return Integer.parseInt(numero, 8); 
            case 4: return Integer.parseInt(numero, 16); 
            default: throw new IllegalArgumentException("Opción no válida");
        }
    }

    public static String convertirDesdeDecimal(int numero, int base) {
        switch (base) {
            case 1: return String.valueOf(numero); 
            case 2: return Integer.toBinaryString(numero); 
            case 3: return Integer.toOctalString(numero); 
            case 4: return Integer.toHexString(numero).toUpperCase(); 
            default: throw new IllegalArgumentException("Opción no válida");
        }
    }
}
