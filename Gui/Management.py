from .include import *
from . import ui_Management,ShowAdAdmin


class Management(ui_Management.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        self.UsersTable.setRowCount(0)
        self.AdList.clear()
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

        self.AdList.addItems([x[0] for x in DBConnection.execute(AdTable.select().where())])
        self.isRefreshing = False

    def __AcceptRequest(self):
        pass
    
    def __ViewRequest(self):
        pass

    def __DeclineRequest(self):
        pass

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
        self.__refresh()