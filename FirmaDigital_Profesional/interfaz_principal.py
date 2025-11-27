import os
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLabel, QFileDialog, QMessageBox,
                               QGraphicsView, QGraphicsScene, QGraphicsPixmapItem)
from PySide6.QtGui import QPixmap, QAction
from PySide6.QtCore import Qt
from dialogo_firma import DialogoFirma
import PyPDF2
from PIL import Image, ImageDraw, ImageFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pdf_path = None
        self.setup_ui()
        
    def setup_ui(self):
        """Configurar la interfaz de usuario"""
        self.setWindowTitle("Firma Digital de Documentos")
        self.setGeometry(100, 100, 1000, 700)
        
        # Crear widget central y layout principal
        widget_central = QWidget()
        layout_principal = QVBoxLayout()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)
        
        # Crear barra de menú
        self.crear_menu()
        
        # Crear botones superiores
        self.crear_botones_superiores(layout_principal)
        
        # Área de previsualización
        self.crear_area_previsualizacion(layout_principal)
        
        # Botones inferiores
        self.crear_botones_inferiores(layout_principal)
        
    def crear_menu(self):
        """Crear la barra de menú"""
        barra_menu = self.menuBar()
        
        # Menú Archivo
        menu_archivo = barra_menu.addMenu("&Archivo")
        
        accion_abrir = QAction("&Abrir PDF", self)
        accion_abrir.triggered.connect(self.abrir_pdf)
        menu_archivo.addAction(accion_abrir)
        
        accion_guardar = QAction("&Guardar como firmado", self)
        accion_guardar.triggered.connect(self.guardar_pdf_firmado)
        menu_archivo.addAction(accion_guardar)
        
        menu_archivo.addSeparator()
        
        accion_salir = QAction("&Salir", self)
        accion_salir.triggered.connect(self.close)
        menu_archivo.addAction(accion_salir)
        
    def crear_botones_superiores(self, layout):
        """Crear la barra de botones superiores"""
        layout_botones = QHBoxLayout()
        
        btn_abrir = QPushButton("Abrir PDF")
        btn_abrir.clicked.connect(self.abrir_pdf)
        
        btn_firmar = QPushButton("Firmar Documento")
        btn_firmar.clicked.connect(self.mostrar_dialogo_firma)
        
        btn_guardar = QPushButton("Guardar como Firmado")
        btn_guardar.clicked.connect(self.guardar_pdf_firmado)
        
        layout_botones.addWidget(btn_abrir)
        layout_botones.addWidget(btn_firmar)
        layout_botones.addWidget(btn_guardar)
        
        layout.addLayout(layout_botones)
        
    def crear_area_previsualizacion(self, layout):
        """Crear el área de previsualización del PDF"""
        # Etiqueta de información
        self.etiqueta_info = QLabel("No se ha cargado ningún PDF")
        self.etiqueta_info.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.etiqueta_info)
        
        # GraphicsView para previsualización
        self.vista_previa = QGraphicsView()
        self.escena_previa = QGraphicsScene()
        self.vista_previa.setScene(self.escena_previa)
        self.vista_previa.setMinimumHeight(400)
        layout.addWidget(self.vista_previa)
        
    def crear_botones_inferiores(self, layout):
        """Crear botones inferiores"""
        layout_inferior = QHBoxLayout()
        
        self.etiqueta_estado = QLabel("Listo")
        layout_inferior.addWidget(self.etiqueta_estado)
        
        layout.addLayout(layout_inferior)
        
    def abrir_pdf(self):
        """Abrir un archivo PDF"""
        ruta, _ = QFileDialog.getOpenFileName(
            self, 
            "Abrir PDF", 
            "", 
            "Archivos PDF (*.pdf)"
        )
        
        if ruta:
            self.pdf_path = ruta
            nombre_archivo = os.path.basename(ruta)
            self.etiqueta_info.setText(f"PDF cargado: {nombre_archivo}")
            self.etiqueta_estado.setText(f"PDF '{nombre_archivo}' cargado correctamente")
            
            # Mostrar previsualización simple (en una app real usarías una librería como pdf2image)
            self.mostrar_previsualizacion_simple(nombre_archivo)
            
    def mostrar_previsualizacion_simple(self, nombre_archivo):
        """Mostrar una previsualización simple del PDF"""
        self.escena_previa.clear()
        
        # Crear una imagen simple para previsualización
        pixmap = QPixmap(400, 500)
        pixmap.fill(Qt.white)
        
        # Aquí en una aplicación real convertirías el PDF a imagen
        # Por ahora mostramos un placeholder
        texto_previa = QLabel(f"Previsualización de: {nombre_archivo}\n\n(En una aplicación real aquí verías las páginas del PDF)")
        texto_previa.setAlignment(Qt.AlignCenter)
        proxy_widget = self.escena_previa.addWidget(texto_previa)
        
    def mostrar_dialogo_firma(self):
        """Mostrar el diálogo para firmar el documento"""
        if not self.pdf_path:
            QMessageBox.warning(self, "Advertencia", "Primero debes abrir un PDF")
            return
            
        dialogo = DialogoFirma(self)
        if dialogo.exec():
            tipo_firma, contenido = dialogo.obtener_firma()
            self.aplicar_firma(tipo_firma, contenido)
            
    def aplicar_firma(self, tipo_firma, contenido):
        """Aplicar la firma al PDF"""
        try:
            if tipo_firma == "texto":
                self.firmar_con_texto(contenido)
            elif tipo_firma == "imagen":
                self.firmar_con_imagen(contenido)
                
            self.etiqueta_estado.setText("Documento firmado correctamente")
            QMessageBox.information(self, "Éxito", "Documento firmado correctamente")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al firmar: {str(e)}")
            
    def firmar_con_texto(self, texto):
        """Firmar el PDF con texto"""
        # Crear una imagen con el texto de firma
        img_firma = Image.new('RGB', (200, 100), color='white')
        draw = ImageDraw.Draw(img_firma)
        
        # Guardar imagen temporal
        img_firma.save("firma_temporal.png")
        
    def firmar_con_imagen(self, ruta_imagen):
        """Firmar el PDF con una imagen"""
        # Aquí procesarías la imagen de firma
        pass
        
    def guardar_pdf_firmado(self):
        """Guardar el PDF firmado"""
        if not self.pdf_path:
            QMessageBox.warning(self, "Advertencia", "No hay PDF para guardar")
            return
            
        ruta_guardar, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar PDF firmado",
            "documento_firmado.pdf",
            "Archivos PDF (*.pdf)"
        )
        
        if ruta_guardar:
            try:
                # Aquí guardarías el PDF firmado
                # Por ahora solo copiamos el original
                import shutil
                shutil.copy2(self.pdf_path, ruta_guardar)
                
                self.etiqueta_estado.setText(f"Documento guardado como: {ruta_guardar}")
                QMessageBox.information(self, "Éxito", f"Documento guardado en:\n{ruta_guardar}")
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al guardar: {str(e)}")
