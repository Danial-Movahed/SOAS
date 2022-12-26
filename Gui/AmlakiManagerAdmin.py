from .include import *
from . import AmlakiManager,Management


class AmlakiManagerAdmin(AmlakiManager.AmlakiManager):
    def __init__(self,username):
        super().__init__(username)
        self.AmlakiMgmt.show()

    def OpenAmlakiMgmt(self):
        self.ManagementWnd = Management.Management(username=self.username[0])
        self.ManagementWnd.closeEvent = self.refresh
