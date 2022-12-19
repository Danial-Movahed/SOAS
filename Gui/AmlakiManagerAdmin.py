from .include import *
from . import AmlakiManager,Management


class AmlakiManagerAdmin(AmlakiManager.AmlakiManager):
    def __init__(self,username):
        super().__init__(username)

    def OpenAmlakiMgmt(self):
        self.ManagementWnd = Management.Management()
        self.ManagementWnd.closeEvent = self.refresh
