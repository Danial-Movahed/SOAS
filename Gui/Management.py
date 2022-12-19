from .include import *
from . import ui_Management


class Management(QMainWindow, ui_Management.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AcceptRequestBtn.clicked.connect(lambda: self.__AcceptRequest())
        self.DeclineRequestBtn.clicked.connect(lambda: self.__DeclineRequest())
        self.ViewRequestBtn.clicked.connect(lambda: self.__ViewRequest())
        self.ViewAdBtn.clicked.connect(lambda: self.__ViewAd())
        self.DeleteAdBtn.clicked.connect(lambda: self.__DeleteAd())
        self.__refresh()
        self.show()

    def __refresh(self):
        pass

    def __AcceptRequest(self):
        pass
    
    def __ViewRequest(self):
        pass

    def __DeclineRequest(self):
        pass

    def __ViewAd(self):
        pass

    def __DeleteAd(self):
        pass