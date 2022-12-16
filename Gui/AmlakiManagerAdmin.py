from .include import *
from . import AmlakiManager


class AmlakiManagerAdmin(AmlakiManager.AmlakiManager):
    def __init__(self):
        super().__init__()

    def __OpenAmlakiMgmt(self):
        self.err = ErrorDialog("This is not implemented yet!", self)
        self.err.exec()
