from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
                               QLabel, QLineEdit, QTextEdit, QComboBox, 
                               QFileDialog, QGroupBox, QRadioButton, QButtonGroup)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class DialogoFirma(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tipo_firma = "texto"
        self.contenido_firma = ""
        self.setup_ui()
        
    def setup_ui(self):
        """Configurar la interfaz del diálogo"""
        self.setWindowTitle("Firmar Documento")
        self.setFixedSize(500, 400)
        
        layout = QVBoxLayout()
        
        # Selección de tipo de firma
        self.crear_seleccion_tipo(layout)
        
        # Área de contenido de firma
        self.crear_area_contenido(layout)
        
        # Botones
        self.crear_botones(layout)
        
        self.setLayout(layout)
        
    def crear_seleccion_tipo(self, layout):
        """Crear la selección de tipo de firma"""
        grupo = QGroupBox("Tipo de Firma")
        layout_grupo = QVBoxLayout()
        
        self.grupo_botones = QButtonGroup(self)
        
        # Opción de texto
        self.radio_texto = QRadioButton("Firma de Texto")
        self.radio_texto.setChecked(True)
        self.radio_texto.toggled.connect(self.cambiar_tipo_firma)
        self.grupo_botones.addButton(self.radio_texto)
        layout_grupo.addWidget(self.radio_texto)
        
        # Opción de imagen
        self.radio_imagen = QRadioButton("Firma con Imagen")
        self.radio_imagen.toggled.connect(self.cambiar_tipo_firma)
        self.grupo_botones.addButton(self.radio_imagen)
        layout_grupo.addWidget(self.radio_imagen)
        
        # Opción de sello
        self.radio_sello = QRadioButton("Sello Digital")
        self.radio_sello.toggled.connect(self.cambiar_tipo_firma)
        self.grupo_botones.addButton(self.radio_sello)
        layout_grupo.addWidget(self.radio_sello)
        
        grupo.setLayout(layout_grupo)
        layout.addWidget(grupo)
        
    def crear_area_contenido(self, layout):
        """Crear el área para el contenido de la firma"""
        # Área para texto
        self.grupo_texto = QGroupBox("Texto de Firma")
        layout_texto = QVBoxLayout()
        
        self.campo_texto = QTextEdit()
        self.campo_texto.setPlaceholderText("Ingresa tu nombre o texto de firma...")
        self.campo_texto.setMaximumHeight(100)
        layout_texto.addWidget(self.campo_texto)
        
        self.grupo_texto.setLayout(layout_texto)
        layout.addWidget(self.grupo_texto)
        
        # Área para imagen
        self.grupo_imagen = QGroupBox("Imagen de Firma")
        layout_imagen = QVBoxLayout()
        
        self.etiqueta_imagen = QLabel("Selecciona una imagen para firmar")
        self.etiqueta_imagen.setAlignment(Qt.AlignCenter)
        self.etiqueta_imagen.setMinimumHeight(150)
        self.etiqueta_imagen.setStyleSheet("border: 1px solid gray;")
        
        btn_seleccionar_imagen = QPushButton("Seleccionar Imagen")
        btn_seleccionar_imagen.clicked.connect(self.seleccionar_imagen)
        
        layout_imagen.addWidget(self.etiqueta_imagen)
        layout_imagen.addWidget(btn_seleccionar_imagen)
        
        self.grupo_imagen.setLayout(layout_imagen)
        layout.addWidget(self.grupo_imagen)
        self.grupo_imagen.setVisible(False)
        
    def crear_botones(self, layout):
        """Crear los botones Aceptar/Cancelar"""
        layout_botones = QHBoxLayout()
        
        btn_aceptar = QPushButton("Aplicar Firma")
        btn_aceptar.clicked.connect(self.aceptar_firma)
        
        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.clicked.connect(self.reject)
        
        layout_botones.addWidget(btn_aceptar)
        layout_botones.addWidget(btn_cancelar)
        
        layout.addLayout(layout_botones)
        
    def cambiar_tipo_firma(self):
        """Cambiar la interfaz según el tipo de firma seleccionado"""
        if self.radio_texto.isChecked():
            self.tipo_firma = "texto"
            self.grupo_texto.setVisible(True)
            self.grupo_imagen.setVisible(False)
        elif self.radio_imagen.isChecked() or self.radio_sello.isChecked():
            self.tipo_firma = "imagen"
            self.grupo_texto.setVisible(False)
            self.grupo_imagen.setVisible(True)
            
    def seleccionar_imagen(self):
        """Seleccionar una imagen para la firma"""
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar Imagen",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp)"
        )
        
        if ruta:
            self.contenido_firma = ruta
            pixmap = QPixmap(ruta)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(200, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.etiqueta_imagen.setPixmap(pixmap)
                
    def aceptar_firma(self):
        """Aceptar y procesar la firma"""
        if self.radio_texto.isChecked():
            texto = self.campo_texto.toPlainText().strip()
            if not texto:
                from PySide6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "Advertencia", "Por favor ingresa un texto para la firma")
                return
            self.contenido_firma = texto
            
        elif (self.radio_imagen.isChecked() or self.radio_sello.isChecked()) and not self.contenido_firma:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Advertencia", "Por favor selecciona una imagen para la firma")
            return
            
        self.accept()
        
    def obtener_firma(self):
        """Obtener los datos de la firma"""
        return self.tipo_firma, self.contenido_firma
