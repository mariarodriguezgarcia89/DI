from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer, Qt
from cronometro import Cronometro

class CronometroWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Creamos un objeto Cronometro (la parte lógica)
        self.crono = Cronometro()

        # Creamos la interfaz
        self.label = QLabel("00:00:00")
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_pausar = QPushButton("Pausar")

        # Layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_iniciar)
        layout.addWidget(self.btn_pausar)
        self.setLayout(layout)

        # Creamos un temporizador que actualizará la pantalla cada segundo
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar)

        # Conectamos los botones
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_pausar.clicked.connect(self.pausar)

    def iniciar(self):
        # Reinicia el cronómetro y empieza a contar
        self.crono.reiniciar()
        self.timer.start(1000)  # Actualiza cada segundo

    def pausar(self):
        # Pausa o continúa según el estado
        if self.timer.isActive():
            self.crono.pausar()
            self.timer.stop()
            self.btn_pausar.setText("Continuar")
        else:
            self.crono.continuar()
            self.timer.start(1000)
            self.btn_pausar.setText("Pausar")

    def actualizar(self):
        # Muestra el tiempo en pantalla
        tiempo = self.crono.getTime().toString("hh:mm:ss")
        self.label.setText(tiempo)
