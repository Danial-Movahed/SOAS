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
        self.NewAdWnd.closeEvent = self.__refresh  # type: ignore
    def __EditAd(self):
        if len(self.MyAdList.selectedItems())==0:
            errdlg = ErrorDialog("Please select an ad!", self)
            errdlg.exec()
            return
        self.EditAdWnd = EditCreateAd.EditCreateAd(self.username,self.MyAdList.selectedItems()[0].text())
        self.EditAdWnd.closeEvent = self.__refresh  # type: ignore
    def __DeleteAd(self):
        if len(self.MyAdList.selectedItems())==0:
            errdlg = ErrorDialog("Please select an ad!", self)
            errdlg.exec()
            return
        self.dlg = CDialog(
            "Are you sure you want to delete this ad?", "Question!", self)
        if self.dlg.exec():
            DBConnection.execute(AdTable.delete().where(AdTable.c.Title == self.MyAdList.selectedItems()[0].text()))
        self.__refresh()
    def __refresh(self,e=None):
        self.MyAdList.clear()
        for x in DBConnection.execute(AdTable.select()).fetchall():
            if x[2] == self.username[0]:
                self.MyAdList.addItem(x[0])