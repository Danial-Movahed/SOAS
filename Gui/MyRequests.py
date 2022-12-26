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
            self.ReceivedRequests.addTopLevelItem(
                QTreeWidgetItem([i[0], i[5], i[1], i[2], i[3], i[4]]))

        for i in self.requestsSent:
            self.SentRequests.addTopLevelItem(
                QTreeWidgetItem([i[0], i[5], i[1], i[2], i[3], i[4]]))

    def __DeleteSentRequest(self):
        if len(self.SentRequests.selectedItems()) == 0:
            errDlg = ErrorDialog("Please select a request!")
            errDlg.exec()
            return
        self.dlg = CDialog(
            "Are you sure you want to delete this request?", "Question!", self)
        if self.dlg.exec():
            DBConnection.execute(RequestTable.delete().where(
                RequestTable.c.Title == self.SentRequests.selectedItems()[0].text(0),
                RequestTable.c.Username == self.SentRequests.selectedItems()[0].text(1),
                RequestTable.c.Details == self.SentRequests.selectedItems()[0].text(2),
                RequestTable.c.Price == self.SentRequests.selectedItems()[0].text(3),
                RequestTable.c.MortPrice == self.SentRequests.selectedItems()[0].text(4),
                RequestTable.c.RentPrice == self.SentRequests.selectedItems()[0].text(5),
            ))
            self.__refresh()

    def __ViewSentRequest(self):
        if len(self.SentRequests.selectedItems()) == 0:
            errDlg = ErrorDialog("Please select a request!")
            errDlg.exec()
            return
        self.ViewReqWnd = ViewRequest.ViewRequest(DBConnection.execute(RequestTable.select().where(
            RequestTable.c.Title == self.SentRequests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.SentRequests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.SentRequests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.SentRequests.selectedItems()[0].text(3),
            RequestTable.c.MortPrice == self.SentRequests.selectedItems()[0].text(4),
            RequestTable.c.RentPrice == self.SentRequests.selectedItems()[0].text(5),
        )).fetchall()[0][7])

    def __ViewReceivedRequest(self):
        if len(self.ReceivedRequests.selectedItems()) == 0:
            errDlg = ErrorDialog("Please select a request!")
            errDlg.exec()
            return
        self.ViewReqWnd = ViewRequest.ViewRequest(DBConnection.execute(RequestTable.select().where(
            RequestTable.c.Title == self.ReceivedRequests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.ReceivedRequests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.ReceivedRequests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.ReceivedRequests.selectedItems()[0].text(3),
            RequestTable.c.MortPrice == self.ReceivedRequests.selectedItems()[0].text(4),
            RequestTable.c.RentPrice == self.ReceivedRequests.selectedItems()[0].text(5),
        )).fetchall()[0][7])

    def __AcceptReceivedRequest(self):
        if len(self.ReceivedRequests.selectedItems()) == 0:
            errDlg = ErrorDialog("Please select a request!")
            errDlg.exec()
            return
        self.dlg = CDialog(
            "Are you sure you want to accept this request?", "Question!", self)
        if self.dlg.exec():
            DBConnection.execute(RequestTable.update().where(
                RequestTable.c.Title == self.ReceivedRequests.selectedItems()[0].text(0),
                RequestTable.c.Username == self.ReceivedRequests.selectedItems()[0].text(1),
                RequestTable.c.Details == self.ReceivedRequests.selectedItems()[0].text(2),
                RequestTable.c.Price == self.ReceivedRequests.selectedItems()[0].text(3),
                RequestTable.c.MortPrice == self.ReceivedRequests.selectedItems()[0].text(4),
                RequestTable.c.RentPrice == self.ReceivedRequests.selectedItems()[0].text(5),
            ).values(Owner = self.ReceivedRequests.selectedItems()[0].text(1)))
            self.__refresh()

    def __DeclineReceivedRequest(self):
        if len(self.ReceivedRequests.selectedItems()) == 0:
            errDlg = ErrorDialog("Please select a request!")
            errDlg.exec()
            return
        self.dlg = CDialog(
            "Are you sure you want to decline this request?", "Question!", self)
        if self.dlg.exec():
            DBConnection.execute(RequestTable.delete().where(
                RequestTable.c.Title == self.ReceivedRequests.selectedItems()[0].text(0),
                RequestTable.c.Username == self.ReceivedRequests.selectedItems()[0].text(1),
                RequestTable.c.Details == self.ReceivedRequests.selectedItems()[0].text(2),
                RequestTable.c.Price == self.ReceivedRequests.selectedItems()[0].text(3),
                RequestTable.c.MortPrice == self.ReceivedRequests.selectedItems()[0].text(4),
                RequestTable.c.RentPrice == self.ReceivedRequests.selectedItems()[0].text(5),
            ))
            self.__refresh()
