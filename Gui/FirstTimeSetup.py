from .include import *
from . import ui_FirstTimeSetup

class FirstTimeSetup(QMainWindow, ui_FirstTimeSetup.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.State = False
        self.FTSQuitbtn.clicked.connect(lambda: self.close())
        self.FTSContinuebtn.clicked.connect(lambda: self.saveClose())
        self.show()
    def saveClose(self):
        if self.FTSPassword.text() == "" or self.FTSUsername.text() == "":
            self.errDlg = ErrorDialog("Please fill everything!", self)
            self.errDlg.exec()
            return
        self.State=True
        self.close()