# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_pagesWidget(object):
    def setupUi(self, pagesWidget):
        if not pagesWidget.objectName():
            pagesWidget.setObjectName(u"pagesWidget")
        pagesWidget.resize(400, 300)
        self.pushButton_L = QPushButton(pagesWidget)
        self.pushButton_L.setObjectName(u"pushButton_L")
        self.pushButton_L.setGeometry(QRect(60, 150, 64, 64))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_L.sizePolicy().hasHeightForWidth())
        self.pushButton_L.setSizePolicy(sizePolicy)
        self.pushButton_L.setMinimumSize(QSize(64, 64))
        self.pushButton_L.setMaximumSize(QSize(64, 64))
        self.pushButton_1 = QPushButton(pagesWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(130, 150, 64, 64))
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QSize(64, 64))
        self.pushButton_1.setMaximumSize(QSize(64, 64))
        self.pushButton_P = QPushButton(pagesWidget)
        self.pushButton_P.setObjectName(u"pushButton_P")
        self.pushButton_P.setGeometry(QRect(200, 150, 64, 64))
        sizePolicy.setHeightForWidth(self.pushButton_P.sizePolicy().hasHeightForWidth())
        self.pushButton_P.setSizePolicy(sizePolicy)
        self.pushButton_P.setMinimumSize(QSize(64, 64))
        self.pushButton_P.setMaximumSize(QSize(64, 64))

        self.retranslateUi(pagesWidget)

        QMetaObject.connectSlotsByName(pagesWidget)
    # setupUi

    def retranslateUi(self, pagesWidget):
        pagesWidget.setWindowTitle(QCoreApplication.translate("pagesWidget", u"Form", None))
        self.pushButton_L.setText(QCoreApplication.translate("pagesWidget", u"<<", None))
        self.pushButton_1.setText(QCoreApplication.translate("pagesWidget", u"1", None))
        self.pushButton_P.setText(QCoreApplication.translate("pagesWidget", u">>", None))
    # retranslateUi

