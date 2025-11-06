import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
# IMPORTANTE: importa el módulo generado por pyside6-rcc 
import recursos_rc  # <-- esto registra :/icons/...

app = QApplication(sys.argv)

# Cargar la interfaz desde el archivo .ui
loader = QUiLoader()
f = QFile("interfaz.ui")

if not f.exists():
    print("Error: No se encuentra el archivo interfaz.ui")
    sys.exit(1)

if f.open(QFile.ReadOnly):
    w = loader.load(f)
    f.close()
    
    if w is not None:
        w.show()
        sys.exit(app.exec())
    else:
        print("Error: No se pudo cargar la interfaz desde interfaz.ui")
else:
    print("Error: No se pudo abrir el archivo interfaz.ui")
