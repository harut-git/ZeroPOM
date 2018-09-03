from Core.BasePage import BasePage


class InboxPage(BasePage):
    __instance = None

    @staticmethod
    def inst():
        if InboxPage.__instance is None:
            InboxPage.__instance = InboxPage()
        return InboxPage.__instance

    "Page class that all page models can inherit from"
