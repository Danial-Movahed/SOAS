from .include import *
from . import ui_SignUp

class SignUp(QMainWindow, ui_SignUp.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.State = False
        self.SignUpContinuebtn.clicked.connect(lambda: self.save())
        self.SignUpQuitbtn.clicked.connect(lambda: self.close())
        self.show()
    def save(self):
        if self.SignUpPassword.text() != self.SignUpConfimPassword.text():
            err = ErrorDialog("Password does not match!")
            err.exec()
            return
        self.State = True
        self.close()