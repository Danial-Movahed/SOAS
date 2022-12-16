from .include import *
from . import ui_AmlakiManager,MyAds


class AmlakiManager(QMainWindow, ui_AmlakiManager.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AmlakiMgmt.clicked.connect(lambda: self.OpenAmlakiMgmt())
        # DBConnection.execute(AdTable.insert().values(Title = "test1"))
        self.AdList.addItems(
            [x[0] for x in DBConnection.execute(AdTable.select()).fetchall()])
        self.MyAds.clicked.connect(lambda: self.__MyAds())
        self.SearchBtn.clicked.connect(lambda: self.__Search())
        self.show()

    def __FixReturn(self, s):
        if s == "Not selected" or s == 0:
            return None
        return s
    
    def __MyAds(self):
        self.MyAdsWnd = MyAds.MyAds()

    def __Search(self):
        self.AdList.clear()
        Floor = self.__FixReturn(self.FloorCombo.currentText())
        CityPart = self.__FixReturn(self.CityPartCombo.currentText())
        Year = self.__FixReturn(self.YearCombo.currentText())
        Room = self.__FixReturn(self.RoomSpin.value())
        Meter = self.__FixReturn(self.MeterSpin.value())
        Parking = None
        Store = None
        if self.ParkingCombo.currentText() == "Yes":
            Parking = True
        elif self.ParkingCombo.currentText() == "No":
            Parking = False
        if self.StoreCombo.currentText() == "Yes":
            Store = True
        elif self.StoreCombo.currentText() == "No":
            Store = False
        self.AdList.addItems([x[0] for x in DBConnection.execute(AdTable.select().where((AdTable.c.Floor == Floor) & 
        (AdTable.c.CityPart == CityPart) & 
        (AdTable.c.YearsOld == Year) & 
        (AdTable.c.Room == Room) & 
        (AdTable.c.Meter == Meter) & 
        (AdTable.c.HasParking == Parking) & 
        (AdTable.c.HasStoreroom == Store)))])

    def OpenAmlakiMgmt(self):
        self.err = ErrorDialog(
            "You do not have the permission to open amlaki management!", self)
        self.err.exec()
