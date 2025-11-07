import sys
from PySide6.QtWidgets import QSlider, QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from t3_batterywidget import BatteryWidget

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("BatteryWidget Demo")
    w.showMaximized()
    battery = BatteryWidget()
    slider = QSlider(Qt.Horizontal)
    slider.setRange(0, 100)
    slider.setValue(50)
    slider.valueChanged.connect(battery.setLevel)
    layout = QVBoxLayout()
    layout.addWidget(battery)
    layout.addWidget(slider)
    w.setLayout(layout)
    layout = QVBoxLayout(w)
    layout.addWidget(battery)
    w.setLayout(layout)
    w.show()
    app.exec()
