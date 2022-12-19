from .include import *
from . import ui_EditCreateAd


class EditCreateAd(QMainWindow, ui_EditCreateAd.Ui_MainWindow):
    def __init__(self,username,currentAd=None):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.currentAdTitle = currentAd
        if self.currentAdTitle != None:
            self.__load()
            self.oldTitle = self.AdTitle.text()
        self.SaveBtn.clicked.connect(lambda: self.__save())
        self.CancelBtn.clicked.connect(lambda: self.close())
        self.show()

    def __load(self):
        currentAd = DBConnection.execute(AdTable.select().where(AdTable.c.Title == self.currentAdTitle)).fetchall()
        self.AdTitle.setText(currentAd[0][0])
        self.AdMessage.setText(currentAd[0][1])
        self.CityPartCombo.setCurrentText(currentAd[0][3])
        self.MeterSpin.setValue(int(currentAd[0][4]))
        self.RoomSpin.setValue(int(currentAd[0][5]))
        self.YearSpin.setValue(int(currentAd[0][6]))
        self.FloorSpin.setValue(int(currentAd[0][7]))
        self.ParkingCombo.setCurrentText(currentAd[0][8])
        self.StoreCombo.setCurrentText(currentAd[0][9])

    def __check(self):
        if self.AdTitle.text() == "" or self.AdMessage.toPlainText() == "":
            return False
        if  self.CityPartCombo.currentText() == "Not selected" or self.ParkingCombo.currentText() == "Not selected" or self.StoreCombo.currentText() == "Not selected":
            return False
        if self.RoomSpin.value() == 0 or self.MeterSpin.value() == 0  or self.FloorSpin.value() == 0 or self.YearSpin.value() == 0:
            return False
        return True
    def __save(self):
        if not self.__check():
            errDlg = ErrorDialog("Please fill all the fields!",self,)
            errDlg.exec()
            return
        if self.currentAdTitle != None:
            try:
                DBConnection.execute(AdTable.update().where(AdTable.c.Title == self.oldTitle).values(
                    Title = self.AdTitle.text(),
                    Message = self.AdMessage.toPlainText(),
                    CityPart = self.CityPartCombo.currentText(),
                    Meter = self.MeterSpin.value(),
                    Room = self.RoomSpin.value(),
                    YearsOld = self.YearSpin.value(),
                    Floor = self.FloorSpin.value(),
                    HasParking = self.ParkingCombo.currentText(),
                    HasStoreroom = self.StoreCombo.currentText()
                ))
                self.close()
                return
            except:
                errDlg = ErrorDialog("This title is not chosen by another user, please use another title!")
                errDlg.exec()
                return
        try:
            DBConnection.execute(AdTable.insert().values(
                Title = self.AdTitle.text(),
                Message = self.AdMessage.toPlainText(),
                Owner = self.username[0],
                Floor = str(self.FloorSpin.value()),
                CityPart = self.CityPartCombo.currentText(),
                YearsOld = str(self.YearSpin.value()),
                Room = str(self.RoomSpin.value()),
                Meter = str(self.MeterSpin.value()),
                HasParking = self.ParkingCombo.currentText(),
                HasStoreroom = self.StoreCombo.currentText()
            ))
            self.close()
        except:
            errDlg = ErrorDialog("This title is not chosen by another user, please use another title!")
            errDlg.exec()