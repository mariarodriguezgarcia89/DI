import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from t2_moneylineedit import MoneyLineEdit

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("MoneyLineEdit Demo")
    layout = QVBoxLayout(w)
    txt = MoneyLineEdit(); lbl = QLabel("Valor:")
    txt.valueChanged.connect(lambda v: lbl.setText(f"Valor: {v:.2f} €"))
    layout.addWidget(txt); layout.addWidget(lbl)
    w.show(); app.exec()
