# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overwiew.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form_Overwiew(object):
    def setupUi(self, Form_Overwiew):
        if not Form_Overwiew.objectName():
            Form_Overwiew.setObjectName(u"Form_Overwiew")
        Form_Overwiew.resize(274, 274)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_Overwiew.sizePolicy().hasHeightForWidth())
        Form_Overwiew.setSizePolicy(sizePolicy)
        Form_Overwiew.setMinimumSize(QSize(274, 274))
        Form_Overwiew.setMaximumSize(QSize(548, 548))
        self.verticalLayout = QVBoxLayout(Form_Overwiew)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.layout_winrate = QVBoxLayout()
        self.layout_winrate.setSpacing(0)
        self.layout_winrate.setObjectName(u"layout_winrate")
        self.label = QLabel(Form_Overwiew)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(128, 32))
        self.label.setMaximumSize(QSize(256, 64))
        font = QFont()
        font.setFamilies([u"VALVE Pulp"])
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.layout_winrate.addWidget(self.label)

        self.label_winrate = QLabel(Form_Overwiew)
        self.label_winrate.setObjectName(u"label_winrate")
        sizePolicy1.setHeightForWidth(self.label_winrate.sizePolicy().hasHeightForWidth())
        self.label_winrate.setSizePolicy(sizePolicy1)
        self.label_winrate.setMinimumSize(QSize(128, 64))
        self.label_winrate.setMaximumSize(QSize(256, 128))
        font1 = QFont()
        font1.setFamilies([u"VALVE Oracle"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_winrate.setFont(font1)
        self.label_winrate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_winrate.addWidget(self.label_winrate)

        self.label_WL = QLabel(Form_Overwiew)
        self.label_WL.setObjectName(u"label_WL")
        sizePolicy1.setHeightForWidth(self.label_WL.sizePolicy().hasHeightForWidth())
        self.label_WL.setSizePolicy(sizePolicy1)
        self.label_WL.setMinimumSize(QSize(128, 32))
        self.label_WL.setMaximumSize(QSize(256, 64))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_WL.setFont(font2)
        self.label_WL.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.layout_winrate.addWidget(self.label_WL)


        self.horizontalLayout_2.addLayout(self.layout_winrate)

        self.layout_kd = QVBoxLayout()
        self.layout_kd.setSpacing(0)
        self.layout_kd.setObjectName(u"layout_kd")
        self.label_3 = QLabel(Form_Overwiew)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(128, 32))
        self.label_3.setMaximumSize(QSize(256, 64))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.layout_kd.addWidget(self.label_3)

        self.label_KD = QLabel(Form_Overwiew)
        self.label_KD.setObjectName(u"label_KD")
        sizePolicy1.setHeightForWidth(self.label_KD.sizePolicy().hasHeightForWidth())
        self.label_KD.setSizePolicy(sizePolicy1)
        self.label_KD.setMinimumSize(QSize(128, 64))
        self.label_KD.setMaximumSize(QSize(256, 128))
        self.label_KD.setFont(font1)
        self.label_KD.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_kd.addWidget(self.label_KD)

        self.label_kkddaa = QLabel(Form_Overwiew)
        self.label_kkddaa.setObjectName(u"label_kkddaa")
        sizePolicy1.setHeightForWidth(self.label_kkddaa.sizePolicy().hasHeightForWidth())
        self.label_kkddaa.setSizePolicy(sizePolicy1)
        self.label_kkddaa.setMinimumSize(QSize(128, 32))
        self.label_kkddaa.setMaximumSize(QSize(256, 64))
        self.label_kkddaa.setFont(font2)
        self.label_kkddaa.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.layout_kd.addWidget(self.label_kkddaa)


        self.horizontalLayout_2.addLayout(self.layout_kd)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 600, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form_Overwiew)

        QMetaObject.connectSlotsByName(Form_Overwiew)
    # setupUi

    def retranslateUi(self, Form_Overwiew):
        Form_Overwiew.setWindowTitle(QCoreApplication.translate("Form_Overwiew", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form_Overwiew", u"WIN RATE", None))
        self.label_winrate.setText(QCoreApplication.translate("Form_Overwiew", u"winrate", None))
        self.label_WL.setText(QCoreApplication.translate("Form_Overwiew", u"W: L:", None))
        self.label_3.setText(QCoreApplication.translate("Form_Overwiew", u"K/D/A", None))
        self.label_KD.setText(QCoreApplication.translate("Form_Overwiew", u"0/0/0", None))
        self.label_kkddaa.setText(QCoreApplication.translate("Form_Overwiew", u"K: D: A:", None))
    # retranslateUi

