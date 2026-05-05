# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 843)
        MainWindow.setMinimumSize(QSize(800, 800))
        MainWindow.setBaseSize(QSize(1200, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1200, 800))
        self.centralwidget.setBaseSize(QSize(1200, 800))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(0, 200))
        self.header_layout = QVBoxLayout(self.header_widget)
        self.header_layout.setObjectName(u"header_layout")

        self.verticalLayout.addWidget(self.header_widget)

        self.maincontentWidget = QWidget(self.centralwidget)
        self.maincontentWidget.setObjectName(u"maincontentWidget")
        self.horizontalLayout = QHBoxLayout(self.maincontentWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.scrollArea = QScrollArea(self.maincontentWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(520, 140))
        self.scrollArea.setMaximumSize(QSize(520, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 518, 556))
        self.scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setObjectName(u"scroll_layout")
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.overwiewWidget = QWidget(self.maincontentWidget)
        self.overwiewWidget.setObjectName(u"overwiewWidget")
        self.overwiewWidget.setMinimumSize(QSize(149, 0))
        self.overwiew_layout = QHBoxLayout(self.overwiewWidget)
        self.overwiew_layout.setObjectName(u"overwiew_layout")

        self.horizontalLayout.addWidget(self.overwiewWidget)


        self.verticalLayout.addWidget(self.maincontentWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

