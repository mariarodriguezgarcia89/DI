# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ejercicio2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineNombre = QLineEdit(self.centralwidget)
        self.lineNombre.setObjectName(u"lineNombre")
        self.lineNombre.setGeometry(QRect(160, 100, 251, 41))
        self.comboRol = QComboBox(self.centralwidget)
        self.comboRol.addItem("")
        self.comboRol.addItem("")
        self.comboRol.addItem("")
        self.comboRol.setObjectName(u"comboRol")
        self.comboRol.setGeometry(QRect(160, 150, 251, 21))
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(100, 110, 49, 16))
        self.lblRol = QLabel(self.centralwidget)
        self.lblRol.setObjectName(u"lblRol")
        self.lblRol.setGeometry(QRect(130, 150, 21, 16))
        self.checkNormas = QCheckBox(self.centralwidget)
        self.checkNormas.setObjectName(u"checkNormas")
        self.checkNormas.setGeometry(QRect(160, 180, 181, 20))
        self.btnEnviar = QPushButton(self.centralwidget)
        self.btnEnviar.setObjectName(u"btnEnviar")
        self.btnEnviar.setGeometry(QRect(260, 230, 79, 24))
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
        self.comboRol.setItemText(0, QCoreApplication.translate("MainWindow", u"Alumno", None))
        self.comboRol.setItemText(1, QCoreApplication.translate("MainWindow", u"Profe", None))
        self.comboRol.setItemText(2, QCoreApplication.translate("MainWindow", u"Invitado", None))

        self.lblNombre.setText(QCoreApplication.translate("MainWindow", u"NOMBRE:", None))
        self.lblRol.setText(QCoreApplication.translate("MainWindow", u"ROL:", None))
        self.checkNormas.setText(QCoreApplication.translate("MainWindow", u"Acepto normas", None))
        self.btnEnviar.setText(QCoreApplication.translate("MainWindow", u"ENVIAR", None))
    # retranslateUi

