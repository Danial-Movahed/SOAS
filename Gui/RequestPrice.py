from .include import *
from . import ui_RequestPrice


class RequestPrice(QDialog, ui_RequestPrice.Ui_Dialog):
    def __init__(self, stPrice):
        super().__init__()
        self.setupUi(self)
        self.status = False
        if stPrice != None:
            self.Price.setValue(stPrice)
        self.buttonBox.buttons()[0].clicked.connect(lambda: self.__Ok())
        self.show()

    def __Ok(self):
        self.status = True
