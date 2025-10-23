import sys
from PySide6.QtWidgets import QProgressDialog, QApplication, QMainWindow, QDialog, QWidget, QMessageBox, QFileDialog, QColorDialog, QLabel, QVBoxLayout, QFontDialog, QInputDialog
from PySide6.QtCore import Qt, QTimer
from mainwindow import Ui_MainWindow
from dialogo1 import Ui_DialogNuevoProyecto
from dialogo2 import Ui_DialogConfirmar

class DialogoProyecto(QDialog, Ui_DialogNuevoProyecto):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btnBoxIntroduce.accepted.connect(self.accept)
        self.btnBoxIntroduce.rejected.connect(self.reject)
        print("Diálogo Nuevo Proyecto inicializado")  

class ConfirmarProyecto(QDialog, Ui_DialogConfirmar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.DialogBoxConfirmar.accepted.connect(self.accept)
        self.DialogBoxConfirmar.rejected.connect(self.reject)
        print("Diálogo Confirmar inicializado")  

class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("Ventana principal inicializada")  

        self.mi_label = QLabel("PREFERENCIAS", self.centralwidget)
        self.mi_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.mi_label.setWordWrap(True)
        self.mi_label.setStyleSheet("font-size: 16px; color: black;")
        self.mi_label.setGeometry(10, 10, 600, 80)
        self.mi_label.show()

        self.btnNuevoProyecto.clicked.connect(self.abrir_nuevo_proyecto)
        self.btnConfirmar.clicked.connect(self.abrir_confirmar)
        self.btnCentroMens.clicked.connect(self.abrir_centro_mensajes)
        self.btnPref.clicked.connect(self.abrir_preferencias)  
        self.bntExport.clicked.connect(self.exportar_datos) 

    def exportar_datos(self):
        print("Iniciando proceso de exportación...")  # ✅ NUEVO
        self.statusBar().showMessage("Preparando exportación...", 2000)  # ✅ NUEVO
        
        progreso = QProgressDialog("Exportando informe...", "Cancelar", 0, 100, self)
        progreso.setWindowTitle("Exportar Informe")
        progreso.setWindowModality(Qt.WindowModal)
        progreso.setMinimumDuration(0)

        self.valor_progreso = 0
        self.timer_exportacion = QTimer()
    
        def actualizar():
            self.valor_progreso += 1
            progreso.setValue(self.valor_progreso)
            
            # ✅ NUEVO: Mensajes durante el progreso
            if self.valor_progreso % 20 == 0:  # Cada 20%
                mensaje = f"Exportación en progreso: {self.valor_progreso}%"
                print(mensaje)
                self.statusBar().showMessage(mensaje, 1000)
            
            if self.valor_progreso >= 100:
                self.timer_exportacion.stop()
                if not progreso.wasCanceled():
                    print("Exportación completada al 100%")  # ✅ NUEVO
                    self.statusBar().showMessage("Exportación completada", 3000)  # ✅ NUEVO
                    QMessageBox.information(self, "Éxito", "Exportación finalizada correctamente")
    
        def cancelar():
            self.timer_exportacion.stop()
            print("Exportación cancelada por el usuario")  # ✅ NUEVO
            self.statusBar().showMessage("Exportación cancelada", 3000)  
            QMessageBox.warning(self, "Cancelado", "Exportación cancelada por el usuario")
    
        progreso.canceled.connect(cancelar)
        self.timer_exportacion.timeout.connect(actualizar)      
        
        # Iniciar la simulación
        self.valor_progreso = 0
        self.timer_exportacion.start(50)
        print("Timer de exportación iniciado")  
        
        progreso.show()   

    def abrir_preferencias(self):
        print("Abriendo diálogo de preferencias...")  
        self.statusBar().showMessage("Abriendo preferencias...", 2000)  
        
        ruta = QFileDialog.getExistingDirectory(self, "Selecciona el directorio de trabajo", "/home")    
        print(f"Directorio seleccionado: {ruta}")  

        color_actual = self.mi_label.palette().color(self.mi_label.foregroundRole())
        color = QColorDialog.getColor(color_actual, self, "Selecciona un color para el texto")

        if color.isValid():
            self.mi_label.setStyleSheet(f"color: {color.name()}; font-size: 16px;")
            QMessageBox.information(self, "Color seleccionado", f"Has cambiado el color del texto a {color.name()}")
            print(f"Color elegido: {color.name()}")
            self.statusBar().showMessage(f"Color cambiado a {color.name()}", 3000)  
        else:
            print("No se seleccionó ningún color.")
            self.statusBar().showMessage("Color no cambiado", 2000)  

        dialogo_fuente = QFontDialog(self)
        dialogo_fuente.setCurrentFont(self.mi_label.font())
        
        if dialogo_fuente.exec():
            fuente = dialogo_fuente.currentFont()
            self.mi_label.setFont(fuente)
            print(f"Fuente elegida: {fuente.family()} {fuente.pointSize()} pt")
            self.statusBar().showMessage(f"Fuente cambiada a {fuente.family()}", 3000)  
        else:
            print("No se seleccionó ninguna fuente.")
            self.statusBar().showMessage("Fuente no cambiada", 2000)  

        texto, ok = QInputDialog.getText(self, "Input", "Introduce tu nombre de usuario:")
        
        if ok and texto:
            nombre_usuario = texto
            print(f"Nombre de usuario introducido: {nombre_usuario}")  
            self.statusBar().showMessage(f"Usuario: {nombre_usuario}", 3000)  
        else: 
            nombre_usuario = "Sin nombre"
            print("No se introdujo nombre de usuario")  
            
        self.mi_label.setText(f"PREFERENCIAS - Usuario: {nombre_usuario}, Color: {color.name()}, Fuente: {fuente.family()}  {fuente.pointSize()} pt, ruta: {ruta}")
        print("Preferencias actualizadas correctamente")  

    def abrir_centro_mensajes(self):
        print("Abriendo centro de mensajes...")  
        self.statusBar().showMessage("Mostrando mensajes...", 2000)  
        
        QMessageBox.information(self, "Information", "Operación completada con éxito.")
        print("Mensaje de información mostrado")  
        
        QMessageBox.warning(self, "Warning", "Estás a punto de sobrescribir un archivo existente.")
        print("Mensaje de advertencia mostrado")  
        
        QMessageBox.critical(self, "Critical", "Error grave en el proceso de guardado")
        print("Mensaje crítico mostrado")  
        
        respuesta = QMessageBox.question(self, "Question", "¿Deseas continuar con la operación?")
        print("Mensaje de pregunta mostrado")  

        if respuesta == QMessageBox.StandardButton.Yes: 
            print("El usuario eligió Sí")
            self.statusBar().showMessage("Usuario confirmó la operación", 3000)  
        else:
            print("El usuario eligió No")
            self.statusBar().showMessage("Usuario canceló la operación", 3000)  

    def abrir_confirmar(self):
        print("Abriendo diálogo de confirmación...")  
        self.statusBar().showMessage("Solicitando confirmación...", 2000)  
        
        dialogo = ConfirmarProyecto(self)
        
        if dialogo.exec():
            self.statusBar().showMessage("Acción confirmada", 3000)
            print("Datos eliminados")
        else:
            self.statusBar().showMessage("Operación abortada por el usuario", 3000)
            print("Usuario canceló la eliminación")  

    def abrir_nuevo_proyecto(self):
        print("Abriendo diálogo de nuevo proyecto...")  
        self.statusBar().showMessage("Creando nuevo proyecto...", 2000)  
        
        dialogo = DialogoProyecto(self)
        
        if dialogo.exec():
            nombre = dialogo.lineIntroduce.text()
            QMessageBox.information(self, "Éxito", f"Proyecto {nombre} creado correctamente.")
            print(f"Proyecto '{nombre}' creado exitosamente")  
            self.statusBar().showMessage(f"Proyecto '{nombre}' creado", 3000)  
        else:
            self.statusBar().showMessage("Operación cancelada", 3000)
            print("Creación de proyecto cancelada")  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("Aplicación iniciada")  
    ventana = VentanaPrincipal()
    ventana.show()
    print("Ventana principal mostrada")  
    sys.exit(app.exec())
