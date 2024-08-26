from credentials import Credentials
from locators.login_page_locators import LoginPageLocators
from page_objects.base_page import BasePage


class LoginPage(BasePage):

    def scroll_to_password_recovery_link(self):
        self.scroll_to_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK)

    def click_on_password_recovery_link(self):
        self.click_on_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK)

    def set_login_data(self):
        self.send_keys_to_element(*LoginPageLocators.EMAIL_FIELD, keys=Credentials.email)
        self.send_keys_to_element(*LoginPageLocators.PASSWORD_FIELD, keys=Credentials.password_old)

    def login(self):
        self.click_on_element(*LoginPageLocators.LOGIN_BUTTON)
