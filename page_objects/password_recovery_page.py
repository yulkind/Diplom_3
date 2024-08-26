from credentials import Credentials
from locators.login_page_locators import LoginPageLocators
from locators.password_recovery_locators import PasswordRecoveryLocators
from page_objects.base_page import BasePage


class PasswordRecoveryPage(BasePage):


    def scroll_to_password_recovery_link(self):
        self.scroll_to_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK)

    def click_on_password_recovery_link(self):
        self.click_on_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK)

    def set_email(self):
        self.send_keys_to_element(*LoginPageLocators.EMAIL_FIELD, keys=Credentials.email)

    def click_on_password_recovery_button(self):
        self.click_on_element(*PasswordRecoveryLocators.PASSWORD_RECOVERY_BUTTON)

    def set_new_password(self):
        self.send_keys_to_element(*PasswordRecoveryLocators.PASSWORD_RECOVERY_FIELD, keys=Credentials.password_new)

    def click_on_show_password_button(self):
        self.click_on_element(*PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON)
