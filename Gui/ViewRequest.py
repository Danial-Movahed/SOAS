from .include import *
from . import ui_ViewRequest

class ViewRequest(QMainWindow, ui_ViewRequest.Ui_MainWindow):
    def __init__(self,reqId):
        super().__init__()
        self.setupUi(self)
        self.reqId = reqId
        self.Request = DBConnection.execute(RequestTable.select().where(RequestTable.c.Id == self.reqId)).fetchall()[0]
        self.Title.setText("Request to buy: "+self.Request[0])
        self.Details.setText(self.Request[1])
        self.Price.setText(self.Request[2])
        self.Writer.setText(self.Request[3]+" wants to buy!")
        self.show()