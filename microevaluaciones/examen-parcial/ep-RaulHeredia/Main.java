
import gui.SumaBinariaGUI;
import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // Crear y mostrar la interfaz gráfica
        SwingUtilities.invokeLater(() -> {
            SumaBinariaGUI app = new SumaBinariaGUI();
            app.setVisible(true);
        });
    }
}
