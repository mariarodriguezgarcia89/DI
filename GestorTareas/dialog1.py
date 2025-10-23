# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo1.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_DialogNuevoProyecto(object):
    def setupUi(self, DialogNuevoProyecto):
        if not DialogNuevoProyecto.objectName():
            DialogNuevoProyecto.setObjectName(u"DialogNuevoProyecto")
        DialogNuevoProyecto.resize(400, 300)
        self.lblIntroduce = QLabel(DialogNuevoProyecto)
        self.lblIntroduce.setObjectName(u"lblIntroduce")
        self.lblIntroduce.setGeometry(QRect(0, 40, 271, 16))
        self.lineIntroduce = QLineEdit(DialogNuevoProyecto)
        self.lineIntroduce.setObjectName(u"lineIntroduce")
        self.lineIntroduce.setGeometry(QRect(240, 40, 113, 21))
        self.btnBoxIntroduce = QDialogButtonBox(DialogNuevoProyecto)
        self.btnBoxIntroduce.setObjectName(u"btnBoxIntroduce")
        self.btnBoxIntroduce.setGeometry(QRect(120, 100, 164, 24))
        self.btnBoxIntroduce.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.retranslateUi(DialogNuevoProyecto)

        QMetaObject.connectSlotsByName(DialogNuevoProyecto)
    # setupUi

    def retranslateUi(self, DialogNuevoProyecto):
        DialogNuevoProyecto.setWindowTitle(QCoreApplication.translate("DialogNuevoProyecto", u"Dialog", None))
        self.lblIntroduce.setText(QCoreApplication.translate("DialogNuevoProyecto", u"Introduce el nombre del nuevo proyecto:", None))
    # retranslateUi

