from .include import *
from . import ui_ShowAd, ui_RequestPrice


class RequestPrice(QDialog, ui_RequestPrice.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.status = False
        self.buttonBox.buttons()[0].clicked.connect(lambda: self.__Ok())
        self.show()

    def __Ok(self):
        self.status = True


class ShowAd(QMainWindow, ui_ShowAd.Ui_MainWindow):
    def __init__(self, title, username):
        super().__init__()
        self.setupUi(self)
        self.title = title
        self.username = username
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
        self.CloseBtn.clicked.connect(lambda: self.close())
        self.RequestBtn.clicked.connect(lambda: self.__Request())
        if self.Ad[10]:
            self.CloseBtn.setEnabled(False)
            self.RequestBtn.setEnabled(False)
            self.Writer.setText(self.Writer.text()+" / Sold Out")
        self.show()

    def __Request(self):
        self.Dlg = RequestPrice()
        self.Dlg.exec()
        if self.Dlg.status:
            try:
                DBConnection.execute(RequestTable.insert().values(
                    Title = self.title,
                    Details = self.Dlg.Details.toPlainText(),
                    Price = self.Dlg.Price.text(),
                    Username = self.username,
                    To = self.Ad[2],
                    Status = "Waiting",
                    Id = self.username+self.title
                ))
            except:
                errDlg = ErrorDialog("You already have sent your request!")
                errDlg.exec()
