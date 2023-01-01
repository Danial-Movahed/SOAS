from .include import *
from . import ui_ShowAdAdmin


class ShowAdAdmin(QMainWindow, ui_ShowAdAdmin.Ui_MainWindow):
    def __init__(self, title):
        super().__init__()
        self.setupUi(self)
        self.title = title
        self.Ad = DBConnection.execute(HouseTable.select().where(
            HouseTable.c.Title == title)).fetchall()[0]
        self.AdTitle.setText(self.Ad[0])
        self.AdMessage.setText(self.Ad[1])
        self.Writer.setText("Owned by: "+self.Ad[2])
        self.StoreRoomLine.setText(self.Ad[9])
        self.ParkingLine.setText(self.Ad[8])
        self.MeterSpin.setValue(int(self.Ad[4]))
        self.CityPartLine.setText(self.Ad[3])
        self.RoomSpin.setValue(int(self.Ad[5]))
        self.YearSpin.setValue(int(self.Ad[6]))
        self.FloorSpin.setValue(int(self.Ad[7]))
        if self.Ad[12]:
            self.SellPrice.hide()
            self.SellLabel.hide()
            self.MortPrice.setValue(self.Ad[14])
            self.RentPrice.setValue(self.Ad[15])
        else:
            self.MortPrice.hide()
            self.MortLabel.hide()
            self.RentPrice.hide()
            self.RentLabel.hide()
            self.SellPrice.setValue(self.Ad[13])

        if self.Ad[10]:
            self.CloseBtn.setEnabled(False)
            self.RequestBtn.setEnabled(False)
            self.Writer.setText(self.Writer.text()+" / Sold Out")
        self.show()
