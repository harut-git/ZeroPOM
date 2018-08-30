from Core.BasePage import BasePage


class AddinsPage(BasePage):
    __instance = None

    @staticmethod
    def inst():
        if AddinsPage.__instance is None:
            AddinsPage.__instance = AddinsPage()
        return AddinsPage.__instance

    zero_text = 'Zero'
    zero_button = 'Login'

    def check_addin_visible(self):


