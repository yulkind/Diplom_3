import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.profile_page import ProfilePage


class TestProfile:
    @allure.description("Переход по клику на «Личный кабинет»")
    def test_go_to_login_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_base_url()
        main_page.click_on_profile_button()
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).text == 'Войти', 'Нет кнопки "Войти'

    @allure.description("Переход в раздел «История заказов»")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        login_page.set_login_data()
        login_page.login()
        main_page.click_on_profile_button()
        profile_page.go_to_order_feed_section()
        #нужно предварительно создать заказ

    @allure.description("Выход из аккаунта")
    def test_logout(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        login_page.set_login_data()
        login_page.login()
        main_page.click_on_profile_button()
        WebDriverWait(driver, 10). until(expected_conditions.element_to_be_clickable((ProfilePageLocators.LOGOUT_SECTION)))
        profile_page.click_on_logout_section()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LoginPageLocators.LOGIN_BUTTON)))
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).text == "Войти", "Выход из аккаунта не произошёл"