import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider,
    QCheckBox, QLineEdit, QToolButton, QHBoxLayout, QStatusBar
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, QIcon
from t2_moneylineedit import MoneyLineEdit
from t3_batterywidget import BatteryWidget
from t4_searchinput import SearchInput
import resources_rc  # tu archivo .qrc


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MENÚ")
        self.resize(800, 600)
        self.setWindowIcon(QIcon(":/contador.png"))

        # StatusBar
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage("LISTO")

        # Barra de menú
        self.menu_bar = self.menuBar()
        self.menu_bar.setStyleSheet("""
            QMenuBar {
                background-color: #2c3e50;
                color: white;
            }
            QMenuBar::item {
                font-size: 18px;
                background-color: transparent;
                padding: 4px 20px;
            }
            QMenuBar::item:selected {
                background-color: #34495e;
            }
            QMenu {
                font-size: 16px;
                background-color: #ecf0f1;
                color: black;
            }
            QMenu::item:selected {
                background-color: #bdc3c7;
            }
        """)
        apps_menu = self.menu_bar.addMenu("Aplicaciones")

        # Acciones del menú
        apps_menu.addAction("Inicio", lambda: self.show_widget(self.inicio_widget_content()))
        apps_menu.addAction("Switch", lambda: self.show_widget(self.switch_widget_content()))
        apps_menu.addAction("MoneyLineEdit", lambda: self.show_widget(self.money_widget_content()))
        apps_menu.addAction("BatteryWidget", lambda: self.show_widget(self.battery_widget_content()))
        apps_menu.addAction("SearchInput", lambda: self.show_widget(self.search_widget_content()))

        # Mostrar pantalla inicial
        self.show_widget(self.inicio_widget_content())

    # -------------------- Wrapper para centralWidget --------------------
    def show_widget(self, widget):
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(widget)
        self.setCentralWidget(container)

    # -------------------- Contenido de miniaplicaciones --------------------
    def inicio_widget_content(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        lbl = QLabel("Pantalla de Inicio")
        lbl.setAlignment(Qt.AlignCenter)
        layout.addWidget(lbl)
        return widget

    def switch_widget_content(self):
        chkSwitch = QCheckBox("OFF")
        chkSwitch.setStyleSheet("""
            QCheckBox::indicator { width: 46px; height: 24px; }
            QCheckBox::indicator:unchecked { border-radius: 12px; background:#ccc; }
            QCheckBox::indicator:checked { border-radius: 12px; background:#2ecc71; }
        """)
        chkSwitch.toggled.connect(lambda s: chkSwitch.setText("ON" if s else "OFF"))

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(chkSwitch)
        return widget

    def money_widget_content(self):
        txt_money = MoneyLineEdit()
        lbl_money = QLabel("Valor:")
        txt_money.valueChanged.connect(lambda v: lbl_money.setText(f"Valor: {v:.2f} €"))

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(txt_money)
        layout.addWidget(lbl_money)
        return widget

    def battery_widget_content(self):
        battery = BatteryWidget()
        slider = QSlider(Qt.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(50)
        slider.valueChanged.connect(battery.setLevel)

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(battery)
        layout.addWidget(slider)
        return widget

    def search_widget_content(self):
        search = SearchInput()
        lbl_search = QLabel("0 caracteres")
        search.text.textChanged.connect(lambda t: lbl_search.setText(f"{len(t)} caracteres"))

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(search)
        layout.addWidget(lbl_search)
        return widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
