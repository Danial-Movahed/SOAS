from hashlib import blake2s
from sqlalchemy import Column, Boolean, String, create_engine, MetaData, Table, Integer, FLOAT
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import socket
import threading
import select
import pickle

class CDialog(QDialog):
    def __init__(self, label, Title, parent=None):
        super().__init__(parent)

        self.setWindowTitle(Title)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel(label)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class ErrorDialog(QDialog):
    def __init__(self, label, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Error!")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(lambda: self.close())
        self.layout = QVBoxLayout()
        message = QLabel(label)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


engine = create_engine('sqlite:///Database.db', echo = False)
meta = MetaData()
UsersTable = Table(
    'Users', meta, 
    Column('Username', String, primary_key=True), 
    Column('Password', String),
    Column('isAdmin', Boolean),
    Column('isVerified', Boolean),
)
HouseTable = Table(
    'Houses', meta, 
    Column("Title", String, primary_key=True),
    Column("Message", String),
    Column("Owner", String),
    Column("CityPart", String),
    Column("Meter", String),
    Column("Room", String),
    Column("YearsOld", String),
    Column("Floor", String),
    Column("HasParking", String),
    Column("HasStoreroom", String),
    Column("isVerified", Boolean),
    Column("isSale", Boolean),
    Column("Mode", Boolean),
    Column("SellPrice", FLOAT),
    Column("MortPrice", FLOAT),
    Column("RentPrice", FLOAT)
)
RequestTable = Table(
    'Reqs', meta, 
    Column("Title", String),
    Column("Details", String),
    Column("Price", String),
    Column("MortPrice", String),
    Column("RentPrice", String),
    Column("Username", String),
    Column("To", String),
    Column("Id", String, primary_key=True)
)
meta.create_all(engine)
DBConnection = engine.connect()