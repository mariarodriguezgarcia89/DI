# demo_producto.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from producto import Producto

class DemoProducto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 2 – Componente Producto")

        # Crear un widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout vertical
        layout = QVBoxLayout(central_widget)

        # Crear instancia de Producto
        self.producto = Producto("Ratón Óptico Pro", 19.99)
        layout.addWidget(self.producto)

        # Botón para actualizar el precio
        self.boton = QPushButton("Actualizar precio")
        self.boton.clicked.connect(self.actualizar_precio)
        layout.addWidget(self.boton)

    def actualizar_precio(self):
        # Cambia el precio → el QLabel se actualiza automáticamente
        self.producto.precio = 14.99


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DemoProducto()
    ventana.show()
    sys.exit(app.exec())
