# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/ShowAdAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(967, 600)
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
        self.AdTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.AdTitle.setFont(font)
        self.AdTitle.setObjectName("AdTitle")
        self.verticalLayout.addWidget(self.AdTitle)
        self.AdMessage = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AdMessage.setFont(font)
        self.AdMessage.setObjectName("AdMessage")
        self.verticalLayout.addWidget(self.AdMessage)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.StoreRoomLine = QtWidgets.QLineEdit(self.centralwidget)
        self.StoreRoomLine.setReadOnly(True)
        self.StoreRoomLine.setObjectName("StoreRoomLine")
        self.verticalLayout_9.addWidget(self.StoreRoomLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.ParkingLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ParkingLine.setReadOnly(True)
        self.ParkingLine.setObjectName("ParkingLine")
        self.verticalLayout_10.addWidget(self.ParkingLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.MeterSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.MeterSpin.setReadOnly(True)
        self.MeterSpin.setMaximum(1000)
        self.MeterSpin.setObjectName("MeterSpin")
        self.verticalLayout_4.addWidget(self.MeterSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.RoomSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.RoomSpin.setReadOnly(True)
        self.RoomSpin.setObjectName("RoomSpin")
        self.verticalLayout_5.addWidget(self.RoomSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.YearSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.YearSpin.setReadOnly(True)
        self.YearSpin.setObjectName("YearSpin")
        self.verticalLayout_6.addWidget(self.YearSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.CityPartLine = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CityPartLine.sizePolicy().hasHeightForWidth())
        self.CityPartLine.setSizePolicy(sizePolicy)
        self.CityPartLine.setReadOnly(True)
        self.CityPartLine.setObjectName("CityPartLine")
        self.verticalLayout_3.addWidget(self.CityPartLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.FloorSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.FloorSpin.setReadOnly(True)
        self.FloorSpin.setMaximum(1000)
        self.FloorSpin.setObjectName("FloorSpin")
        self.verticalLayout_7.addWidget(self.FloorSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.RentLabel = QtWidgets.QLabel(self.centralwidget)
        self.RentLabel.setObjectName("RentLabel")
        self.verticalLayout_12.addWidget(self.RentLabel)
        self.RentPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.RentPrice.setReadOnly(True)
        self.RentPrice.setObjectName("RentPrice")
        self.verticalLayout_12.addWidget(self.RentPrice)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.SellLabel = QtWidgets.QLabel(self.centralwidget)
        self.SellLabel.setObjectName("SellLabel")
        self.verticalLayout_8.addWidget(self.SellLabel)
        self.SellPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SellPrice.setReadOnly(True)
        self.SellPrice.setObjectName("SellPrice")
        self.verticalLayout_8.addWidget(self.SellPrice)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.MortLabel = QtWidgets.QLabel(self.centralwidget)
        self.MortLabel.setObjectName("MortLabel")
        self.verticalLayout_11.addWidget(self.MortLabel)
        self.MortPrice = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.MortPrice.setReadOnly(True)
        self.MortPrice.setObjectName("MortPrice")
        self.verticalLayout_11.addWidget(self.MortPrice)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show House - SOAS"))
        self.AdTitle.setText(_translate("MainWindow", "Title"))
        self.label_6.setText(_translate("MainWindow", "Have Store Room?"))
        self.label_7.setText(_translate("MainWindow", "Have Parking?"))
        self.label_2.setText(_translate("MainWindow", "Meters"))
        self.label_3.setText(_translate("MainWindow", "Rooms"))
        self.label_4.setText(_translate("MainWindow", "Year of construction"))
        self.label.setText(_translate("MainWindow", "City Part"))
        self.label_5.setText(_translate("MainWindow", "Floor"))
        self.RentLabel.setText(_translate("MainWindow", "Rent Price"))
        self.SellLabel.setText(_translate("MainWindow", "Sell Price"))
        self.MortLabel.setText(_translate("MainWindow", "Mortgage Price"))
        self.Writer.setText(_translate("MainWindow", "TextLabel"))
