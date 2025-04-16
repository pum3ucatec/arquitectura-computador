import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraBinaria {
    private JFrame frame;
    private JTextField textField;
    private String operacion = "";
    
    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            try {
                CalculadoraBinaria window = new CalculadoraBinaria();
                window.frame.setVisible(true);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    public CalculadoraBinaria() {
        frame = new JFrame("Calculadora Binaria");
        frame.setBounds(100, 100, 350, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().setLayout(null);

        textField = new JTextField();
        textField.setFont(new Font("Tahoma", Font.PLAIN, 20));
        textField.setBounds(10, 10, 310, 50);
        frame.getContentPane().add(textField);
        textField.setColumns(10);

        String[] botones = {
            "0", "1", "+", "-", "=", "C"
        };
        
        int x = 10, y = 70;
        for (int i = 0; i < botones.length; i++) {
            JButton button = new JButton(botones[i]);
            button.setFont(new Font("Tahoma", Font.PLAIN, 20));
            button.setBounds(x, y, 60, 60);
            frame.getContentPane().add(button);
            x += 70;
            if ((i + 1) % 3 == 0) {
                x = 10;
                y += 70;
            }

            button.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    String command = e.getActionCommand();

                    if (command.equals("C")) {
                        textField.setText("");
                        operacion = "";
                    } else if (command.equals("=")) {
                        try {
                            String[] operands = operacion.split("[-+]");
                            String operador = operacion.replaceAll("[0-1]", "");
                            int num1 = Integer.parseInt(operands[0], 2);
                            int num2 = Integer.parseInt(operands[1], 2);
                            int resultado = 0;

                            if (operador.equals("+")) {
                                resultado = num1 + num2;
                            } else if (operador.equals("-")) {
                                resultado = num1 - num2;
                            }
                            textField.setText(Integer.toBinaryString(resultado));
                        } catch (Exception ex) {
                            textField.setText("Error");
                        }
                    } else {
                        operacion += command;
                        textField.setText(operacion);
                    }
                }
            });
        }
    }
}
