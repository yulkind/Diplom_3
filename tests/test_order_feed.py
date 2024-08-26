import allure
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from locators.profile_page_locators import ProfilePageLocators
from page_objects.basic_functionality import BasicFunctionality
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage
from page_objects.profile_page import ProfilePage
from urls import Urls


class TestOrderFeed:
    @allure.description("Открытие всплывающего окна с деталями при клике на заказ")
    def test_open_last_order(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        order_feed = OrderFeedPage(driver, Urls.base_url)

        main_page.open_base_url()
        order_feed.go_to_order_feed_page()
        order_feed.wait_for_element_to_be_visible(OrderFeedLocators.ORDER_FEED_TITLE)
        order_feed.open_last_order()
        assert order_feed.find_element(*OrderFeedLocators.INGREDIENTS_TITLE).text == 'Cостав'

    @allure.description("Отображение заказов пользователя из раздела «История заказов» на странице «Лента заказов»")
    def test_created_order_is_displayed_in_order_feed(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        order_feed = OrderFeedPage(driver, Urls.base_url)
        login_page = LoginPage(driver, Urls.base_url)
        basic_functionality = BasicFunctionality(driver, Urls.base_url)
        profile_page = ProfilePage(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        login_page.set_login_data()
        login_page.login()
        order_feed.wait_for_element_to_be_visible(MainPageLocators.PLACE_ORDER_BUTTON)
        basic_functionality.add_ingredient_to_order()
        basic_functionality.place_order()
        order_feed.wait_for_element_to_be_visible(MainPageLocators.ORDER_ID_TITLE)

        order_feed.close_order_popup_window()
        main_page.click_on_profile_button()
        order_feed.wait_for_element_to_be_visible(ProfilePageLocators.ORDER_FEED_SECTION)
        profile_page.go_to_order_feed_section()

        order_from_order_feed_section = order_feed.get_order_number_from_order_feed_section()
        order_feed.go_to_order_feed_page()
        order_feed.wait_for_element_to_be_visible(OrderFeedLocators.ORDER_FEED_LAST_ORDER_ID)
        order_from_main_page = order_feed.get_last_order_number_from_main_page()

        assert order_from_main_page == order_from_order_feed_section

    @allure.description("Увеличение счётчика «Выполнено за всё» время при создании нового заказа")
    def test_counter_all_time_increases(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        login_page = LoginPage(driver, Urls.base_url)
        basic_functionality = BasicFunctionality(driver, Urls.base_url)
        order_feed = OrderFeedPage(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        login_page.set_login_data()
        login_page.login()
        order_feed.wait_for_element_to_be_visible(MainPageLocators.PLACE_ORDER_BUTTON)
        order_feed.go_to_order_feed_page()
        order_feed.wait_for_element_to_be_visible(OrderFeedLocators.ORDER_FEED_ORDER_ID)
        order_id = order_feed.get_orders_number_all_time()
        basic_functionality.go_to_constructor()
        basic_functionality.add_ingredient_to_order()
        basic_functionality.place_order()
        order_feed.wait_for_element_to_be_visible(MainPageLocators.ORDER_ID_TITLE)

        order_feed.close_order_popup_window()
        order_feed.go_to_order_feed_page()
        order_feed.wait_for_element_to_be_visible(OrderFeedLocators.ORDER_FEED_ORDER_ID)
        new_order_id = order_feed.get_orders_number_all_time()
        assert int(new_order_id) == int(order_id) + 1

    @allure.description("Увеличение счётчика «Выполнено за всё время» при создании нового заказа")
    def test_counter_today_increases(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        login_page = LoginPage(driver, Urls.base_url)
        basic_functionality = BasicFunctionality(driver, Urls.base_url)
        order_feed = OrderFeedPage(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        login_page.set_login_data()
        login_page.login()
        order_feed.wait_for_element_to_be_visible(MainPageLocators.PLACE_ORDER_BUTTON)
        order_feed.go_to_order_feed_page()
        order_feed.wait_for_element_to_be_visible(OrderFeedLocators.ORDER_FEED_ORDER_ID)
        order_id = order_feed.get_orders_number_today()
        basic_functionality.go_to_constructor()
        basic_functionality.add_ingredient_to_order()
        basic_functionality.place_order()
        order_feed.wait_for_element_to_be_visible(MainPageLocators.ORDER_ID_TITLE)

        order_feed.close_order_popup_window()
        order_feed.go_to_order_feed_page()
        order_feed.wait_for_element_to_be_visible(OrderFeedLocators.ORDER_FEED_ORDER_ID)
        new_order_id = order_feed.get_orders_number_today()
        assert int(new_order_id) == int(order_id) + 1

    @allure.description("Появление номера заказа после его оформления в разделе «В работе»")
    def test_order_in_progress_correct_number(self, driver):
        main_page = MainPage(driver, Urls.base_url)
        login_page = LoginPage(driver, Urls.base_url)
        basic_functionality = BasicFunctionality(driver, Urls.base_url)
        order_feed = OrderFeedPage(driver, Urls.base_url)

        main_page.open_base_url()
        main_page.click_on_profile_button()
        login_page.set_login_data()
        login_page.login()
        order_feed.wait_for_element_to_be_visible(MainPageLocators.PLACE_ORDER_BUTTON)
        basic_functionality.add_ingredient_to_order()
        basic_functionality.place_order()
        order_feed.wait_for_element_to_be_visible(MainPageLocators.ORDER_ID_TITLE)

        order_id = order_feed.get_last_order_number_from_main_page()
        order_feed.close_order_popup_window()
        order_feed.go_to_order_feed_page()
        order_feed.wait_for_element_to_be_visible(OrderFeedLocators.ORDER_IN_PROGRESS)

        new_order_id = order_feed.get_order_in_progress()

        assert int(new_order_id) == int(order_id)
