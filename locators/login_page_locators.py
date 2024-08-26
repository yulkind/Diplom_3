from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_LINK = By.XPATH, '//a[@href="/forgot-password"]'
    LOGIN_BUTTON = By.XPATH, '//button[contains(text(),"Войти")]'
    EMAIL_FIELD = By.XPATH, '//input[@name="name" and @type="text"]'
    PASSWORD_FIELD = By.XPATH, '//input[@name="Пароль"]'
