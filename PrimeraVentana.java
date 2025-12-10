import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class PrimeraGUI {

    public static void main(String[] args) {
        // Crear el frame principal
        JFrame frame = new JFrame("Mi primera GUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 150); // Tamaño de la ventana

        // Crear un panel con FlowLayout
        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());

        // Crear los componentes
        JLabel label = new JLabel("Escribe tu nombre:");
        JTextField textField = new JTextField(20); // campo de texto de 20 columnas
        JButton boton = new JButton("Saludar");

        // Agregar los componentes al panel
        panel.add(label);
        panel.add(textField);
        panel.add(boton);

        // Agregar el panel al frame
        frame.add(panel);

        // Hacer visible la ventana
        frame.setVisible(true);

        // Acción del botón
        boton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nombre = textField.getText().trim();
                if (nombre.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Error: el campo está vacío.",
                            "Error", JOptionPane.ERROR_MESSAGE);
                } else {
                    JOptionPane.showMessageDialog(frame,
                            "Hola, " + nombre + "! Bienvenido/a a tu primera GUI en Java.");
                }
            }
        });
    }
}
