from .include import *
from . import ui_MyAds

class MyAds(QMainWindow, ui_MyAds.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
