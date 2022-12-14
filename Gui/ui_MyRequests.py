# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/MyRequests.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.SentTab = QtWidgets.QWidget()
        self.SentTab.setObjectName("SentTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.SentTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SentRequests = QtWidgets.QTreeWidget(self.SentTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SentRequests.sizePolicy().hasHeightForWidth())
        self.SentRequests.setSizePolicy(sizePolicy)
        self.SentRequests.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.SentRequests.setObjectName("SentRequests")
        self.verticalLayout_2.addWidget(self.SentRequests)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(27)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DeleteSentRequestBtn = QtWidgets.QPushButton(self.SentTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteSentRequestBtn.sizePolicy().hasHeightForWidth())
        self.DeleteSentRequestBtn.setSizePolicy(sizePolicy)
        self.DeleteSentRequestBtn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DeleteSentRequestBtn.setFont(font)
        self.DeleteSentRequestBtn.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.DeleteSentRequestBtn.setObjectName("DeleteSentRequestBtn")
        self.horizontalLayout_2.addWidget(self.DeleteSentRequestBtn)
        self.ViewSentRequestBtn = QtWidgets.QPushButton(self.SentTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ViewSentRequestBtn.sizePolicy().hasHeightForWidth())
        self.ViewSentRequestBtn.setSizePolicy(sizePolicy)
        self.ViewSentRequestBtn.setMaximumSize(QtCore.QSize(16777215, 100))
        self.ViewSentRequestBtn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ViewSentRequestBtn.setFont(font)
        self.ViewSentRequestBtn.setStyleSheet("background-color: rgb(84, 110, 255);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.ViewSentRequestBtn.setObjectName("ViewSentRequestBtn")
        self.horizontalLayout_2.addWidget(self.ViewSentRequestBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.SentTab, "")
        self.ReceivedTab = QtWidgets.QWidget()
        self.ReceivedTab.setObjectName("ReceivedTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.ReceivedTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(25, 25, 25, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ReceivedRequests = QtWidgets.QTreeWidget(self.ReceivedTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReceivedRequests.sizePolicy().hasHeightForWidth())
        self.ReceivedRequests.setSizePolicy(sizePolicy)
        self.ReceivedRequests.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ReceivedRequests.setObjectName("ReceivedRequests")
        self.verticalLayout.addWidget(self.ReceivedRequests)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(27)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DeclineReceivedRequestBtn = QtWidgets.QPushButton(self.ReceivedTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeclineReceivedRequestBtn.sizePolicy().hasHeightForWidth())
        self.DeclineReceivedRequestBtn.setSizePolicy(sizePolicy)
        self.DeclineReceivedRequestBtn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DeclineReceivedRequestBtn.setFont(font)
        self.DeclineReceivedRequestBtn.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.DeclineReceivedRequestBtn.setObjectName("DeclineReceivedRequestBtn")
        self.horizontalLayout.addWidget(self.DeclineReceivedRequestBtn)
        self.ViewReceivedRequestBtn = QtWidgets.QPushButton(self.ReceivedTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ViewReceivedRequestBtn.sizePolicy().hasHeightForWidth())
        self.ViewReceivedRequestBtn.setSizePolicy(sizePolicy)
        self.ViewReceivedRequestBtn.setMaximumSize(QtCore.QSize(16777215, 100))
        self.ViewReceivedRequestBtn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ViewReceivedRequestBtn.setFont(font)
        self.ViewReceivedRequestBtn.setStyleSheet("background-color: rgb(84, 110, 255);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.ViewReceivedRequestBtn.setObjectName("ViewReceivedRequestBtn")
        self.horizontalLayout.addWidget(self.ViewReceivedRequestBtn)
        self.AcceptReceivedRequestBtn = QtWidgets.QPushButton(self.ReceivedTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AcceptReceivedRequestBtn.sizePolicy().hasHeightForWidth())
        self.AcceptReceivedRequestBtn.setSizePolicy(sizePolicy)
        self.AcceptReceivedRequestBtn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AcceptReceivedRequestBtn.setFont(font)
        self.AcceptReceivedRequestBtn.setStyleSheet("background-color: rgb(5, 163, 55);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.AcceptReceivedRequestBtn.setObjectName("AcceptReceivedRequestBtn")
        self.horizontalLayout.addWidget(self.AcceptReceivedRequestBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.ReceivedTab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 30))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SentRequests.headerItem().setText(0, _translate("MainWindow", "Title"))
        self.SentRequests.headerItem().setText(1, _translate("MainWindow", "Name"))
        self.SentRequests.headerItem().setText(2, _translate("MainWindow", "Details"))
        self.SentRequests.headerItem().setText(3, _translate("MainWindow", "Price"))
        self.SentRequests.headerItem().setText(4, _translate("MainWindow", "Status"))
        self.DeleteSentRequestBtn.setText(_translate("MainWindow", "Delete Request"))
        self.ViewSentRequestBtn.setText(_translate("MainWindow", "View Request"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SentTab), _translate("MainWindow", "Sent"))
        self.ReceivedRequests.headerItem().setText(0, _translate("MainWindow", "Title"))
        self.ReceivedRequests.headerItem().setText(1, _translate("MainWindow", "Name"))
        self.ReceivedRequests.headerItem().setText(2, _translate("MainWindow", "Details"))
        self.ReceivedRequests.headerItem().setText(3, _translate("MainWindow", "Price"))
        self.ReceivedRequests.headerItem().setText(4, _translate("MainWindow", "Status"))
        self.DeclineReceivedRequestBtn.setText(_translate("MainWindow", "Decline Request"))
        self.ViewReceivedRequestBtn.setText(_translate("MainWindow", "View Request"))
        self.AcceptReceivedRequestBtn.setText(_translate("MainWindow", "Accept Request"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ReceivedTab), _translate("MainWindow", "Received"))
