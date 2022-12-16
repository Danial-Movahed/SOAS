from .include import *
from . import ui_MyAds,EditCreateAd

class MyAds(QMainWindow, ui_MyAds.Ui_MainWindow):
    def __init__(self,username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.NewAd.clicked.connect(lambda: self.__NewAd())
        self.EditAd.clicked.connect(lambda: self.__EditAd())
        self.DeleteAd.clicked.connect(lambda: self.__DeleteAd())
        self.show()
    def __NewAd(self):
        self.NewAdWnd = EditCreateAd.EditCreateAd(self.username)
    def __EditAd(self):
        self.EditAdWnd = EditCreateAd.EditCreateAd(self.username)
    def __DeleteAd(self):
        pass