from .include import *
from . import ui_AmlakiMgrAdmin

class Login(QMainWindow, ui_AmlakiMgrAdmin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Base = declarative_base()
        self.engine = create_engine('sqlite:///Databases/Agahis.db')
        self.Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.show()