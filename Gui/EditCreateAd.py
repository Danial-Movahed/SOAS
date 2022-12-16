from .include import *
from . import ui_EditCreateAd

class EditCreateAd(QMainWindow, ui_EditCreateAd.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
