import sys
from PySide6.QtWidgets import QApplication
from interfaz_principal import MainWindow

def main():
    # Crear la aplicación
    app = QApplication(sys.argv)
    app.setApplicationName("Firma Digital de Documentos")
    
    # Crear y mostrar la ventana principal
    ventana = MainWindow()
    ventana.show()
    
    # Ejecutar la aplicación
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
