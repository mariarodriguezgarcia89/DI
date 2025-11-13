import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QListWidget
from PySide6.QtCore import Qt           
from buscador import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Mini 1 – Buscador de productos")

        # Guardamos todas las etiquetas en una lista
        self.product_labels = [
            self.ui.label,
            self.ui.label_2,
            self.ui.label_3,
            self.ui.label_4,
            self.ui.label_5
        ]

        # Conectamos el cambio de texto para filtrar
        self.ui.lineEdit.textChanged.connect(self.filter_products)


    def filter_products(self, text):
        text_lower = text.lower()
        for label in self.product_labels:
            product_name = label.text().lower()
            label.setVisible(text_lower in product_name or not text_lower)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
