# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ejercicio12.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(644, 600)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionAbrir.setCheckable(False)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.actionAbrir.setIcon(icon)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionGuardar.setIcon(icon1)
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.actionSalir.setIcon(icon2)
        self.actionMostrar = QAction(MainWindow)
        self.actionMostrar.setObjectName(u"actionMostrar")
        self.actionOcultar = QAction(MainWindow)
        self.actionOcultar.setObjectName(u"actionOcultar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 644, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.dockPlaylist = QDockWidget(MainWindow)
        self.dockPlaylist.setObjectName(u"dockPlaylist")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.lstPlaylist = QListWidget(self.dockWidgetContents)
        QListWidgetItem(self.lstPlaylist)
        QListWidgetItem(self.lstPlaylist)
        QListWidgetItem(self.lstPlaylist)
        self.lstPlaylist.setObjectName(u"lstPlaylist")
        self.lstPlaylist.setGeometry(QRect(20, 90, 371, 291))
        self.dockPlaylist.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockPlaylist)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuVer.addAction(self.actionMostrar)
        self.menuVer.addAction(self.actionOcultar)
        self.toolBar.addAction(self.actionAbrir)
        self.toolBar.addAction(self.actionGuardar)
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir...", None))
#if QT_CONFIG(statustip)
        self.actionAbrir.setStatusTip(QCoreApplication.translate("MainWindow", u"Abrir un archivo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(statustip)
        self.actionGuardar.setStatusTip(QCoreApplication.translate("MainWindow", u"Guardar el archivo", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(statustip)
        self.actionSalir.setStatusTip(QCoreApplication.translate("MainWindow", u"Cerrar la aplicaci\u00f3n", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.actionOcultar.setText(QCoreApplication.translate("MainWindow", u"Ocultar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.dockPlaylist.setWindowTitle(QCoreApplication.translate("MainWindow", u"Playlist", None))

        __sortingEnabled = self.lstPlaylist.isSortingEnabled()
        self.lstPlaylist.setSortingEnabled(False)
        ___qlistwidgetitem = self.lstPlaylist.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"cancion_1.wav", None));
        ___qlistwidgetitem1 = self.lstPlaylist.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"cancion_2.wav", None));
        ___qlistwidgetitem2 = self.lstPlaylist.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"cancion_3.wav", None));
        self.lstPlaylist.setSortingEnabled(__sortingEnabled)

    # retranslateUi

