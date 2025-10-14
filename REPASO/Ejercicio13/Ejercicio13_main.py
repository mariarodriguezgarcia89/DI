import sys
from PySide6.QtGui import QBrush, QColor, QConicalGradient
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from ejercicio13 import Ui_MainWindow

class Ventana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.actionPlay.triggered.connect(self.play)
        self.actionPause.triggered.connect(self.pause)
        self.actionStop.triggered.connect(self.stop)
        
        self.lstPlaylist.itemDoubleClicked.connect(self.item_double_clicked)

    
    def item_double_clicked(self, item):
        self.lblTitulo.setText(f"Reproduciendo {item.text()}")


    def play(self):
        self.statusBar().showMessage("Play")

    def pause(self):
        self.statusBar().showMessage("Pause")

    def stop(self):
        self.statusBar().showMessage("Stop")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Ventana()
    w.show()
    sys.exit(app.exec())
