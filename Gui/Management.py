from .include import *
from . import ui_Management, ShowAdAdmin, ViewRequest


class Management(ui_Management.Ui_MainWindow, QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.DeleteUserBtn.clicked.connect(lambda: self.__DeleteUser())
        self.UsersTable.cellChanged.connect(self.__SaveUsers)
        self.HouseTable.cellChanged.connect(self.__SaveHouses)
        self.HouseTable.itemDoubleClicked.connect(self.__ViewHouse)
        self.DeleteHouseBtn.clicked.connect(self.__DeleteHouse)
        self.isRefreshing = True
        self.__refresh()
        self.show()

    def __DeleteHouse(self):
        if self.HouseTable.currentRow() == -1:
            self.errDlg = ErrorDialog("Please select a house!", self)
            self.errDlg.exec()
            return
        self.dlg = CDialog(
            "Are you sure you want to delete this house?", "Question!", self)
        if self.dlg.exec():
            DBConnection.execute(HouseTable.delete().where(
                HouseTable.c.Title == self.HouseTable.item(self.HouseTable.currentRow(), 0).text()))
            self.__refresh()

    def __DeleteUser(self):
        if self.UsersTable.currentRow() == -1:
            self.errDlg = ErrorDialog("Please select an user!", self)
            self.errDlg.exec()
            return
        self.dlg = CDialog(
            "Are you sure you want to delete this user?", "Question!", self)
        if self.dlg.exec():
            DBConnection.execute(UsersTable.delete().where(
                UsersTable.c.Username == self.UsersTable.item(self.UsersTable.currentRow(), 0).text()))
            self.__refresh()

    def __SaveUsers(self, row, column):
        if self.isRefreshing:
            return
        print("Updating user info!")
        DBConnection.execute(UsersTable.update().where(UsersTable.c.Username == self.UsersTable.item(row, 0).text()).values(
            isVerified=(self.UsersTable.item(
                row, 1).checkState() == Qt.Checked),
            isAdmin=(self.UsersTable.item(row, 2).checkState() == Qt.Checked),
            Password=self.UsersTable.item(row, 3).text()
        ))

    def __SaveHouses(self, row, column):
        if self.isRefreshing:
            return
        print("Updating house info!")
        DBConnection.execute(HouseTable.update().where(HouseTable.c.Title == self.HouseTable.item(row, 0).text()).values(
            isVerified=(self.HouseTable.item(
                row, 1).checkState() == Qt.Checked),
            isSale=(self.HouseTable.item(row, 2).checkState() == Qt.Checked),
            Mode=(self.HouseTable.item(row, 3).checkState() == Qt.Checked),
        ))

    def __ViewHouse(self, item):
        if self.isRefreshing:
            return
        self.ShowAdWnd = ShowAdAdmin.ShowAdAdmin(DBConnection.execute(HouseTable.select().where(
            HouseTable.c.Title == self.HouseTable.item(self.HouseTable.currentRow(), 0).text())).fetchall()[0][0])

    def __refresh(self):
        self.isRefreshing = True
        # Users
        self.UsersTable.setRowCount(0)
        for u in DBConnection.execute(UsersTable.select().where()).fetchall():
            rowPosition = self.UsersTable.rowCount()
            self.UsersTable.insertRow(rowPosition)
            tmp = QTableWidgetItem(str(u[0]))
            tmp.setFlags(tmp.flags() ^ Qt.ItemIsEditable)
            self.UsersTable.setItem(rowPosition, 0, QTableWidgetItem(tmp))
            tmp = QTableWidgetItem()
            tmp.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            tmp.setText("Verified?")
            if u[3]:
                tmp.setCheckState(Qt.Checked)
            else:
                tmp.setCheckState(Qt.Unchecked)
            self.UsersTable.setItem(rowPosition, 1, tmp)
            tmp = QTableWidgetItem()
            tmp.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            tmp.setText("Admin?")
            if u[2]:
                tmp.setCheckState(Qt.Checked)
            else:
                tmp.setCheckState(Qt.Unchecked)

            self.UsersTable.setItem(rowPosition, 2, tmp)
            self.UsersTable.setItem(rowPosition, 3, QTableWidgetItem(u[1]))

        # Houses
        self.HouseTable.setRowCount(0)
        for h in DBConnection.execute(HouseTable.select()).fetchall():
            rowPosition = self.HouseTable.rowCount()
            self.HouseTable.insertRow(rowPosition)
            tmp = QTableWidgetItem(str(h[0]))
            tmp.setFlags(tmp.flags() ^ Qt.ItemIsEditable)
            self.HouseTable.setItem(rowPosition, 0, QTableWidgetItem(tmp))
            tmp = QTableWidgetItem()
            tmp.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            tmp.setText("Verified?")
            if h[10]:
                tmp.setCheckState(Qt.Checked)
            else:
                tmp.setCheckState(Qt.Unchecked)
            self.HouseTable.setItem(rowPosition, 1, tmp)
            tmp = QTableWidgetItem()
            tmp.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            tmp.setText("For Sale?")
            if h[11]:
                tmp.setCheckState(Qt.Checked)
            else:
                tmp.setCheckState(Qt.Unchecked)
            self.HouseTable.setItem(rowPosition, 2, tmp)
            tmp = QTableWidgetItem()
            tmp.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            tmp.setText("For Rent?")
            if h[12]:
                tmp.setCheckState(Qt.Checked)
            else:
                tmp.setCheckState(Qt.Unchecked)
            self.HouseTable.setItem(rowPosition, 3, tmp)

        self.isRefreshing = False
