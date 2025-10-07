# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ejercicio8.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(210, 230, 120, 80))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.lbl1 = QLabel(self.page)
        self.lbl1.setObjectName(u"lbl1")
        self.lbl1.setGeometry(QRect(40, 30, 49, 16))
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.lbl2 = QLabel(self.page_3)
        self.lbl2.setObjectName(u"lbl2")
        self.lbl2.setGeometry(QRect(40, 30, 49, 16))
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lbl3 = QLabel(self.page_2)
        self.lbl3.setObjectName(u"lbl3")
        self.lbl3.setGeometry(QRect(40, 30, 49, 16))
        self.stackedWidget.addWidget(self.page_2)
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(200, 310, 79, 24))
        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(200, 340, 79, 24))
        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setGeometry(QRect(200, 370, 79, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl1.setText(QCoreApplication.translate("MainWindow", u"CAPA1", None))
        self.lbl2.setText(QCoreApplication.translate("MainWindow", u"CAPA2", None))
        self.lbl3.setText(QCoreApplication.translate("MainWindow", u"CAPA3", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"VER CAPA 1", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"VER CAPA 2", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"VER CAPA 3", None))
    # retranslateUi

