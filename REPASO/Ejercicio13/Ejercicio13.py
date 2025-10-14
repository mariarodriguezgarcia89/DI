# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ejercicio13.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(498, 580)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionPlay = QAction(MainWindow)
        self.actionPlay.setObjectName(u"actionPlay")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.actionPlay.setIcon(icon)
        self.actionPlay.setMenuRole(QAction.MenuRole.NoRole)
        self.actionPause = QAction(MainWindow)
        self.actionPause.setObjectName(u"actionPause")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.actionPause.setIcon(icon1)
        self.actionPause.setMenuRole(QAction.MenuRole.NoRole)
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.actionStop.setIcon(icon2)
        self.actionStop.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(140, 50, 191, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTitulo = QLabel(self.verticalLayoutWidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 498, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.Playlist = QDockWidget(MainWindow)
        self.Playlist.setObjectName(u"Playlist")
        self.Playlist.setFloating(True)
        self.Playlist.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetClosable|QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.Playlist.setDockLocation(Qt.DockWidgetArea.TopDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.lstPlaylist = QListWidget(self.dockWidgetContents)
        QListWidgetItem(self.lstPlaylist)
        QListWidgetItem(self.lstPlaylist)
        QListWidgetItem(self.lstPlaylist)
        self.lstPlaylist.setObjectName(u"lstPlaylist")
        self.lstPlaylist.setGeometry(QRect(0, 10, 491, 192))
        self.Playlist.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.Playlist)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionSalir)
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionStop)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.actionPause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"Listo", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))

        __sortingEnabled = self.lstPlaylist.isSortingEnabled()
        self.lstPlaylist.setSortingEnabled(False)
        ___qlistwidgetitem = self.lstPlaylist.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Canci\u00f3n1.mp3", None));
        ___qlistwidgetitem1 = self.lstPlaylist.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Canci\u00f3n2.mp3", None));
        ___qlistwidgetitem2 = self.lstPlaylist.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Canci\u00f3n3.mp3", None));
        self.lstPlaylist.setSortingEnabled(__sortingEnabled)

    # retranslateUi

