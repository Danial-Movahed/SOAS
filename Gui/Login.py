from .include import *
from . import AmlakiManager, ui_Login, FirstTimeSetup, AmlakiManagerAdmin, SignUp


class Login(QMainWindow, ui_Login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoginContinueBtn.clicked.connect(lambda: self.check())
        self.LoginQuitBtn.clicked.connect(lambda: self.close())
        self.LoginSignUpBtn.clicked.connect(lambda: self.signUp())
        if len(DBConnection.execute(UsersTable.select()).fetchall()) == 0:
            self.firstTimeSetup()
            return
        self.show()

    def signUp(self):
        self.SignUpWnd = SignUp.SignUp()
        self.SignUpWnd.closeEvent = self.signUpSave  # type: ignore

    def signUpSave(self, e):
        if self.SignUpWnd.State:
            DBConnection.execute(UsersTable.insert().values(Username=self.SignUpWnd.SignUpUsername.text(
            ), Password=blake2s((self.SignUpWnd.SignUpPassword.text()).encode()).hexdigest(), isAdmin=False, isVerified=False))
            self.dialog = CDialog(
                "User created, waiting for admin verification!", "Waiting", self)
            self.dialog.exec()

    def check(self):
        user = DBConnection.execute(UsersTable.select().where((UsersTable.c.Username == self.LoginUsername.text()) &
        (UsersTable.c.Password == blake2s((self.LoginPassword.text()).encode()).hexdigest()))).fetchall()
        if len(user) == 0:
            self.LoginLabel.setText("Wrong username or password!")
            return
        if not user[0][3]:
            self.LoginLabel.setText("Your user is not verified!")
            return
        self.LoginLabel.setText("Welcome!")
        if user[0][2]:
            self.AmlakiMgr = AmlakiManagerAdmin.AmlakiManagerAdmin(user[0])
            self.close()
        else:
            self.AmlakiMgr = AmlakiManager.AmlakiManager(user[0])
            self.close()

    def firstTimeSetup(self):
        self.FTSWnd = FirstTimeSetup.FirstTimeSetup()
        self.FTSWnd.closeEvent = self.firstTimeSetupSave  # type: ignore

    def firstTimeSetupSave(self, e):
        if self.FTSWnd.State:
            DBConnection.execute(UsersTable.insert().values(Username=self.FTSWnd.FTSUsername.text(
            ), Password=blake2s((self.FTSWnd.FTSPassword.text()).encode()).hexdigest(), isAdmin=True, isVerified=True))
            self.show()
            return
        self.close()
