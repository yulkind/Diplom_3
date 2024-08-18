import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from page_objects.basic_functionality import BasicFunctionality
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage


class TestBasicFunctionality:
    @allure.description("Переход по клику на «Конструктор»")
    def test_go_to_constructor_from_profile(self, driver):
        main_page = MainPage(driver)
        basic_functionality = BasicFunctionality(driver)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        basic_functionality.go_to_constructor()
        assert driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).text == 'Войти в аккаунт'

    @allure.description("Появление всплывающего окна после клика на ингредиент")
    def test_open_ingredients_detail(self, driver):
        main_page = MainPage(driver)
        basic_functionality = BasicFunctionality(driver)

        main_page.open_base_url()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.FLUORESCENT_BUN_IMAGE)))
        basic_functionality.click_on_ingredient()
        assert driver.find_element(*MainPageLocators.INGREDIENTS_DETAILS).text == 'Детали ингредиента'

    @allure.description("Закрытие всплывающего окна кликом по крестику")
    def test_popup_window_close(self, driver):
        main_page = MainPage(driver)
        basic_functionality = BasicFunctionality(driver)

        main_page.open_base_url()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((MainPageLocators.FLUORESCENT_BUN_IMAGE)))
        basic_functionality.click_on_ingredient()
        order_feed.close_order_popup_window()
        assert driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).text == 'Войти в аккаунт'

    @allure.description("Увеличение каунтера ингредиента при добавлении его в заказ")
    def test_add_ingredient_to_order(self, driver):
        main_page = MainPage(driver)
        basic_functionality = BasicFunctionality(driver)

        main_page.open_base_url()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.FLUORESCENT_BUN_IMAGE)))
        basic_functionality.add_ingredient_to_order(driver)
        assert "2" in driver.find_element(*MainPageLocators.COUNTER_OF_FLUORESCENT_BUN).get_attribute('innerText')

    @allure.description("Оформление заказа залогиненным пользователем")
    def test_pace_order_by_logged_in_user(self, driver):
        main_page = MainPage(driver)
        basic_functionality = BasicFunctionality(driver)
        login_page = LoginPage(driver)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        login_page.set_login_data()
        login_page.login()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MainPageLocators.PLACE_ORDER_BUTTON)))
        basic_functionality.place_order()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((MainPageLocators.ORDER_ID_TITLE)))
        assert driver.find_element(*MainPageLocators.ORDER_ID_TITLE).text == 'идентификатор заказа'


