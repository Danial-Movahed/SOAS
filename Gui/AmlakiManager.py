from .include import *
from . import MyAds,ui_AmlakiManager

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

    def __refresh(self,e=None):
        self.AdList.clear()
        self.FloorCombo.clear()
        self.CityPartCombo.clear()
        self.YearCombo.clear()
        self.RoomCombo.clear()
        self.MeterCombo.clear()
        self.ParkingCombo.clear()
        self.StoreCombo.clear()
        self.CityPartCombo.addItem("Not selected")
        self.MeterCombo.addItem("Not selected")
        self.RoomCombo.addItem("Not selected")
        self.YearCombo.addItem("Not selected")
        self.FloorCombo.addItem("Not selected")
        self.ParkingCombo.addItem("Not selected")
        self.StoreCombo.addItem("Not selected")
        for x in DBConnection.execute(AdTable.select()).fetchall():
            # if x[2] != self.username[0]:
                self.AdList.addItem(x[0])
                self.CityPartCombo.addItem(x[3])
                self.MeterCombo.addItem(x[4])
                self.RoomCombo.addItem(x[5])
                self.YearCombo.addItem(x[6])
                self.FloorCombo.addItem(x[7])
                self.ParkingCombo.addItem(x[8])
                self.StoreCombo.addItem(x[9])

    def __FixReturn(self, s):
        if s == "Not selected":
            return None
        return s
    
    def __MyAds(self):
        self.MyAdsWnd = MyAds.MyAds(self.username)
        self.MyAdsWnd.closeEvent = self.__refresh

    def __Search(self):
        self.AdList.clear()
        Floor = self.__FixReturn(self.FloorCombo.currentText())
        CityPart = self.__FixReturn(self.CityPartCombo.currentText())
        Year = self.__FixReturn(self.YearCombo.currentText())
        Room = self.__FixReturn(self.RoomCombo.currentText())
        Meter = self.__FixReturn(self.MeterCombo.currentText())
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
