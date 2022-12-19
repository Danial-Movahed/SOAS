from .include import *
from . import ui_MyRequests


class MyRequests(QMainWindow, ui_MyRequests.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Sent
        self.DeleteSentRequestBtn.clicked.connect(lambda: self.__DeleteSentRequest())
        self.EditSentRequestBtn.clicked.connect(lambda: self.__EditSentRequest())
        self.ViewSentRequestBtn.clicked.connect(lambda: self.__ViewSentRequest())
        # Received
        self.ViewReceivedRequestBtn.clicked.connect(lambda: self.__ViewReceivedRequest())
        self.AcceptReceivedRequestBtn.clicked.connect(lambda: self.__AcceptReceivedRequest())
        self.DeclineReceivedRequestBtn.clicked.connect(lambda: self.__DeclineReceivedRequest())
        self.show()

    def __DeleteSentRequest(self):
        pass

    def __EditSentRequest(self):
        pass

    def __ViewSentRequest(self):
        pass
    
    def __ViewReceivedRequest(self):
        pass

    def __AcceptReceivedRequest(self):
        pass

    def __DeclineReceivedRequest(self):
        pass