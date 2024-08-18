import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.password_recovery_locators import PasswordRecoveryLocators
from page_objects.main_page import MainPage
from page_objects.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecovery:
    @allure.description("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page.open_base_url()
        main_page.click_on_profile_button()
        password_recovery_page.scroll_to_password_recovery_link()
        password_recovery_page.click_on_password_recovery_link()
        assert driver.find_element(
            *PasswordRecoveryLocators.PASSWORD_RECOVERY_BUTTON).text == 'Восстановить', 'Нет кнопки "Восстановить"'

    @allure.description("Ввод почты и клик по кнопке «Восстановить»")
    def test_password_recovery_button_click(self, driver):
        main_page = MainPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page.open_base_url()
        main_page.click_on_profile_button()
        password_recovery_page.scroll_to_password_recovery_link()
        password_recovery_page.click_on_password_recovery_link()
        password_recovery_page.set_email()
        password_recovery_page.click_on_password_recovery_button()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((PasswordRecoveryLocators.PASSWORD_SAVE_BUTTON)))
        assert driver.find_element(
            *PasswordRecoveryLocators.PASSWORD_SAVE_BUTTON).text == 'Сохранить', 'Нет кнопки "Сохранить"'

    @allure.description("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_password_field_is_active(self, driver):
        main_page = MainPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)
        main_page.open_base_url()
        main_page.click_on_profile_button()
        password_recovery_page.scroll_to_password_recovery_link()
        password_recovery_page.click_on_password_recovery_link()
        password_recovery_page.set_email()
        password_recovery_page.click_on_password_recovery_button()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((PasswordRecoveryLocators.PASSWORD_SAVE_BUTTON)))
        password_recovery_page.set_new_password()
        # Не пришлось использовать данный метод, так как поле уже подсвечено после ввода пароля
        # password_recovery_page.click_on_show_password_button()
        assert "active" in driver.find_element(*PasswordRecoveryLocators.PASSWORD_FIELD).get_attribute("class"), "Поле пароля не стало активным после клика."

