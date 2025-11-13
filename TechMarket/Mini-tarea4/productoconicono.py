from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QSizePolicy
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import resources_rc

class ProductoConIcono(QWidget):
    def __init__(self, nombre, precio, icono_path):
        super().__init__()
        imagen = QLabel()
        pixmap = QPixmap(icono_path)
        imagen.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        imagen.setAlignment(Qt.AlignCenter)

        nombre_label = QLabel(nombre)
        nombre_label.setAlignment(Qt.AlignCenter)
        nombre_label.setFont(QFont("Arial", 12, QFont.Bold))

        precio_label = QLabel(f"{precio:.2f} €")
        precio_label.setAlignment(Qt.AlignCenter)
        precio_label.setFont(QFont("Arial", 10))

        layout = QVBoxLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(5,5,5,5)
        layout.addWidget(imagen)
        layout.addWidget(nombre_label)
        layout.addWidget(precio_label)
        self.setLayout(layout)

        # Evita que el widget se estire
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Productos con icono")

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignTop)  # importante

        p1 = ProductoConIcono("Portátil ZenAir", 799, "icons/laptop.png")
        p2 = ProductoConIcono("Ratón Ergonomic", 25, "icons/mouse.png")
        p3 = ProductoConIcono("Teclado Gamer RGB", 99, "icons/keyboard.png")

        layout.addWidget(p1)
        layout.addWidget(p2)
        layout.addWidget(p3)
        layout.addStretch()  # empuja todo hacia arriba

        self.setCentralWidget(central)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
