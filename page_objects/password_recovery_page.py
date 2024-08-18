from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from credentials import Credentials
from locators.login_page_locators import LoginPageLocators
from locators.password_recovery_locators import PasswordRecoveryLocators


class PasswordRecoveryPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_password_recovery_link(self):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK))

    def click_on_password_recovery_link(self):
        self.driver.find_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK).click()

    def set_email(self):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(Credentials.email)

    def click_on_password_recovery_button(self):
        self.driver.find_element(*PasswordRecoveryLocators.PASSWORD_RECOVERY_BUTTON).click()

    def set_new_password(self):
        self.driver.find_element(*PasswordRecoveryLocators.PASSWORD_RECOVERY_FIELD).send_keys(Credentials.password_new)

    def click_on_show_password_button(self):
        self.driver.find_element(*PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON).click()
