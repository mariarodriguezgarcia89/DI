import sys
from PySide6.QtGui import QBrush, QColor, QConicalGradient
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from ejercicio10 import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionAbrir.triggered.connect(self.abrir)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionSalir.triggered.connect(self.close)

    def abrir(self):
        self.actionAbrir.setStatusTip("Abrir un archivo")
        print("Abrir archivo")
   

    def guardar(self):
        self.actionGuardar.setStatusTip("Guardar el archivo")
        print("Guardar archivo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ventana()
    w.show()
    sys.exit(app.exec())
