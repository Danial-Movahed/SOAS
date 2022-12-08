from hashlib import blake2s
from sqlalchemy import Column, Boolean, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, make_transient
from sqlalchemy import create_engine
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import socket
import threading
import select
import pickle

Base = declarative_base()

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

class Agahi(Base):
    __tablename__ = "Agahi"
    Title = Column(String(), primary_key=True, nullable=False)
    Message = Column(String(), nullable=False)
    Writer = Column(String(), nullable=False)
    CityPart= Column(String(), nullable=False)
    Meter = Column(String(), nullable=False)
    Room = Column(String(), nullable=False)
    YearsOld = Column(String(), nullable=False)
    Floor = Column(String(), nullable=False)
    HasParking = Column(String(), nullable=False)
    HasStoreroom = Column(String(), nullable=False)
class User(Base):
    __tablename__ = "User"
    Username = Column(String(), primary_key=True, nullable=False)
    Password = Column(String(), nullable=False)
    isAdmin = Column(Boolean(), nullable=False)

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
