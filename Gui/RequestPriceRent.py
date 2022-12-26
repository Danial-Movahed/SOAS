from .include import *
from . import ui_RequestPriceRent

class RequestPriceRent(QDialog, ui_RequestPriceRent.Ui_Dialog):
    def __init__(self,stMort,stRent):
        super().__init__()
        self.setupUi(self)
        self.status = False
        if stMort != None:
            self.MortSpin.setValue(stPrice)
        if stRent != None:
            self.RentSpin.setValue(stPrice)
        self.buttonBox.buttons()[0].clicked.connect(lambda: self.__Ok())
        self.show()

    def __Ok(self):
        self.status = True
