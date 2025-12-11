import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class VentanaConColores extends JFrame {

    private JPanel panel;

    public VentanaConColores() {
        // Configuración de la ventana
        setTitle("Cambiar Color del Panel");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // Centrar ventana

        // Crear panel principal
        panel = new JPanel();
        panel.setBackground(Color.WHITE); // Color inicial
        panel.setLayout(new FlowLayout());

        // Crear botones
        JButton btnRojo = new JButton("Rojo");
        JButton btnVerde = new JButton("Verde");
        JButton btnAzul = new JButton("Azul");

        // Agregar ActionListener a los botones
        btnRojo.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                panel.setBackground(Color.RED);
            }
        });

        btnVerde.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                panel.setBackground(Color.GREEN);
            }
        });

        btnAzul.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                panel.setBackground(Color.BLUE);
            }
        });

        // Agregar botones al panel
        panel.add(btnRojo);
        panel.add(btnVerde);
        panel.add(btnAzul);

        // Agregar panel a la ventana
        add(panel);

        setVisible(true);
    }

    public static void main(String[] args) {
        new VentanaConColores();
    }
}
