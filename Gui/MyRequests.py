from .include import *
from . import ui_MyRequests


class MyRequests(QMainWindow, ui_MyRequests.Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.requestsReceived = []
        self.requestsSent = []
        self.__refresh()
        # Sent
        self.DeleteSentRequestBtn.clicked.connect(
            lambda: self.__DeleteSentRequest())
        self.EditSentRequestBtn.clicked.connect(
            lambda: self.__EditSentRequest())
        self.ViewSentRequestBtn.clicked.connect(
            lambda: self.__ViewSentRequest())
        # Received
        self.ViewReceivedRequestBtn.clicked.connect(
            lambda: self.__ViewReceivedRequest())
        self.AcceptReceivedRequestBtn.clicked.connect(
            lambda: self.__AcceptReceivedRequest())
        self.DeclineReceivedRequestBtn.clicked.connect(
            lambda: self.__DeclineReceivedRequest())
        self.show()

    def __refresh(self):
        self.ReceivedRequests.clear()
        self.SentRequests.clear()
        self.requestsReceived = DBConnection.execute(
            RequestTable.select().where(RequestTable.c.To == self.username)).fetchall()
        self.requestsSent = DBConnection.execute(RequestTable.select().where(
            RequestTable.c.Username == self.username)).fetchall()

        for i in self.requestsReceived:
            self.ReceivedRequests.addTopLevelItem(
                QTreeWidgetItem([i[0], i[3], i[1], i[2]]))

        for i in self.requestsSent:
            self.SentRequests.addTopLevelItem(
                QTreeWidgetItem([i[0], i[3], i[1], i[2], i[5]]))

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
        if len(self.ReceivedRequests.selectedItems()) == 0:
            errDlg = ErrorDialog("Please select a request!")
            errDlg.exec()
            return
        DBConnection.execute(RequestTable.delete().where(
            RequestTable.c.Title == self.ReceivedRequests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.ReceivedRequests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.ReceivedRequests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.ReceivedRequests.selectedItems()[0].text(3),
        ))
        self.__refresh()
