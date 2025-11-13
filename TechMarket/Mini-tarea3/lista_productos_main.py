import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QListWidget, QVBoxLayout, QWidget, QListWidgetItem
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini 3 – Lista de productos")

        # Crear widget central y layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Crear campo de búsqueda manualmente
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Buscar producto...")
        layout.addWidget(self.lineEdit)

        # Crear lista
        self.listWidget = QListWidget()
        layout.addWidget(self.listWidget)

        # Agregar productos de ejemplo
        productos = [
            "Ratón Óptico Pro - 19.99 €",
            "Teclado Mecánico X - 49.99 €",
            "Monitor HD 24\" - 129.99 €",
            "Auriculares Inalámbricos - 39.99 €",
            "Webcam Full HD - 59.99 €"
        ]
        for producto in productos:
            self.listWidget.addItem(QListWidgetItem(producto))

        # Conectar el filtro
        self.lineEdit.textChanged.connect(self.filter_products)

    def filter_products(self, text):
        text_lower = text.lower()
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            visible = text_lower in item.text().lower() or not text_lower
            item.setHidden(not visible)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
