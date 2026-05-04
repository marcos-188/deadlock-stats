# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form_Profile(object):
    def setupUi(self, Form_Profile):
        if not Form_Profile.objectName():
            Form_Profile.setObjectName(u"Form_Profile")
        Form_Profile.resize(977, 414)
        self.gridLayout = QGridLayout(Form_Profile)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.label_awatar = QLabel(Form_Profile)
        self.label_awatar.setObjectName(u"label_awatar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_awatar.sizePolicy().hasHeightForWidth())
        self.label_awatar.setSizePolicy(sizePolicy)
        self.label_awatar.setMinimumSize(QSize(128, 128))
        self.label_awatar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_awatar, 0, 0, 1, 1)

        self.label_nazwa = QLabel(Form_Profile)
        self.label_nazwa.setObjectName(u"label_nazwa")
        font = QFont()
        font.setPointSize(18)
        self.label_nazwa.setFont(font)

        self.gridLayout.addWidget(self.label_nazwa, 0, 1, 1, 1)


        self.retranslateUi(Form_Profile)

        QMetaObject.connectSlotsByName(Form_Profile)
    # setupUi

    def retranslateUi(self, Form_Profile):
        Form_Profile.setWindowTitle(QCoreApplication.translate("Form_Profile", u"Form", None))
        self.label_awatar.setText(QCoreApplication.translate("Form_Profile", u"profile pic", None))
        self.label_nazwa.setText(QCoreApplication.translate("Form_Profile", u"profile name", None))
    # retranslateUi

