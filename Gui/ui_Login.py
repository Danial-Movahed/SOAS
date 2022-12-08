# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LoginText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.LoginText.setFont(font)
        self.LoginText.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginText.setObjectName("LoginText")
        self.verticalLayout.addWidget(self.LoginText)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.LoginUsername = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LoginUsername.setFont(font)
        self.LoginUsername.setObjectName("LoginUsername")
        self.verticalLayout.addWidget(self.LoginUsername)
        self.LoginPassword = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LoginPassword.setFont(font)
        self.LoginPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LoginPassword.setObjectName("LoginPassword")
        self.verticalLayout.addWidget(self.LoginPassword)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.LoginQuitBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginQuitBtn.sizePolicy().hasHeightForWidth())
        self.LoginQuitBtn.setSizePolicy(sizePolicy)
        self.LoginQuitBtn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LoginQuitBtn.setFont(font)
        self.LoginQuitBtn.setStyleSheet("background-color:  rgb(255, 0, 4);")
        self.LoginQuitBtn.setObjectName("LoginQuitBtn")
        self.horizontalLayout.addWidget(self.LoginQuitBtn)
        spacerItem3 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.LoginContinueBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginContinueBtn.sizePolicy().hasHeightForWidth())
        self.LoginContinueBtn.setSizePolicy(sizePolicy)
        self.LoginContinueBtn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.LoginContinueBtn.setFont(font)
        self.LoginContinueBtn.setStyleSheet("background-color: rgb(69, 255, 12);")
        self.LoginContinueBtn.setObjectName("LoginContinueBtn")
        self.horizontalLayout.addWidget(self.LoginContinueBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoginText.setText(_translate("MainWindow", "Enter username and password:"))
        self.LoginUsername.setPlaceholderText(_translate("MainWindow", "Username:"))
        self.LoginPassword.setPlaceholderText(_translate("MainWindow", "Password:"))
        self.LoginQuitBtn.setText(_translate("MainWindow", "Quit"))
        self.LoginContinueBtn.setText(_translate("MainWindow", "Continue"))
