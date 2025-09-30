# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ejercicio3.ui'
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progreBar = QProgressBar(self.centralwidget)
        self.progreBar.setObjectName(u"progreBar")
        self.progreBar.setGeometry(QRect(140, 150, 291, 23))
        self.progreBar.setValue(0)
        self.btnIniciar = QPushButton(self.centralwidget)
        self.btnIniciar.setObjectName(u"btnIniciar")
        self.btnIniciar.setGeometry(QRect(140, 170, 79, 24))
        self.listaTareas = QListWidget(self.centralwidget)
        QListWidgetItem(self.listaTareas)
        QListWidgetItem(self.listaTareas)
        QListWidgetItem(self.listaTareas)
        self.listaTareas.setObjectName(u"listaTareas")
        self.listaTareas.setGeometry(QRect(140, 220, 256, 61))
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
        self.btnIniciar.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))

        __sortingEnabled = self.listaTareas.isSortingEnabled()
        self.listaTareas.setSortingEnabled(False)
        ___qlistwidgetitem = self.listaTareas.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Tarea1", None));
        ___qlistwidgetitem1 = self.listaTareas.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tarea2", None));
        ___qlistwidgetitem2 = self.listaTareas.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tarea3", None));
        self.listaTareas.setSortingEnabled(__sortingEnabled)

    # retranslateUi

