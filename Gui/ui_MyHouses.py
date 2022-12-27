# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/MyHouses.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(20, 20, 20, -1)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(19)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.AddHouse = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddHouse.sizePolicy().hasHeightForWidth())
        self.AddHouse.setSizePolicy(sizePolicy)
        self.AddHouse.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddHouse.setFont(font)
        self.AddHouse.setStyleSheet("background-color: rgb(5, 163, 55);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.AddHouse.setObjectName("AddHouse")
        self.verticalLayout.addWidget(self.AddHouse)
        self.EditHouse = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditHouse.sizePolicy().hasHeightForWidth())
        self.EditHouse.setSizePolicy(sizePolicy)
        self.EditHouse.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EditHouse.setFont(font)
        self.EditHouse.setStyleSheet("border-radius: 10px;\n"
"padding: 0px 5px;\n"
"background-color: rgb(5, 87, 163);")
        self.EditHouse.setObjectName("EditHouse")
        self.verticalLayout.addWidget(self.EditHouse)
        self.DeleteHouse = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteHouse.sizePolicy().hasHeightForWidth())
        self.DeleteHouse.setSizePolicy(sizePolicy)
        self.DeleteHouse.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DeleteHouse.setFont(font)
        self.DeleteHouse.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.DeleteHouse.setObjectName("DeleteHouse")
        self.verticalLayout.addWidget(self.DeleteHouse)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.MyAdList = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.MyAdList.setFont(font)
        self.MyAdList.setStyleSheet("background-color: #444;\n"
"border-radius:10px;")
        self.MyAdList.setObjectName("MyAdList")
        self.horizontalLayout.addWidget(self.MyAdList)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SaleBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaleBtn.sizePolicy().hasHeightForWidth())
        self.SaleBtn.setSizePolicy(sizePolicy)
        self.SaleBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SaleBtn.setFont(font)
        self.SaleBtn.setStyleSheet("background-color: rgb(111, 26, 172);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.SaleBtn.setObjectName("SaleBtn")
        self.horizontalLayout_2.addWidget(self.SaleBtn)
        self.RentBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RentBtn.sizePolicy().hasHeightForWidth())
        self.RentBtn.setSizePolicy(sizePolicy)
        self.RentBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.RentBtn.setFont(font)
        self.RentBtn.setStyleSheet("background-color: rgb(191, 0, 175);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.RentBtn.setObjectName("RentBtn")
        self.horizontalLayout_2.addWidget(self.RentBtn)
        self.DisableBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DisableBtn.sizePolicy().hasHeightForWidth())
        self.DisableBtn.setSizePolicy(sizePolicy)
        self.DisableBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DisableBtn.setFont(font)
        self.DisableBtn.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.DisableBtn.setObjectName("DisableBtn")
        self.horizontalLayout_2.addWidget(self.DisableBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Houses - SOAS"))
        self.AddHouse.setText(_translate("MainWindow", "Add House"))
        self.EditHouse.setText(_translate("MainWindow", "Edit House"))
        self.DeleteHouse.setText(_translate("MainWindow", "Delete House"))
        self.SaleBtn.setText(_translate("MainWindow", "Set for sale"))
        self.RentBtn.setText(_translate("MainWindow", "Set for rent"))
        self.DisableBtn.setText(_translate("MainWindow", "Disable everything"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
from . import bg_rc
