# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(568, 476)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(250, 180, 160, 146))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnNuevoProyecto = QPushButton(self.verticalLayoutWidget)
        self.btnNuevoProyecto.setObjectName(u"btnNuevoProyecto")

        self.verticalLayout.addWidget(self.btnNuevoProyecto)

        self.btnConfirmar = QPushButton(self.verticalLayoutWidget)
        self.btnConfirmar.setObjectName(u"btnConfirmar")

        self.verticalLayout.addWidget(self.btnConfirmar)

        self.btnCentroMens = QPushButton(self.verticalLayoutWidget)
        self.btnCentroMens.setObjectName(u"btnCentroMens")

        self.verticalLayout.addWidget(self.btnCentroMens)

        self.btnPref = QPushButton(self.verticalLayoutWidget)
        self.btnPref.setObjectName(u"btnPref")

        self.verticalLayout.addWidget(self.btnPref)

        self.bntExport = QPushButton(self.verticalLayoutWidget)
        self.bntExport.setObjectName(u"bntExport")

        self.verticalLayout.addWidget(self.bntExport)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 568, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuHerramientas = QMenu(self.menubar)
        self.menuHerramientas.setObjectName(u"menuHerramientas")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnNuevoProyecto.setText(QCoreApplication.translate("MainWindow", u"Nuevo Proyecto...", None))
        self.btnConfirmar.setText(QCoreApplication.translate("MainWindow", u"Confirmar Acci\u00f3n...", None))
        self.btnCentroMens.setText(QCoreApplication.translate("MainWindow", u"Centro de mensajes...", None))
        self.btnPref.setText(QCoreApplication.translate("MainWindow", u"Preferencias de usuario...", None))
        self.bntExport.setText(QCoreApplication.translate("MainWindow", u"Exportar informe...", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuHerramientas.setTitle(QCoreApplication.translate("MainWindow", u"Herramientas", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

