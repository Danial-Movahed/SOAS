from .include import *
from . import ui_Login, FirstTimeSetup
from . import AmlakiMgr,AmlakiMgrAdmin

class Login(QMainWindow, ui_Login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoginContinueBtn.clicked.connect(lambda: self.check())
        self.LoginQuitBtn.clicked.connect(lambda: self.close())
        self.engine = create_engine('sqlite:///Database.db', echo = True)
        self.meta = MetaData()
        self.UsersTable = Table(
            'Users', self.meta, 
            Column('Username', String, primary_key=True), 
            Column('Password', String),
            Column('isAdmin', Boolean),
        )
        self.AdTable = Table(
            'Ads', self.meta, 
            Column("Title", String, primary_key=True),
            Column("Message", String),
            Column("Writer", String),
            Column("CityPart", String),
            Column("Meter", String),
            Column("Room", String),
            Column("YearsOld", String),
            Column("Floor", String),
            Column("HasParking", String),
            Column("HasStoreroom", String),
        )
        self.meta.create_all(self.engine)
        self.DBConnection = self.engine.connect()
        if len(self.DBConnection.execute(self.UsersTable.select()).fetchall()) == 0:
            self.firstTimeSetup()
            return
        self.show()

    def check(self):
        user = self.DBConnection.execute(self.UsersTable.select().where(self.UsersTable.c.Username == self.LoginUsername.text() and self.UsersTable.c.Password == blake2s((self.LoginPassword.text()).encode()).hexdigest()))
        if user == None:
            self.LoginLabel.setText("Wrong username or password!")
            return None
        self.LoginLabel.setText("Welcome!")
        if user.isAdmin:
            self.AmlakiMgr = AmlakiMgrAdmin()
        else:
            self.AmlakiMgr = AmlakiMgr()

    def firstTimeSetup(self):
        self.FTSWnd = FirstTimeSetup.FirstTimeSetup()
        self.FTSWnd.closeEvent = self.firstTimeSetupSave

    def firstTimeSetupSave(self, e):
        if self.FTSWnd.State:
            self.DBConnection.execute(self.UsersTable.insert().values(Username = self.FTSWnd.FTSUsername.text(), Password =  blake2s((self.FTSWnd.FTSPassword.text()).encode()).hexdigest(), isAdmin = True))
            self.show()
            return
        self.close()
