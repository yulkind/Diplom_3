from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from locators.profile_page_locators import ProfilePageLocators
from page_objects.base_page import BasePage


class OrderFeedPage(BasePage):

    def go_to_order_feed_page(self):
        self.click_on_element(*OrderFeedLocators.ORDER_FEED_BUTTON)

    def open_last_order(self):
        self.click_on_element(*OrderFeedLocators.ORDER_FEED_LAST_ORDER_ID)

    def get_order_number_from_main_page(self):
        return self.get_element_attribute(*MainPageLocators.ORDER_ID, "class")

    def get_order_number_from_order_feed_section(self):
        self.scroll_to_element(*ProfilePageLocators.LAST_ORDER_IN_ORDER_FEED_SECTION)
        return self.get_element_text(*ProfilePageLocators.LAST_ORDER_IN_ORDER_FEED_SECTION)

    def close_order_popup_window(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.POPUP_WINDOW_CLOSE_BUTTON, timeout=10)
        self.click_on_element(*MainPageLocators.POPUP_WINDOW_CLOSE_BUTTON)

    def get_orders_number_all_time(self):
        self.wait_for_element_to_be_visible(OrderFeedLocators.ORDER_FEED_ORDER_ID, timeout=10)
        return self.get_element_text(*OrderFeedLocators.ORDER_FEED_ORDER_ID)

    def get_last_order_number_from_main_page(self):
        return self.get_element_text(*MainPageLocators.LAST_ORDER_ID)

    def get_orders_number_today(self):
        self.scroll_to_element(*OrderFeedLocators.ORDER_FEED_ORDER_ID_TODAY)
        return self.get_element_text(*OrderFeedLocators.ORDER_FEED_ORDER_ID_TODAY)

    def get_order_in_progress(self):
        return self.get_element_text(*OrderFeedLocators.ORDER_IN_PROGRESS)



