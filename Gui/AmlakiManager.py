from .include import *
from . import ui_AmlakiManager,MyAds


class AmlakiManager(QMainWindow, ui_AmlakiManager.Ui_MainWindow):
    def __init__(self,username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.AmlakiMgmt.clicked.connect(lambda: self.OpenAmlakiMgmt())
        self.__refresh()
        self.MyAds.clicked.connect(lambda: self.__MyAds())
        self.SearchBtn.clicked.connect(lambda: self.__Search())
        self.show()

    def __refresh(self):
        self.AdList.clear()
        for x in DBConnection.execute(AdTable.select()).fetchall():
            if x[2] != self.username[0]:
                self.AdList.addItem(x[0])

    def __FixReturn(self, s):
        if s == "Not selected" or s == 0:
            return None
        return s
    
    def __MyAds(self):
        self.MyAdsWnd = MyAds.MyAds(self.username)

    def __Search(self):
        self.AdList.clear()
        Floor = self.__FixReturn(self.FloorCombo.currentText())
        CityPart = self.__FixReturn(self.CityPartCombo.currentText())
        Year = self.__FixReturn(self.YearCombo.currentText())
        Room = self.__FixReturn(self.RoomSpin.value())
        Meter = self.__FixReturn(self.MeterSpin.value())
        Parking = self.__FixReturn(self.ParkingCombo.currentText())
        Store = self.__FixReturn(self.StoreCombo.currentText())
        for x in DBConnection.execute(AdTable.select().where(
            ((Floor == None) or (AdTable.c.Floor == Floor)),
            ((CityPart == None) or (AdTable.c.CityPart == CityPart)),
            ((Year == None) or (AdTable.c.YearsOld == Year)),
            ((Room == None) or (AdTable.c.Room == Room)),
            ((Meter == None) or (AdTable.c.Meter == Meter)),
            ((Parking == None) or (AdTable.c.HasParking == Parking)),
            ((Store == None) or (AdTable.c.HasStoreroom == Store))
        )):
            if x[2]!=self.username[0]:
                self.AdList.addItem(x[0])

    def OpenAmlakiMgmt(self):
        self.err = ErrorDialog(
            "You do not have the permission to open amlaki management!", self)
        self.err.exec()
