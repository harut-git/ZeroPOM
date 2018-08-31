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
    username = 'Username'
    password = 'Password'
    login = 'Login'

    def check_addin_visible(self):
        addin_text = self.wait_and_get_name(self.zero_text, 35)
        addin_button = self.wait_and_get_name(self.zero_button, 35)
        print addin_button.get_attribute('HelpText') + ' is displayed'
        print addin_text.get_attribute('Name') + ' is displayed'

    def nd_frame_login(self):
        username_field = self.get_name(self.username)
        password_field = self.get_name(self.password)
        login_button = self.get_name(self.login)
        username_field.send_keys("qa@zeroapp.ai")
        password_field.send_keys("InboxZero123")
        login_button.click()

    def addin_login(self):
        login_button = self.get_name(self.zero_button)
        login_button.click()
