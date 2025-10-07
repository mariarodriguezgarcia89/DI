
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(130, 120, 311, 261))
        self.layoutBotones = QVBoxLayout(self.verticalLayoutWidget)
        self.layoutBotones.setObjectName(u"layoutBotones")
        self.layoutBotones.setContentsMargins(0, 0, 0, 0)
        self.btn1 = QPushButton(self.verticalLayoutWidget)
        self.btn1.setObjectName(u"btn1")

        self.layoutBotones.addWidget(self.btn1)

        self.btn2 = QPushButton(self.verticalLayoutWidget)
        self.btn2.setObjectName(u"btn2")

        self.layoutBotones.addWidget(self.btn2)

        self.btn3 = QPushButton(self.verticalLayoutWidget)
        self.btn3.setObjectName(u"btn3")

        self.layoutBotones.addWidget(self.btn3)

        self.btn4 = QPushButton(self.verticalLayoutWidget)
        self.btn4.setObjectName(u"btn4")

        self.layoutBotones.addWidget(self.btn4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
    # retranslateUi

