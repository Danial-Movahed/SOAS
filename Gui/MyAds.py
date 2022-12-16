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
        self.__refresh()
        self.show()
    def __NewAd(self):
        self.NewAdWnd = EditCreateAd.EditCreateAd(self.username)
        self.NewAdWnd.closeEvent = self.__refresh
    def __EditAd(self):
        self.EditAdWnd = EditCreateAd.EditCreateAd(self.username)
        self.NewAdWnd.closeEvent = self.__refresh
    def __DeleteAd(self):
        pass
    def __refresh(self,e=None):
        self.MyAdList.clear()
        for x in DBConnection.execute(AdTable.select()).fetchall():
            if x[2] == self.username[0]:
                self.MyAdList.addItem(x[0])