# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/ViewRequest.ui'
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.verticalLayout.addWidget(self.Title)
        self.Details = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Details.setFont(font)
        self.Details.setObjectName("Details")
        self.verticalLayout.addWidget(self.Details)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.BuyLab = QtWidgets.QLabel(self.centralwidget)
        self.BuyLab.setObjectName("BuyLab")
        self.verticalLayout_7.addWidget(self.BuyLab)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BuyPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BuyPrice.sizePolicy().hasHeightForWidth())
        self.BuyPrice.setSizePolicy(sizePolicy)
        self.BuyPrice.setReadOnly(True)
        self.BuyPrice.setObjectName("BuyPrice")
        self.horizontalLayout.addWidget(self.BuyPrice)
        self.BuyBil = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BuyBil.setFont(font)
        self.BuyBil.setObjectName("BuyBil")
        self.horizontalLayout.addWidget(self.BuyBil)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.MortLab = QtWidgets.QLabel(self.centralwidget)
        self.MortLab.setObjectName("MortLab")
        self.verticalLayout_7.addWidget(self.MortLab)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.MortPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MortPrice.sizePolicy().hasHeightForWidth())
        self.MortPrice.setSizePolicy(sizePolicy)
        self.MortPrice.setReadOnly(True)
        self.MortPrice.setObjectName("MortPrice")
        self.horizontalLayout_3.addWidget(self.MortPrice)
        self.MortMil = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MortMil.setFont(font)
        self.MortMil.setObjectName("MortMil")
        self.horizontalLayout_3.addWidget(self.MortMil)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.RentLab = QtWidgets.QLabel(self.centralwidget)
        self.RentLab.setObjectName("RentLab")
        self.verticalLayout_7.addWidget(self.RentLab)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.RentPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RentPrice.sizePolicy().hasHeightForWidth())
        self.RentPrice.setSizePolicy(sizePolicy)
        self.RentPrice.setReadOnly(True)
        self.RentPrice.setObjectName("RentPrice")
        self.horizontalLayout_4.addWidget(self.RentPrice)
        self.RentMil = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RentMil.setFont(font)
        self.RentMil.setObjectName("RentMil")
        self.horizontalLayout_4.addWidget(self.RentMil)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.Writer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Writer.setFont(font)
        self.Writer.setObjectName("Writer")
        self.verticalLayout.addWidget(self.Writer)
        self.verticalLayout_2.addLayout(self.verticalLayout)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "View Request - SOAS"))
        self.Title.setText(_translate("MainWindow", "Title"))
        self.BuyLab.setText(_translate("MainWindow", "Buy Price"))
        self.BuyBil.setText(_translate("MainWindow", "Billion"))
        self.MortLab.setText(_translate("MainWindow", "Mortage Price"))
        self.MortMil.setText(_translate("MainWindow", "Million"))
        self.RentLab.setText(_translate("MainWindow", "Rent Price"))
        self.RentMil.setText(_translate("MainWindow", "Million"))
        self.Writer.setText(_translate("MainWindow", "TextLabel"))
