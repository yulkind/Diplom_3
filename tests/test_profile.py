import allure
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from page_objects.basic_functionality import BasicFunctionality
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage
from page_objects.profile_page import ProfilePage
from urls import Urls


class TestProfile:
    @allure.description("Переход по клику на «Личный кабинет»")
    def test_go_to_login_page(self, driver):
        main_page = MainPage(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).text == 'Войти', 'Нет кнопки "Войти'

    @allure.description("Переход в раздел «История заказов»")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        login_page = LoginPage(driver, Urls.base_url)
        profile_page = ProfilePage(driver, Urls.base_url)
        order_feed = OrderFeedPage(driver, Urls.base_url)
        basic_functionality = BasicFunctionality(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        login_page.set_login_data()
        login_page.login()
        order_feed.wait_for_element_to_be_visible(MainPageLocators.PLACE_ORDER_BUTTON)
        basic_functionality.add_ingredient_to_order()
        basic_functionality.place_order()
        order_feed.close_order_popup_window()
        main_page.click_on_profile_button()
        profile_page.go_to_order_feed_section()
        order_number = order_feed.get_order_number_from_order_feed_section()
        assert order_number != '', 'Не найден номер заказа'

    @allure.description("Выход из аккаунта")
    def test_logout(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        login_page = LoginPage(driver, Urls.base_url)
        profile_page = ProfilePage(driver, Urls.base_url)
        order_feed = OrderFeedPage(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        login_page.set_login_data()
        login_page.login()
        main_page.click_on_profile_button()
        order_feed.wait_for_element_to_be_visible(ProfilePageLocators.LOGOUT_SECTION)
        profile_page.click_on_logout_section()
        order_feed.wait_for_element_to_be_visible(LoginPageLocators.LOGIN_BUTTON)
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).text == "Войти", "Выход из аккаунта не произошёл"
