# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/EditCreateAd.ui'
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
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.AdTitle = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.AdTitle.setFont(font)
        self.AdTitle.setObjectName("AdTitle")
        self.verticalLayout.addWidget(self.AdTitle)
        self.AdMessage = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AdMessage.setFont(font)
        self.AdMessage.setObjectName("AdMessage")
        self.verticalLayout.addWidget(self.AdMessage)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.StoreCombo = QtWidgets.QComboBox(self.centralwidget)
        self.StoreCombo.setObjectName("StoreCombo")
        self.StoreCombo.addItem("")
        self.StoreCombo.addItem("")
        self.StoreCombo.addItem("")
        self.verticalLayout_9.addWidget(self.StoreCombo)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.ParkingCombo = QtWidgets.QComboBox(self.centralwidget)
        self.ParkingCombo.setObjectName("ParkingCombo")
        self.ParkingCombo.addItem("")
        self.ParkingCombo.addItem("")
        self.ParkingCombo.addItem("")
        self.verticalLayout_10.addWidget(self.ParkingCombo)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.MeterSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.MeterSpin.setObjectName("MeterSpin")
        self.verticalLayout_4.addWidget(self.MeterSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.RoomSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.RoomSpin.setObjectName("RoomSpin")
        self.verticalLayout_5.addWidget(self.RoomSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.YearLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YearLineEdit.sizePolicy().hasHeightForWidth())
        self.YearLineEdit.setSizePolicy(sizePolicy)
        self.YearLineEdit.setObjectName("YearLineEdit")
        self.verticalLayout_6.addWidget(self.YearLineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.CityPartCombo = QtWidgets.QComboBox(self.centralwidget)
        self.CityPartCombo.setObjectName("CityPartCombo")
        self.CityPartCombo.addItem("")
        self.CityPartCombo.addItem("")
        self.CityPartCombo.addItem("")
        self.CityPartCombo.addItem("")
        self.CityPartCombo.addItem("")
        self.verticalLayout_3.addWidget(self.CityPartCombo)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.FloorSpin = QtWidgets.QSpinBox(self.centralwidget)
        self.FloorSpin.setObjectName("FloorSpin")
        self.verticalLayout_7.addWidget(self.FloorSpin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CancelBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelBtn.sizePolicy().hasHeightForWidth())
        self.CancelBtn.setSizePolicy(sizePolicy)
        self.CancelBtn.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(15)
        self.CancelBtn.setFont(font)
        self.CancelBtn.setStyleSheet("background-color: rgb(216, 0, 4);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.CancelBtn.setObjectName("CancelBtn")
        self.horizontalLayout.addWidget(self.CancelBtn)
        self.SaveBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveBtn.sizePolicy().hasHeightForWidth())
        self.SaveBtn.setSizePolicy(sizePolicy)
        self.SaveBtn.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SaveBtn.setFont(font)
        self.SaveBtn.setStyleSheet("background-color: rgb(5, 163, 55);\n"
"border-radius: 10px;\n"
"padding: 0px 5px;")
        self.SaveBtn.setObjectName("SaveBtn")
        self.horizontalLayout.addWidget(self.SaveBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.AdTitle.setPlaceholderText(_translate("MainWindow", "Ad title"))
        self.AdMessage.setPlaceholderText(_translate("MainWindow", "Ad message"))
        self.label_7.setText(_translate("MainWindow", "Has store room?"))
        self.StoreCombo.setItemText(0, _translate("MainWindow", "Not selected"))
        self.StoreCombo.setItemText(1, _translate("MainWindow", "Yes"))
        self.StoreCombo.setItemText(2, _translate("MainWindow", "No"))
        self.label_8.setText(_translate("MainWindow", "Has parking?"))
        self.ParkingCombo.setItemText(0, _translate("MainWindow", "Not selected"))
        self.ParkingCombo.setItemText(1, _translate("MainWindow", "Yes"))
        self.ParkingCombo.setItemText(2, _translate("MainWindow", "No"))
        self.label_2.setText(_translate("MainWindow", "Meters"))
        self.label_3.setText(_translate("MainWindow", "Rooms"))
        self.label_4.setText(_translate("MainWindow", "Year of construction"))
        self.label.setText(_translate("MainWindow", "City Part"))
        self.CityPartCombo.setItemText(0, _translate("MainWindow", "Not selected"))
        self.CityPartCombo.setItemText(1, _translate("MainWindow", "North"))
        self.CityPartCombo.setItemText(2, _translate("MainWindow", "South"))
        self.CityPartCombo.setItemText(3, _translate("MainWindow", "East"))
        self.CityPartCombo.setItemText(4, _translate("MainWindow", "West"))
        self.label_5.setText(_translate("MainWindow", "Floor"))
        self.CancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.SaveBtn.setText(_translate("MainWindow", "Save"))
from . import bg_rc
