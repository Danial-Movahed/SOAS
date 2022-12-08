from .include import *
from . import ui_Login
# from . import AmlakiMgr,AmlakiMgrAdmin

class Login(QMainWindow, ui_Login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoginContinueBtn.clicked.connect(lambda: self.check())
        self.LoginQuitBtn.clicked.connect(lambda: self.close())
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///Databases/Users.db')
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.show()
    def check(self):
        user = self.session.query(User).filter(User.Username == self.LoginUsername.text and User.Password == self.LoginPassword.text)
        if user == None:
            self.label_6.setText("Wrong username or password!")
            return None
        self.label_6.setText("Welcome!")
        # if user.isAdmin:
        #     self.AmlakiMgr = AmlakiMgrAdmin()
        # else:
        #     self.AmlakiMgr = AmlakiMgr()
        