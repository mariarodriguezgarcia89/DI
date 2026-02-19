import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import QUrl, QDir
from PySide6.QtGui import QDesktopServices
from PySide6.QtWebEngineWidgets import QWebEngineView
import os

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Abrir informe en navegador")

        layout = QVBoxLayout()
        boton = QPushButton("Abrir informe")
        boton.clicked.connect(self.abrir_informe)
        layout.addWidget(boton)

        self.web = QWebEngineView()
        layout.addWidget(self.web)
        self.setLayout(layout)

        self.cargar_en_webengine()

    def abrir_informe(self):
        ruta_absoluta = os.path.join(os.path.dirname(__file__), "informe_ventas.html")
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))
    
    def cargar_en_webengine(self):
        ruta_absoluta = os.path.join(os.path.dirname(__file__), "informe_ventas.html")
        self.web.load(QUrl.fromLocalFile(ruta_absoluta))
        
    def abrir_en_navegador(self):
        ruta_absoluta = os.path.join(os.path.dirname(__file__), "informe_ventas.html")
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    v = Ventana()
    v.resize(1000, 800)
    v.show()
    sys.exit(app.exec())
