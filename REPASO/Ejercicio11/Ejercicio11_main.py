import sys
from PySide6.QtGui import QBrush, QColor, QConicalGradient
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from ejercici11 import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        QTimer.singleShot(0, lambda: self.statusBar().showMessage("Listo", 5000))  # Mensaje inmediato

        label_normal = QLabel("Soy un label normal")
        label_permanente = QLabel("Soy un label permanente")

        self.statusBar().addPermanentWidget(label_permanente)
        self.statusBar().addWidget(label_normal)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ventana()
    w.show()
    sys.exit(app.exec())
