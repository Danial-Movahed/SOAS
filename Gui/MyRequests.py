from .include import *
from . import ui_MyRequests,ViewRequest


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
            if i[5] == "Accepted":
                continue
            self.ReceivedRequests.addTopLevelItem(
                QTreeWidgetItem([i[0], i[3], i[1], i[2], i[5]]))

        for i in self.requestsSent:
            self.SentRequests.addTopLevelItem(
                QTreeWidgetItem([i[0], i[3], i[1], i[2], i[5]]))

    def __DeleteSentRequest(self):
        DBConnection.execute(RequestTable.delete().where(
            RequestTable.c.Title == self.SentRequests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.SentRequests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.SentRequests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.SentRequests.selectedItems()[0].text(3),
        ))
        self.__refresh()

    def __ViewSentRequest(self):
        self.ViewReqWnd = ViewRequest.ViewRequest(DBConnection.execute(RequestTable.select().where(
            RequestTable.c.Title == self.SentRequests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.SentRequests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.SentRequests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.SentRequests.selectedItems()[0].text(3),
        )).fetchall()[0][6])

    def __ViewReceivedRequest(self):
            self.ViewReqWnd = ViewRequest.ViewRequest(DBConnection.execute(RequestTable.select().where(
            RequestTable.c.Title == self.ReceivedRequests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.ReceivedRequests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.ReceivedRequests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.ReceivedRequests.selectedItems()[0].text(3),
        )).fetchall()[0][6])

    def __AcceptReceivedRequest(self):
        DBConnection.execute(RequestTable.update().where(
            RequestTable.c.Title == self.ReceivedRequests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.ReceivedRequests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.ReceivedRequests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.ReceivedRequests.selectedItems()[0].text(3),
        ).values(Status = "Waiting for admin"))
        # DBConnection.execute(AdTable.update().where(
        #     AdTable.c.Title == self.ReceivedRequests.selectedItems()[0].text(0)
        # ).values(
        #     isSold = True,
        #     Owner = self.ReceivedRequests.selectedItems()[0].text(1),
        #     Title = DBConnection.execute(AdTable.select().where(AdTable.c.Title == self.ReceivedRequests.selectedItems()[0].text(0))).fetchall()[0][0]+" Sold Out!"
        #     ))
        self.__refresh()

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
