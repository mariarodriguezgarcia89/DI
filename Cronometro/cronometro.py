from PySide6.QtCore import QElapsedTimer, QTime

class Cronometro:
    def __init__(self):
        # Creamos dos contadores de tiempo
        # _tiempo_transcurrido mide desde que arrancamos el cronómetro
        # _tiempo_pausa mide cuánto tiempo hemos estado en pausa
        self._tiempo_transcurrido = QElapsedTimer()
        self._tiempo_pausa = QElapsedTimer()

        # acumulador sirve para guardar el tiempo total pausado
        self.acumulador = 0

    def reiniciar(self):
        # Reinicia el cronómetro desde cero
        self._tiempo_transcurrido.restart()
        self.acumulador = 0

    def getTime(self):
        # Devuelve el tiempo transcurrido total (sin contar las pausas)
        return QTime(0, 0).addMSecs(self._tiempo_transcurrido.elapsed() - self.acumulador)

    def pausar(self):
        # Cuando pausamos, empezamos a medir cuánto dura la pausa
        self._tiempo_pausa.restart()

    def continuar(self):
        # Cuando continuamos, sumamos al acumulador el tiempo que estuvimos pausados
        self.acumulador += self._tiempo_pausa.elapsed()
