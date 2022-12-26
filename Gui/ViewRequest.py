from .include import *
from . import ui_ViewRequest

class ViewRequest(QMainWindow, ui_ViewRequest.Ui_MainWindow):
    def __init__(self,reqId):
        super().__init__()
        self.setupUi(self)
        self.reqId = reqId
        self.Request = DBConnection.execute(RequestTable.select().where(RequestTable.c.Id == self.reqId)).fetchall()[0]
        if self.Request[2] == 0:
            self.Rent = True
        else:
            self.Rent = False
        self.Title.setText("Request to "+self.Rent*"rent: "+abs(self.Rent-1)*"buy: "+self.Request[0])
        self.Details.setText(self.Request[1])
        self.Writer.setText(self.Request[3]+" wants to "+self.Rent*"rent "+abs(self.Rent-1)*"buy "+"from "+self.Request[4]+"!")
        if self.Request[2]==0:
            self.BuyBil.hide()
            self.BuyLab.hide()
            self.BuyPrice.hide()
        if self.Request[3]==0:
            self.MortLab.hide()
            self.MortMil.hide()
            self.MortPrice.hide()
        if self.Request[4]==0:
            self.RentLab.hide()
            self.RentMil.hide()
            self.RentPrice.hide()
        self.BuyPrice.setValue(self.Request[2])
        self.MortPrice.setValue(self.Request[3])
        self.RentPrice.setValue(self.Request[4])
        self.show()