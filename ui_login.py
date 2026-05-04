# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form_login(object):
    def setupUi(self, Form_login):
        if not Form_login.objectName():
            Form_login.setObjectName(u"Form_login")
        Form_login.resize(800, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_login.sizePolicy().hasHeightForWidth())
        Form_login.setSizePolicy(sizePolicy)
        Form_login.setMinimumSize(QSize(800, 400))
        Form_login.setBaseSize(QSize(700, 400))
        icon = QIcon(QIcon.fromTheme(u"applications-internet"))
        Form_login.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form_login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_title = QLabel(Form_login)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(36)
        self.label_title.setFont(font)
        self.label_title.setAutoFillBackground(True)
        self.label_title.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_title.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_title.setLineWidth(3)
        self.label_title.setMidLineWidth(3)
        self.label_title.setTextFormat(Qt.TextFormat.RichText)
        self.label_title.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(24)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, -1, 15, -1)
        self.lineEdit_link = QLineEdit(Form_login)
        self.lineEdit_link.setObjectName(u"lineEdit_link")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_link.sizePolicy().hasHeightForWidth())
        self.lineEdit_link.setSizePolicy(sizePolicy1)
        self.lineEdit_link.setMinimumSize(QSize(0, 80))
        font1 = QFont()
        font1.setPointSize(16)
        self.lineEdit_link.setFont(font1)
        self.lineEdit_link.setAutoFillBackground(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_link)

        self.pushButton_szukaj = QPushButton(Form_login)
        self.pushButton_szukaj.setObjectName(u"pushButton_szukaj")
        self.pushButton_szukaj.setMinimumSize(QSize(80, 80))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton_szukaj.setFont(font2)
        self.pushButton_szukaj.setAutoDefault(False)
        self.pushButton_szukaj.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_szukaj)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, -1, -1, -1)
        self.checkBox_zapisz = QCheckBox(Form_login)
        self.checkBox_zapisz.setObjectName(u"checkBox_zapisz")
        font3 = QFont()
        font3.setPointSize(11)
        self.checkBox_zapisz.setFont(font3)
        self.checkBox_zapisz.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBox_zapisz)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)


        self.retranslateUi(Form_login)

        self.pushButton_szukaj.setDefault(False)


        QMetaObject.connectSlotsByName(Form_login)
    # setupUi

    def retranslateUi(self, Form_login):
        Form_login.setWindowTitle(QCoreApplication.translate("Form_login", u"Login", None))
        self.label_title.setText(QCoreApplication.translate("Form_login", u"DEADLOCK STATS", None))
        self.lineEdit_link.setInputMask("")
        self.lineEdit_link.setPlaceholderText(QCoreApplication.translate("Form_login", u"Podaj link do profilu steam", None))
        self.pushButton_szukaj.setText(QCoreApplication.translate("Form_login", u"Zaloguj", None))
        self.checkBox_zapisz.setText(QCoreApplication.translate("Form_login", u"Zapisz profil", None))
    # retranslateUi

