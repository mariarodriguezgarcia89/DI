# producto.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Producto(QWidget):
    def __init__(self, nombre, precio):
        super().__init__()  # inicializar correctamente QWidget

        # Atributos privados
        self._nombre = nombre
        self._precio = precio

        # Crear las etiquetas privadas
        self._label_nombre = QLabel(self._nombre)
        self._label_precio = QLabel(f"{self._precio:.2f} €")

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self._label_nombre)
        layout.addWidget(self._label_precio)
        self.setLayout(layout)

    # --- Propiedad nombre ---
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
        self._label_nombre.setText(valor)  # corregido con _label_nombre

    # --- Propiedad precio ---
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        self._precio = valor
        self._label_precio.setText(f"{valor:.2f} €")  # corregido con _label_precio
