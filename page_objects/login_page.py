from credentials import Credentials
from locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_password_recovery_link(self):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK))

    def click_on_password_recovery_link(self):
        self.driver.find_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK).click()

    def set_login_data(self):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(Credentials.email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(Credentials.password_old)

    def login(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
