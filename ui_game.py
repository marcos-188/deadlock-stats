# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form_Game(object):
    def setupUi(self, Form_Game):
        if not Form_Game.objectName():
            Form_Game.setObjectName(u"Form_Game")
        Form_Game.resize(500, 140)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_Game.sizePolicy().hasHeightForWidth())
        Form_Game.setSizePolicy(sizePolicy)
        Form_Game.setMinimumSize(QSize(500, 140))
        Form_Game.setMaximumSize(QSize(500, 140))
        self.horizontalLayout = QHBoxLayout(Form_Game)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 2, 0, 2)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_heroicon = QLabel(Form_Game)
        self.label_heroicon.setObjectName(u"label_heroicon")
        sizePolicy.setHeightForWidth(self.label_heroicon.sizePolicy().hasHeightForWidth())
        self.label_heroicon.setSizePolicy(sizePolicy)
        self.label_heroicon.setMinimumSize(QSize(64, 64))
        self.label_heroicon.setMaximumSize(QSize(64, 64))
        self.label_heroicon.setBaseSize(QSize(64, 64))

        self.gridLayout.addWidget(self.label_heroicon, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, -1, -1, -1)
        self.label_heroname = QLabel(Form_Game)
        self.label_heroname.setObjectName(u"label_heroname")
        sizePolicy.setHeightForWidth(self.label_heroname.sizePolicy().hasHeightForWidth())
        self.label_heroname.setSizePolicy(sizePolicy)
        self.label_heroname.setMinimumSize(QSize(128, 32))
        self.label_heroname.setMaximumSize(QSize(128, 32))
        self.label_heroname.setBaseSize(QSize(64, 32))
        font = QFont()
        font.setPointSize(14)
        self.label_heroname.setFont(font)

        self.verticalLayout_3.addWidget(self.label_heroname)

        self.label_wynik = QLabel(Form_Game)
        self.label_wynik.setObjectName(u"label_wynik")
        sizePolicy.setHeightForWidth(self.label_wynik.sizePolicy().hasHeightForWidth())
        self.label_wynik.setSizePolicy(sizePolicy)
        self.label_wynik.setMinimumSize(QSize(128, 32))
        self.label_wynik.setMaximumSize(QSize(128, 32))
        self.label_wynik.setBaseSize(QSize(32, 64))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_wynik.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_wynik)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, -1, -1, -1)
        self.label_idgry = QLabel(Form_Game)
        self.label_idgry.setObjectName(u"label_idgry")

        self.verticalLayout_4.addWidget(self.label_idgry)

        self.label_data = QLabel(Form_Game)
        self.label_data.setObjectName(u"label_data")

        self.verticalLayout_4.addWidget(self.label_data)

        self.label_duration = QLabel(Form_Game)
        self.label_duration.setObjectName(u"label_duration")

        self.verticalLayout_4.addWidget(self.label_duration)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_KDA = QLabel(Form_Game)
        self.label_KDA.setObjectName(u"label_KDA")
        sizePolicy.setHeightForWidth(self.label_KDA.sizePolicy().hasHeightForWidth())
        self.label_KDA.setSizePolicy(sizePolicy)
        self.label_KDA.setMinimumSize(QSize(128, 40))
        self.label_KDA.setMaximumSize(QSize(128, 40))

        self.verticalLayout_5.addWidget(self.label_KDA)

        self.label_Dusze = QLabel(Form_Game)
        self.label_Dusze.setObjectName(u"label_Dusze")
        sizePolicy.setHeightForWidth(self.label_Dusze.sizePolicy().hasHeightForWidth())
        self.label_Dusze.setSizePolicy(sizePolicy)
        self.label_Dusze.setMinimumSize(QSize(128, 40))
        self.label_Dusze.setMaximumSize(QSize(128, 40))

        self.verticalLayout_5.addWidget(self.label_Dusze)

        self.label_MVP = QLabel(Form_Game)
        self.label_MVP.setObjectName(u"label_MVP")

        self.verticalLayout_5.addWidget(self.label_MVP)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.label_Gracze = QLabel(Form_Game)
        self.label_Gracze.setObjectName(u"label_Gracze")
        sizePolicy.setHeightForWidth(self.label_Gracze.sizePolicy().hasHeightForWidth())
        self.label_Gracze.setSizePolicy(sizePolicy)
        self.label_Gracze.setMinimumSize(QSize(128, 128))
        self.label_Gracze.setMaximumSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.label_Gracze)


        self.retranslateUi(Form_Game)

        QMetaObject.connectSlotsByName(Form_Game)
    # setupUi

    def retranslateUi(self, Form_Game):
        Form_Game.setWindowTitle(QCoreApplication.translate("Form_Game", u"Form", None))
        self.label_heroicon.setText(QCoreApplication.translate("Form_Game", u"Ikonka", None))
        self.label_heroname.setText(QCoreApplication.translate("Form_Game", u"Nazwa", None))
        self.label_wynik.setText(QCoreApplication.translate("Form_Game", u"Wynik", None))
        self.label_idgry.setText(QCoreApplication.translate("Form_Game", u"ID gry", None))
        self.label_data.setText(QCoreApplication.translate("Form_Game", u"Data", None))
        self.label_duration.setText(QCoreApplication.translate("Form_Game", u"Duration", None))
        self.label_KDA.setText(QCoreApplication.translate("Form_Game", u"K/D/A", None))
        self.label_Dusze.setText(QCoreApplication.translate("Form_Game", u"Dusze", None))
        self.label_MVP.setText(QCoreApplication.translate("Form_Game", u"Sratatata(MVP)", None))
        self.label_Gracze.setText(QCoreApplication.translate("Form_Game", u"Sratatatatat (gracze)", None))
    # retranslateUi

