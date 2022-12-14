from .include import *
from . import ui_ShowAdAdmin


class ShowAdAdmin(QMainWindow, ui_ShowAdAdmin.Ui_MainWindow):
    def __init__(self, title):
        super().__init__()
        self.setupUi(self)
        self.title = title
        self.Ad = DBConnection.execute(AdTable.select().where(
            AdTable.c.Title == title)).fetchall()[0]
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
        if self.Ad[10]:
            self.CloseBtn.setEnabled(False)
            self.RequestBtn.setEnabled(False)
            self.Writer.setText(self.Writer.text()+" / Sold Out")
        self.show()