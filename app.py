import sys

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from saludo import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnCambiar.clicked.connect(self.on_cambiar)
        print("Hola, que tal")

    def on_cambiar(self):
        self.textVentana.setText('HOLA!')
        self.textVentana.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        print("Has pulsado el botón")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ventana()
    w.show()
    sys.exit(app.exec())  # en PySide6 es .exec(), no .exec_()

