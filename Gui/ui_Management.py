# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/Management.ui'
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.UsersTab = QtWidgets.QWidget()
        self.UsersTab.setObjectName("UsersTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.UsersTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(10, 10, 10, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.UsersTable = QtWidgets.QTableWidget(self.UsersTab)
        self.UsersTable.setObjectName("UsersTable")
        self.UsersTable.setColumnCount(4)
        self.UsersTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.UsersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.UsersTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.UsersTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.UsersTable.setHorizontalHeaderItem(3, item)
        self.verticalLayout_6.addWidget(self.UsersTable)
        self.DeleteUserBtn = QtWidgets.QPushButton(self.UsersTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteUserBtn.sizePolicy().hasHeightForWidth())
        self.DeleteUserBtn.setSizePolicy(sizePolicy)
        self.DeleteUserBtn.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DeleteUserBtn.setFont(font)
        self.DeleteUserBtn.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.DeleteUserBtn.setObjectName("DeleteUserBtn")
        self.verticalLayout_6.addWidget(self.DeleteUserBtn)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.UsersTab, "")
        self.Houses = QtWidgets.QWidget()
        self.Houses.setObjectName("Houses")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Houses)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(10, 10, 10, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.HouseTable = QtWidgets.QTableWidget(self.Houses)
        self.HouseTable.setObjectName("HouseTable")
        self.HouseTable.setColumnCount(4)
        self.HouseTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.HouseTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.HouseTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.HouseTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.HouseTable.setHorizontalHeaderItem(3, item)
        self.verticalLayout_8.addWidget(self.HouseTable)
        self.DeleteHouseBtn = QtWidgets.QPushButton(self.Houses)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteHouseBtn.sizePolicy().hasHeightForWidth())
        self.DeleteHouseBtn.setSizePolicy(sizePolicy)
        self.DeleteHouseBtn.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DeleteHouseBtn.setFont(font)
        self.DeleteHouseBtn.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.DeleteHouseBtn.setObjectName("DeleteHouseBtn")
        self.verticalLayout_8.addWidget(self.DeleteHouseBtn)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.Houses, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Management - SOAS"))
        item = self.UsersTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Username"))
        item = self.UsersTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Verified?"))
        item = self.UsersTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Admin?"))
        item = self.UsersTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        self.DeleteUserBtn.setText(_translate("MainWindow", "Delete User"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UsersTab), _translate("MainWindow", "Users"))
        item = self.HouseTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.HouseTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Verified?"))
        item = self.HouseTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "For Sale?"))
        item = self.HouseTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "For Rent?"))
        self.DeleteHouseBtn.setText(_translate("MainWindow", "Delete House"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Houses), _translate("MainWindow", "Houses"))
