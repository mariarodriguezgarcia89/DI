import sys
from PySide6.QtGui import QBrush, QColor, QConicalGradient
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout
from ejercicio8 import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Crear un layout para organizar TODOS los elementos
        layout_principal = QVBoxLayout(self.centralwidget)  # Usar el centralwidget existente
        # Agregar espacio en la parte superior
        layout_principal.addStretch()
        # Agregar el stackedWidget centrado
        layout_principal.addWidget(self.stackedWidget)
        
        # Crear un layout horizontal para los botones
        layout_botones = QHBoxLayout()
        layout_botones.addStretch()
        layout_botones.addWidget(self.btn1)
        layout_botones.addWidget(self.btn2)
        layout_botones.addWidget(self.btn3)
        layout_botones.addStretch()
        
        # Agregar el layout de botones al layout principal
        layout_principal.addLayout(layout_botones)
        
        # Agregar espacio en la parte inferior
        layout_principal.addStretch()

        # Botones
        self.btn1.clicked.connect(self.on_click)
        self.btn2.clicked.connect(self.on_click)
        self.btn3.clicked.connect(self.on_click)


    def on_click(self):
        sender = self.sender()
        if sender == self.btn1:
             self.stackedWidget.setCurrentIndex(0)
        elif sender == self.btn2:
                self.stackedWidget.setCurrentIndex(1)
        elif sender == self.btn3:
                self.stackedWidget.setCurrentIndex(2)   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ventana()
    w.show()
    sys.exit(app.exec())
