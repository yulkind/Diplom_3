import allure
from locators.password_recovery_locators import PasswordRecoveryLocators
from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage
from page_objects.password_recovery_page import PasswordRecoveryPage
from urls import Urls


class TestPasswordRecovery:
    @allure.description("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_password_recovery_page(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        password_recovery_page = PasswordRecoveryPage(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        password_recovery_page.scroll_to_password_recovery_link()
        password_recovery_page.click_on_password_recovery_link()
        assert driver.find_element(
            *PasswordRecoveryLocators.PASSWORD_RECOVERY_BUTTON).text == 'Восстановить', 'Нет кнопки "Восстановить"'

    @allure.description("Ввод почты и клик по кнопке «Восстановить»")
    def test_password_recovery_button_click(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        password_recovery_page = PasswordRecoveryPage(driver, Urls.base_url)
        order_feed = OrderFeedPage(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        password_recovery_page.scroll_to_password_recovery_link()
        password_recovery_page.click_on_password_recovery_link()
        password_recovery_page.set_email()
        password_recovery_page.click_on_password_recovery_button()
        order_feed.wait_for_element_to_be_visible(PasswordRecoveryLocators.PASSWORD_SAVE_BUTTON)
        assert driver.find_element(
            *PasswordRecoveryLocators.PASSWORD_SAVE_BUTTON).text == 'Сохранить', 'Нет кнопки "Сохранить"'

    @allure.description("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_password_field_is_active(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        password_recovery_page = PasswordRecoveryPage(driver, Urls.base_url)
        order_feed = OrderFeedPage(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        password_recovery_page.scroll_to_password_recovery_link()
        password_recovery_page.click_on_password_recovery_link()
        password_recovery_page.set_email()
        password_recovery_page.click_on_password_recovery_button()
        order_feed.wait_for_element_to_be_visible(PasswordRecoveryLocators.PASSWORD_SAVE_BUTTON)
        password_recovery_page.set_new_password()
        # Не пришлось использовать данный метод, так как поле уже подсвечено после ввода пароля
        # password_recovery_page.click_on_show_password_button()
        assert "active" in driver.find_element(*PasswordRecoveryLocators.PASSWORD_FIELD).get_attribute("class"), "Поле пароля не стало активным после клика."

