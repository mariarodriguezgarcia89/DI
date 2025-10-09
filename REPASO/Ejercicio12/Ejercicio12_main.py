import sys
from PySide6.QtGui import QBrush, QColor, QConicalGradient
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from ejercicio12 import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.menuVer.addAction(self.dockPlaylist.toggleViewAction())

        # Conectar las acciones personalizadas
        self.actionMostrar.triggered.connect(self.mostrar)
        self.actionOcultar.triggered.connect(self.ocultar)

        # Estado inicial
        self.actionMostrar.setEnabled(False)
        self.actionOcultar.setEnabled(True)


    def mostrar(self):
        self.dockPlaylist.show()
        self.actionMostrar.setEnabled(False)
        self.actionOcultar.setEnabled(True)

    def ocultar(self):
        self.dockPlaylist.hide()
        self.actionMostrar.setEnabled(True)
        self.actionOcultar.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ventana()
    w.show()
    sys.exit(app.exec())
