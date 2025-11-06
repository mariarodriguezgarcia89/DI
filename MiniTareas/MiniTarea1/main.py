import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from t1_switch import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Aplicar estilo de switch
        self.apply_switch_style()
        
    def apply_switch_style(self):
        self.ui.chkSwitch.setStyleSheet("""
        QCheckBox::indicator { width: 46px; height: 24px; }
        QCheckBox::indicator:unchecked { border-radius: 12px; background:#ccc; }
        QCheckBox::indicator:checked { border-radius: 12px; background:#2ecc71; }
        """)
        self.ui.chkSwitch.toggled.connect(lambda s: self.ui.chkSwitch.setText("ON" if s else "OFF"))
        # Establecer el texto inicial según el estado actual
        self.ui.chkSwitch.setText("OFF")  # Esto fuerza el texto a "OFF"
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
