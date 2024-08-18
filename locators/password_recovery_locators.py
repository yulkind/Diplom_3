from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    PASSWORD_RECOVERY_BUTTON = By.XPATH, '//button[contains(text(),"Восстановить")]'
    PASSWORD_SAVE_BUTTON = By.XPATH, '// button[contains(text(), "Сохранить")]'
    PASSWORD_RECOVERY_FIELD = By.XPATH, '//input[@name="Введите новый пароль"]'
    SHOW_PASSWORD_BUTTON = By.XPATH, '//svg[@viewBox="0 0 24 24" and @fill="#8585AD"]'
    PASSWORD_FIELD = By.XPATH, '//body/div[@id="root"]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]'

