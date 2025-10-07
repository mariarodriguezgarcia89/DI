import sys
from PySide6.QtGui import QBrush, QColor, QConicalGradient
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from ejercicio4 import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Centrar el layout verticalmente y horizontalmente
        widget_central = QWidget()
        layout_centrado = QVBoxLayout(widget_central)
        layout_centrado.addStretch()
        layout_centrado.addWidget(self.verticalLayoutWidget) 
        layout_centrado.addStretch()

        # Asignar el layout al centro
        self.setCentralWidget(widget_central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ventana()
    w.show()
    sys.exit(app.exec())
