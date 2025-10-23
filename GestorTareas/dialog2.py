# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogo2.ui'
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
    QLabel, QSizePolicy, QWidget)

class Ui_DialogConfirmar(object):
    def setupUi(self, DialogConfirmar):
        if not DialogConfirmar.objectName():
            DialogConfirmar.setObjectName(u"DialogConfirmar")
        DialogConfirmar.resize(400, 300)
        self.lblConfirmar = QLabel(DialogConfirmar)
        self.lblConfirmar.setObjectName(u"lblConfirmar")
        self.lblConfirmar.setGeometry(QRect(60, 100, 321, 61))
        self.DialogBoxConfirmar = QDialogButtonBox(DialogConfirmar)
        self.DialogBoxConfirmar.setObjectName(u"DialogBoxConfirmar")
        self.DialogBoxConfirmar.setGeometry(QRect(130, 190, 164, 24))
        self.DialogBoxConfirmar.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.retranslateUi(DialogConfirmar)

        QMetaObject.connectSlotsByName(DialogConfirmar)
    # setupUi

    def retranslateUi(self, DialogConfirmar):
        DialogConfirmar.setWindowTitle(QCoreApplication.translate("DialogConfirmar", u"Dialog", None))
        self.lblConfirmar.setText(QCoreApplication.translate("DialogConfirmar", u"\u00bfSeguro que deseas eliminar los datos temporales?", None))
    # retranslateUi

