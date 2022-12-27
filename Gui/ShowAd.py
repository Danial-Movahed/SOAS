from .include import *
from . import ui_ShowAd, RequestPrice, RequestPriceRent

class ShowAd(QMainWindow, ui_ShowAd.Ui_MainWindow):
    def __init__(self, title, username):
        super().__init__()
        self.setupUi(self)
        self.title = title
        self.username = username
        self.House = DBConnection.execute(HouseTable.select().where(
            HouseTable.c.Title == title)).fetchall()[0]
        self.AdTitle.setText(self.House[0])
        self.AdMessage.setText(self.House[1])
        self.Writer.setText("Owned by: "+self.House[2])
        self.StoreRoomLine.setText(self.House[9])
        self.ParkingLine.setText(self.House[8])
        self.MeterSpin.setValue(int(self.House[4]))
        self.CityPartLine.setText(self.House[3])
        self.RoomSpin.setValue(int(self.House[5]))
        self.YearSpin.setValue(int(self.House[6]))
        self.FloorSpin.setValue(int(self.House[7]))
        self.CloseBtn.clicked.connect(lambda: self.close())
        self.RequestBtn.clicked.connect(lambda: self.__Request())
        if self.House[12]:
            self.Writer.setText("For Rent!\n"+self.Writer.text())
            self.RequestBtn.setText("Rent!")
            self.SellPrice.hide()
            self.SellLabel.hide()
            self.MortPrice.setValue(self.House[14])
            self.RentPrice.setValue(self.House[15])
        else:
            self.Writer.setText("For Sale!\n"+self.Writer.text())
            self.RequestBtn.setText("Buy!")
            self.MortPrice.hide()
            self.MortLabel.hide()
            self.RentPrice.hide()
            self.RentLabel.hide()
            self.SellPrice.setValue(self.House[13])
        
        self.show()

    def __Request(self):
        if self.House[12]:
            self.Dlg = RequestPriceRent.RequestPriceRent(self.House[14], self.House[15])
            self.Dlg.exec()
            if self.Dlg.status:
                try:
                    DBConnection.execute(RequestTable.insert().values(
                        Title = self.title,
                        Details = self.Dlg.Details.toPlainText(),
                        MortPrice = self.Dlg.MortSpin.value(),
                        RentPrice = self.Dlg.RentSpin.value(),
                        Price = 0,
                        Username = self.username,
                        To = self.House[2],
                        Id = self.username+self.title
                    ))
                except:
                    errDlg = ErrorDialog("You already have sent your request!")
                    errDlg.exec()
            return

        self.Dlg = RequestPrice.RequestPrice(self.House[13])
        self.Dlg.exec()
        if self.Dlg.status:
            try:
                DBConnection.execute(RequestTable.insert().values(
                    Title = self.title,
                    Details = self.Dlg.Details.toPlainText(),
                    Price = self.Dlg.Price.value(),
                    MortPrice = 0,
                    RentPrice = 0,
                    Username = self.username,
                    To = self.House[2],
                    Id = self.username+self.title
                ))
            except:
                errDlg = ErrorDialog("You already have sent your request!")
                errDlg.exec()
