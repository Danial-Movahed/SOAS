from .include import *
from . import ui_EditCreateAd


class EditCreateAd(QMainWindow, ui_EditCreateAd.Ui_MainWindow):
    def __init__(self,username,currentAd=None):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.SaveBtn.clicked.connect(lambda: self.__save())
        self.CancelBtn.clicked.connect(lambda: self.close())
        self.show()

    def __check(self):
        if self.AdTitle.text() == "" or self.AdMessage.toPlainText() == "" or self.YearLineEdit.text() == "":
            return False
        if  self.CityPartCombo.currentText() == "Not selected" or self.ParkingCombo.currentText() == "Not selected" or self.StoreCombo.currentText() == "Not selected":
            return False
        if self.RoomSpin.value() == 0 or self.MeterSpin.value() == 0  or self.FloorSpin.value() == 0:
            return False
        return True
    def __save(self):
        if not self.__check():
            errDlg = ErrorDialog("Please fill all the fields!",self,)
            errDlg.exec()
            return
        try:
            DBConnection.execute(AdTable.insert().values(
                Title = self.AdTitle.text(),
                Message = self.AdMessage.toPlainText(),
                Writer = self.username[0],
                Floor = self.FloorSpin.value(),
                CityPart = self.CityPartCombo.currentText(),
                YearsOld = self.YearLineEdit.text(),
                Room = self.RoomSpin.value(),
                Meter = self.MeterSpin.value(),
                HasParking = self.ParkingCombo.currentText(),
                HasStoreroom = self.StoreCombo.currentText()
            ))
            self.close()
        except:
            errDlg = ErrorDialog("This title is not chosen by another user, please use another title!")
            errDlg.exec()