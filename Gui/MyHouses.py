from .include import *
from . import EditCreateHouse, ui_MyHouses, RequestPrice, RequestPriceRent


class MyHouses(QMainWindow, ui_MyHouses.Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.AddHouse.clicked.connect(lambda: self.__AddHouse())
        self.EditHouse.clicked.connect(lambda: self.__EditHouse())
        self.DeleteHouse.clicked.connect(lambda: self.__DeleteHouse())
        self.RentBtn.clicked.connect(lambda: self.__SetRent())
        self.SaleBtn.clicked.connect(lambda: self.__SetSale())
        self.DisableBtn.clicked.connect(lambda: self.__DisableEv())
        self.RentBtn.setEnabled(False)
        self.SaleBtn.setEnabled(False)
        self.DisableBtn.setEnabled(False)
        self.MyAdList.itemSelectionChanged.connect(self.__SetButton)
        self.__refresh()
        self.show()

    def __calcNiceSale(self):
        tmp = DBConnection.execute(HouseTable.select().where(HouseTable.c.Title == self.MyAdList.selectedItems()[0].text())).fetchall()[0]
        price=float(self.Dlg.Price.value())
        meter=int(tmp[4])
        room=int(tmp[5])
        year=int(tmp[6])
        floor=int(tmp[7])
        parking=tmp[8]
        store=tmp[9]
        if tmp[3] == "North":
            loc=4
        elif tmp[3] == "West":
            loc=3
        elif tmp[3] == "East":
            loc=2
        elif tmp[3] == "South":
            loc=1
        if parking:
            parking = 2
        else:
            parking = 1
        if store:
            store = 1.5
        else:
            store = 1
        floor/=2
        floor+=0.5
        if year != 0:
            nice = loc*room*parking*store*floor/(price/meter)*((year/5)+1)
        else:
            nice = loc*room*parking*store*floor*2/(price/meter)
        return nice

    def __calcNiceRent(self):
        tmp = DBConnection.execute(HouseTable.select().where(HouseTable.c.Title == self.MyAdList.selectedItems()[0].text())).fetchall()[0]
        meter=int(tmp[4])
        room=int(tmp[5])
        year=int(tmp[6])
        floor=int(tmp[7])
        parking=tmp[8]
        store=tmp[9]
        if tmp[3] == "North":
            loc=16
        elif tmp[3] == "West":
            loc=9
        elif tmp[3] == "East":
            loc=4
        elif tmp[3] == "South":
            loc=1
        if parking:
            parking = 2
        else:
            parking = 1
        if store:
            store = 1.5
        else:
            store = 1
        floor/=2
        floor+=0.5
        price = (((float(self.Dlg.RentSpin.value())*1000000)/30000)+float(self.Dlg.MortSpin.value()))*7.2/1000
        if year != 0:
            nice = loc*room*parking*store*floor/(price/meter)*((year/5)+1)
        else:
            nice = loc*room*parking*store*floor*2/(price/meter)
        return nice

    def __DisableEv(self):
        self.dlg = CDialog(
            "Are you sure you want to disable rent and sale for this house?", "Question!", self)
        if self.dlg.exec():
            tmp = DBConnection.execute(HouseTable.select().where(
                HouseTable.c.Title == self.MyAdList.selectedItems()[0].text()
            )).fetchall()[0]
            if not tmp[16]:
                DBConnection.execute(HouseTable.update().where(
                HouseTable.c.Title == self.MyAdList.selectedItems()[0].text()
                ).values(
                    CanSell = True,
                    Owner = tmp[17],
                    LOwn = None
                ))
            DBConnection.execute(HouseTable.update().where(
                HouseTable.c.Title == self.MyAdList.selectedItems()[0].text()
            ).values(
                isSale=False,
                Mode=False,
                SellPrice=0,
                MortPrice=0,
                RentPrice=0
            ))
            self.__refresh()

    def __SetButton(self):
        if len(self.MyAdList.selectedItems()) == 0:
            self.RentBtn.setEnabled(False)
            self.SaleBtn.setEnabled(False)
            self.DisableBtn.setEnabled(False)
            return
        tmp = DBConnection.execute(HouseTable.select().where(
            HouseTable.c.Title == self.MyAdList.selectedItems()[0].text(),
        )).fetchall()[0]

        if not tmp[10]:
            self.RentBtn.setEnabled(False)
            self.SaleBtn.setEnabled(False)
            self.DisableBtn.setEnabled(False)
            return

        if not tmp[16]:
            self.RentBtn.setEnabled(False)
            self.SaleBtn.setEnabled(False)
            self.DisableBtn.setEnabled(True)
            return

        self.RentBtn.setEnabled(True)
        self.SaleBtn.setEnabled(True)
        self.DisableBtn.setEnabled(True)

    def __SetRent(self):
        tmp = DBConnection.execute(HouseTable.select().where(
            HouseTable.c.Title == self.MyAdList.selectedItems()[0].text())).fetchall()[0]
        self.Dlg = RequestPriceRent.RequestPriceRent(tmp[13], tmp[14])
        self.Dlg.Details.hide()
        self.Dlg.label_2.hide()
        self.Dlg.exec()
        if self.Dlg.status:
            DBConnection.execute(HouseTable.update().where(
                HouseTable.c.Title == self.MyAdList.selectedItems()[0].text()
            ).values(
                MortPrice=float(self.Dlg.MortSpin.value()),
                RentPrice=float(self.Dlg.RentSpin.value()),
                SellPrice=0,
                isSale=True,
                Mode=True,
                Nice=self.__calcNiceRent()
            ))

    def __SetSale(self):
        self.Dlg = RequestPrice.RequestPrice(DBConnection.execute(HouseTable.select().where(
            HouseTable.c.Title == self.MyAdList.selectedItems()[0].text())).fetchall()[0][12])
        self.Dlg.Details.hide()
        self.Dlg.label_2.hide()
        self.Dlg.exec()
        if self.Dlg.status:
            DBConnection.execute(HouseTable.update().where(
                HouseTable.c.Title == self.MyAdList.selectedItems()[0].text()
            ).values(
                SellPrice=float(self.Dlg.Price.value()),
                MortPrice=0,
                RentPrice=0,
                isSale=True,
                Mode=False,
                Nice=self.__calcNiceSale()
            ))

    def __AddHouse(self):
        self.NewAdWnd = EditCreateHouse.EditCreateHouse(self.username)
        self.NewAdWnd.closeEvent = self.__refresh  # type: ignore

    def __EditHouse(self):
        if len(self.MyAdList.selectedItems()) == 0:
            errdlg = ErrorDialog("Please select an ad!", self)
            errdlg.exec()
            return
        self.EditAdWnd = EditCreateHouse.EditCreateHouse(
            self.username, self.MyAdList.selectedItems()[0].text())
        self.EditAdWnd.closeEvent = self.__refresh  # type: ignore

    def __DeleteHouse(self):
        if len(self.MyAdList.selectedItems()) == 0:
            errdlg = ErrorDialog("Please select an ad!", self)
            errdlg.exec()
            return
        self.dlg = CDialog(
            "Are you sure you want to delete this ad?", "Question!", self)
        if self.dlg.exec():
            DBConnection.execute(HouseTable.delete().where(
                HouseTable.c.Title == self.MyAdList.selectedItems()[0].text()))
            self.__refresh()

    def __refresh(self, e=None):
        self.MyAdList.clear()
        for x in DBConnection.execute(HouseTable.select()).fetchall():
            if x[2] == self.username or x[17] == self.username:
                self.MyAdList.addItem(x[0])
