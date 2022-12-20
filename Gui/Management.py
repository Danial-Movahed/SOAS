from matplotlib import use
from .include import *
from . import ui_Management,ShowAdAdmin,ViewRequest


class Management(ui_Management.Ui_MainWindow, QMainWindow):
    def __init__(self,username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.AcceptRequestBtn.clicked.connect(lambda: self.__AcceptRequest())
        self.DeclineRequestBtn.clicked.connect(lambda: self.__DeclineRequest())
        self.ViewRequestBtn.clicked.connect(lambda: self.__ViewRequest())
        self.ViewAdBtn.clicked.connect(lambda: self.__ViewAd())
        self.DeleteAdBtn.clicked.connect(lambda: self.__DeleteAd())
        self.DeleteUserBtn.clicked.connect(lambda: self.__DeleteUser())
        self.UsersTable.cellChanged.connect(self.__SaveUsers)
        self.isRefreshing=True
        self.__refresh()
        self.show()

    def __DeleteUser(self):
        print(self.UsersTable.item(self.UsersTable.currentRow(),0).text())
        DBConnection.execute(UsersTable.delete().where(UsersTable.c.Username == self.UsersTable.item(self.UsersTable.currentRow(),0).text()))
        self.__refresh()

    def __SaveUsers(self,row,column):
        if self.isRefreshing:
            return
        print("Updating user info!")
        DBConnection.execute(UsersTable.update().where(UsersTable.c.Username == self.UsersTable.item(row, 0).text()).values(
            isVerified = (self.UsersTable.item(row, 1).checkState() == Qt.Checked),
            isAdmin = (self.UsersTable.item(row, 2).checkState() == Qt.Checked),
            Password = self.UsersTable.item(row,3).text()
        ))

    def __refresh(self):
        self.isRefreshing = True
        ############# Users
        self.UsersTable.setRowCount(0)
        for u in DBConnection.execute(UsersTable.select().where()).fetchall():
            rowPosition = self.UsersTable.rowCount()
            self.UsersTable.insertRow(rowPosition)
            tmp = QTableWidgetItem(str(u[0]))
            tmp.setFlags(tmp.flags() ^ Qt.ItemIsEditable)
            self.UsersTable.setItem(rowPosition , 0, QTableWidgetItem(tmp))
            tmp = QTableWidgetItem()
            tmp.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            tmp.setText("Verified?")
            if u[3]:
                tmp.setCheckState(Qt.Checked)
            else:
                tmp.setCheckState(Qt.Unchecked)       
            self.UsersTable.setItem(rowPosition , 1, tmp)
            tmp = QTableWidgetItem()
            tmp.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            tmp.setText("Admin?")
            if u[2]:
                tmp.setCheckState(Qt.Checked)
            else:
                tmp.setCheckState(Qt.Unchecked)       

            self.UsersTable.setItem(rowPosition , 2, tmp)
            self.UsersTable.setItem(rowPosition , 3, QTableWidgetItem(u[1]))
        ################# Ads
        self.AdList.clear()
        self.AdList.addItems([x[0] for x in DBConnection.execute(AdTable.select().where())])
        ################# Requests
        self.Requests.clear()
        for i in DBConnection.execute(
        RequestTable.select().where(
            RequestTable.c.Status == "Waiting for admin"
        )).fetchall():
            if i[5] == "Accepted":
                continue
            self.Requests.addTopLevelItem(
                QTreeWidgetItem([i[0], i[3], i[1], i[2], i[5]]))

        self.isRefreshing = False

    def __AcceptRequest(self):
        DBConnection.execute(RequestTable.update().where(
            RequestTable.c.Title == self.Requests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.Requests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.Requests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.Requests.selectedItems()[0].text(3),
        ).values(Status = "Accepted!"))
        DBConnection.execute(AdTable.update().where(
            AdTable.c.Title == self.Requests.selectedItems()[0].text(0)
        ).values(
            isSold = True,
            Owner = self.Requests.selectedItems()[0].text(1),
            Title = DBConnection.execute(AdTable.select().where(AdTable.c.Title == self.Requests.selectedItems()[0].text(0))).fetchall()[0][0]+" Sold Out!"
            ))
        self.__refresh()

    def __ViewRequest(self):
        if len(self.Requests.selectedItems()) == 0:
            self.errDlg = ErrorDialog("Please select a request!", self)
            self.errDlg.exec()
        self.ViewReqWnd = ViewRequest.ViewRequest(DBConnection.execute(RequestTable.select().where(
            RequestTable.c.Title == self.Requests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.Requests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.Requests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.Requests.selectedItems()[0].text(3),
        )).fetchall()[0][6])

    def __DeclineRequest(self):
        DBConnection.execute(RequestTable.delete().where(
            RequestTable.c.Title == self.Requests.selectedItems()[0].text(0),
            RequestTable.c.Username == self.Requests.selectedItems()[0].text(1),
            RequestTable.c.Details == self.Requests.selectedItems()[0].text(2),
            RequestTable.c.Price == self.Requests.selectedItems()[0].text(3),
        ))
        self.__refresh()

    def __ViewAd(self):
        if len(self.AdList.selectedItems()) == 0:
            self.errDlg = ErrorDialog("Please select an ad!", self)
            self.errDlg.exec()
        self.ShowAdWnd = ShowAdAdmin.ShowAdAdmin(self.AdList.selectedItems()[0].text())

    def __DeleteAd(self):
        if len(self.AdList.selectedItems()) == 0:
            self.errDlg = ErrorDialog("Please select an ad!", self)
            self.errDlg.exec()
        DBConnection.execute(AdTable.delete().where(
            AdTable.c.Title == self.AdList.selectedItems()[0].text()
        ))
        DBConnection.execute(RequestTable.delete().where(RequestTable.c.Title == self.AdList.selectedItems()[0].text()))
        self.__refresh()