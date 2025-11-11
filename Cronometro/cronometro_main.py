import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from cronometro_ui import CronometroWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cronómetro")
        self.cronometro_widget = CronometroWidget()
        self.setCentralWidget(self.cronometro_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
