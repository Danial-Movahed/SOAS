from .include import *
from . import MyHouses, MyRequests, ShowAd, ui_AmlakiManager


class AmlakiManager(QMainWindow, ui_AmlakiManager.Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.AmlakiMgmt.clicked.connect(lambda: self.OpenAmlakiMgmt())
        self.MyAds.clicked.connect(lambda: self.__MyAds())
        self.SearchBtn.clicked.connect(lambda: self.__Search())
        self.MyReqs.clicked.connect(lambda: self.__MyReqs())
        self.MinBuySlider.valueChanged.connect(
            lambda: self.__ShowSliderValue())
        self.MaxBuySlider.valueChanged.connect(
            lambda: self.__ShowSliderValue())
        self.MinMortSlider.valueChanged.connect(
            lambda: self.__ShowSliderValue())
        self.MaxMortSlider.valueChanged.connect(
            lambda: self.__ShowSliderValue())
        self.MinRentSlider.valueChanged.connect(
            lambda: self.__ShowSliderValue())
        self.MaxRentSlider.valueChanged.connect(
            lambda: self.__ShowSliderValue())
        self.AdList.itemDoubleClicked.connect(self.__ViewAd)
        self.username = username[0]
        self.AmlakiMgmt.hide()
        self.__ShowSliderValue()
        self.refresh()
        self.show()

    def __ShowSliderValue(self):
        self.MinBuyLabel.setText(
            "Minimum Buying Price: "+str(self.MinBuySlider.value()/1000)+"B")
        self.MaxBuyLabel.setText(
            "Maximum Buying Price: "+str(self.MaxBuySlider.value()/1000)+"B")
        self.MinMortLabel.setText(
            "Minimum Mortgage Price: "+str(self.MinMortSlider.value())+"M")
        self.MaxMortLabel.setText(
            "Maximum Mortgage Price: "+str(self.MaxMortSlider.value())+"M")
        self.MinRentLabel.setText(
            "Minimum Rent Price: "+str(self.MinRentSlider.value())+"M")
        self.MaxRentLabel.setText(
            "Maximum Rent Price: "+str(self.MaxRentSlider.value())+"M")

    def __ViewAd(self, item):
        self.ShowAdWnd = ShowAd.ShowAd(item.text(), self.username)

    def __MyReqs(self):
        self.MyReqsWnd = MyRequests.MyRequests(self.username)
        self.MyReqsWnd.closeEvent = self.refresh

    def refresh(self, e=None):
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
        for x in DBConnection.execute(HouseTable.select().where(HouseTable.c.Owner != self.username, HouseTable.c.isVerified == True, HouseTable.c.isSale == True).order_by(HouseTable.c.Nice.desc())).fetchall():
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
        self.MyAdsWnd = MyHouses.MyHouses(self.username)
        self.MyAdsWnd.closeEvent = self.refresh

    def __Search(self):
        self.AdList.clear()
        Floor = self.__FixReturn(self.FloorCombo.currentText())
        CityPart = self.__FixReturn(self.CityPartCombo.currentText())
        Year = self.__FixReturn(self.YearCombo.currentText())
        Room = self.__FixReturn(self.RoomCombo.currentText())
        Meter = self.__FixReturn(self.MeterCombo.currentText())
        Parking = self.__FixReturn(self.ParkingCombo.currentText())
        Store = self.__FixReturn(self.StoreCombo.currentText())
        Mode = self.__FixReturn(self.ModeCombo.currentText())
        if Mode == "Rent":
            Mode = True
        elif Mode == "Buy":
            Mode = False
        self.AdList.addItems([x[0] for x in DBConnection.execute(HouseTable.select().where(
            ((Floor == None) or (HouseTable.c.Floor == Floor)),
            ((CityPart == None) or (HouseTable.c.CityPart == CityPart)),
            ((Year == None) or (HouseTable.c.YearsOld == Year)),
            ((Room == None) or (HouseTable.c.Room == Room)),
            ((Meter == None) or (HouseTable.c.Meter == Meter)),
            ((Parking == None) or (HouseTable.c.HasParking == Parking)),
            ((Store == None) or (HouseTable.c.HasStoreroom == Store)),
            ((Mode == None) or (HouseTable.c.Mode == Mode)),
            HouseTable.c.isVerified == True,
            HouseTable.c.Owner != self.username,
            HouseTable.c.isSale == True,
            HouseTable.c.SellPrice >= self.MinBuySlider.value()/1000,
            HouseTable.c.SellPrice <= self.MaxBuySlider.value()/1000,
            HouseTable.c.MortPrice >= self.MinMortSlider.value(),
            HouseTable.c.MortPrice <= self.MaxMortSlider.value(),
            HouseTable.c.RentPrice >= self.MinRentSlider.value(),
            HouseTable.c.RentPrice <= self.MaxRentSlider.value()
        ).order_by(HouseTable.c.Nice.desc()))])

    def OpenAmlakiMgmt(self):
        self.err = ErrorDialog(
            "You do not have the permission to open amlaki management!", self)
        self.err.exec()
