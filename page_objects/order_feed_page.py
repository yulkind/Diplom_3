from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from locators.profile_page_locators import ProfilePageLocators


class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_order_feed_page(self):
        self.driver.find_element(*OrderFeedLocators.ORDER_FEED_BUTTON).click()

    def open_last_order(self):
        self.driver.find_element(*OrderFeedLocators.LAST_ORDER).click()

    def get_order_number_from_main_page(self):
        self.driver.find_element(*MainPageLocators.ORDER_ID).get_attribute("class")

    def get_order_number_from_order_feed_section(self):
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.driver.find_element(*ProfilePageLocators.LAST_ORDER_IN_ORDER_FEED_SECTION))
        order_id_element = self.driver.find_element(*ProfilePageLocators.LAST_ORDER_IN_ORDER_FEED_SECTION)
        order_id_text = order_id_element.text
        return order_id_text

    def close_order_popup_window(self):
        self.driver.find_element(*MainPageLocators.ORDER_POPUP_WINDOW_CLOSE_BUTTON).click()

    def get_orders_number_all_time(self):
        order_id_element = WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((OrderFeedLocators.ORDER_FEED_ORDER_ID)))
        order_id_text = order_id_element.text
        return order_id_text

    def get_last_order_number_from_main_page(self):
        order_id_element = self.driver.find_element(*MainPageLocators.LAST_ORDER_ID)
        order_id_text = order_id_element.text
        return order_id_text

    def get_orders_number_today(self):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*OrderFeedLocators.ORDER_FEED_ORDER_ID_TODAY))
        order_id_element = self.driver.find_element(*OrderFeedLocators.ORDER_FEED_ORDER_ID_TODAY)
        order_id_text = order_id_element.text
        return order_id_text

    def get_order_in_progress(self):
        order_id_element = self.driver.find_element(*OrderFeedLocators.ORDER_IN_PROGRESS)
        order_id_text = order_id_element.text
        return order_id_text



