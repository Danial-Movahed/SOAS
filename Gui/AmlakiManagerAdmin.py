from .include import *
from . import AmlakiManager


class AmlakiManagerAdmin(AmlakiManager.AmlakiManager):
    def __init__(self,username):
        super().__init__(username)

    def OpenAmlakiMgmt(self):
        self.err = ErrorDialog("This is not implemented yet!", self)
        self.err.exec()
