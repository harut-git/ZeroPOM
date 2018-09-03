from Core.BasePage import BasePage


class RibbonPage(BasePage):
    __instance = None

    @staticmethod
    def inst():
        if RibbonPage.__instance is None:
            RibbonPage.__instance = RibbonPage()
        return RibbonPage.__instance

    # -- Elements -- #

    file = 'File'
    filing_log = 'Filing Log'
    refresh = 'Refresh'
    settings = 'Settings'
    filter = 'Show all'
    status = ''


