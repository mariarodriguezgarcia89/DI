# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TechMarket_Dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QScrollArea,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionA_adir_Producto = QAction(MainWindow)
        self.actionA_adir_Producto.setObjectName(u"actionA_adir_Producto")
        self.actionA_adir_Producto.setMenuRole(QAction.MenuRole.NoRole)
        self.actionEliminar_Producto = QAction(MainWindow)
        self.actionEliminar_Producto.setObjectName(u"actionEliminar_Producto")
        self.actionEliminar_Producto.setMenuRole(QAction.MenuRole.NoRole)
        self.actionMostrar_Estad_sticas = QAction(MainWindow)
        self.actionMostrar_Estad_sticas.setObjectName(u"actionMostrar_Estad_sticas")
        self.actionMostrar_Estad_sticas.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineBuscador = QLineEdit(self.centralwidget)
        self.lineBuscador.setObjectName(u"lineBuscador")
        self.lineBuscador.setGeometry(QRect(90, 20, 451, 31))
        self.lblBuscador = QLabel(self.centralwidget)
        self.lblBuscador.setObjectName(u"lblBuscador")
        self.lblBuscador.setGeometry(QRect(20, 30, 49, 16))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 80, 241, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 239, 239))
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 241, 241))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionA_adir_Producto)
        self.toolBar.addAction(self.actionEliminar_Producto)
        self.toolBar.addAction(self.actionMostrar_Estad_sticas)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionA_adir_Producto.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Producto", None))
        self.actionEliminar_Producto.setText(QCoreApplication.translate("MainWindow", u"Eliminar Producto", None))
        self.actionMostrar_Estad_sticas.setText(QCoreApplication.translate("MainWindow", u"Mostrar Estad\u00edsticas", None))
        self.lblBuscador.setText(QCoreApplication.translate("MainWindow", u"Buscador:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

