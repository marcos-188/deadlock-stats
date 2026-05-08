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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QMenuBar, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 766)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(850, 675))
        MainWindow.setBaseSize(QSize(1000, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(820, 670))
        self.centralwidget.setBaseSize(QSize(1200, 800))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.header_widget.sizePolicy().hasHeightForWidth())
        self.header_widget.setSizePolicy(sizePolicy2)
        self.header_widget.setMinimumSize(QSize(0, 200))
        self.header_widget.setMaximumSize(QSize(16777215, 200))
        self.header_layout = QVBoxLayout(self.header_widget)
        self.header_layout.setObjectName(u"header_layout")

        self.gridLayout.addWidget(self.header_widget, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.overwiewWidget = QWidget(self.centralwidget)
        self.overwiewWidget.setObjectName(u"overwiewWidget")
        sizePolicy1.setHeightForWidth(self.overwiewWidget.sizePolicy().hasHeightForWidth())
        self.overwiewWidget.setSizePolicy(sizePolicy1)
        self.overwiewWidget.setMinimumSize(QSize(274, 274))
        self.overwiewWidget.setMaximumSize(QSize(548, 16777215))
        self.overwiew_layout = QHBoxLayout(self.overwiewWidget)
        self.overwiew_layout.setSpacing(0)
        self.overwiew_layout.setObjectName(u"overwiew_layout")
        self.overwiew_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.overwiew_layout.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.overwiewWidget, 0, 1, 2, 1)

        self.maincontentWidget = QWidget(self.centralwidget)
        self.maincontentWidget.setObjectName(u"maincontentWidget")
        self.horizontalLayout = QHBoxLayout(self.maincontentWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.scrollArea = QScrollArea(self.maincontentWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(520, 430))
        self.scrollArea.setMaximumSize(QSize(520, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 518, 428))
        self.scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.scroll_layout.setSpacing(5)
        self.scroll_layout.setObjectName(u"scroll_layout")
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.maincontentWidget, 1, 0, 1, 1)

        self.pagesWidget = QWidget(self.centralwidget)
        self.pagesWidget.setObjectName(u"pagesWidget")

        self.gridLayout.addWidget(self.pagesWidget, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 22))
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

