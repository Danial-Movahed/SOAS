# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogingwQFer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.7
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LoginText = QLabel(self.centralwidget)
        self.LoginText.setObjectName(u"LoginText")
        font = QFont()
        font.setPointSize(21)
        self.LoginText.setFont(font)
        self.LoginText.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.LoginText)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.LoginUsername = QLineEdit(self.centralwidget)
        self.LoginUsername.setObjectName(u"LoginUsername")
        font1 = QFont()
        font1.setPointSize(15)
        self.LoginUsername.setFont(font1)

        self.verticalLayout.addWidget(self.LoginUsername)

        self.LoginPassword = QLineEdit(self.centralwidget)
        self.LoginPassword.setObjectName(u"LoginPassword")
        self.LoginPassword.setFont(font1)
        self.LoginPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.LoginPassword)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.LoginQuitBtn = QPushButton(self.centralwidget)
        self.LoginQuitBtn.setObjectName(u"LoginQuitBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginQuitBtn.sizePolicy().hasHeightForWidth())
        self.LoginQuitBtn.setSizePolicy(sizePolicy)
        self.LoginQuitBtn.setMaximumSize(QSize(16777215, 100))
        self.LoginQuitBtn.setFont(font1)
        self.LoginQuitBtn.setStyleSheet(u"background-color:  rgb(255, 0, 4);")

        self.horizontalLayout.addWidget(self.LoginQuitBtn)

        self.horizontalSpacer = QSpacerItem(130, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.LoginContinueBtn = QPushButton(self.centralwidget)
        self.LoginContinueBtn.setObjectName(u"LoginContinueBtn")
        sizePolicy.setHeightForWidth(self.LoginContinueBtn.sizePolicy().hasHeightForWidth())
        self.LoginContinueBtn.setSizePolicy(sizePolicy)
        self.LoginContinueBtn.setMaximumSize(QSize(16777215, 100))
        self.LoginContinueBtn.setFont(font1)
        self.LoginContinueBtn.setStyleSheet(u"background-color: rgb(69, 255, 12);")

        self.horizontalLayout.addWidget(self.LoginContinueBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LoginText.setText(QCoreApplication.translate("MainWindow", u"Enter username and password:", None))
        self.LoginUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.LoginPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.LoginQuitBtn.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.LoginContinueBtn.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
    # retranslateUi

