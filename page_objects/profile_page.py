from locators.profile_page_locators import ProfilePageLocators
from page_objects.base_page import BasePage


class ProfilePage(BasePage):

    def go_to_order_feed_section(self):
        self.wait_for_element_to_be_clickable(*ProfilePageLocators.ORDER_FEED_SECTION)
        self.click_on_element(*ProfilePageLocators.ORDER_FEED_SECTION)

    def click_on_logout_section(self):
        self.click_on_element(*ProfilePageLocators.LOGOUT_SECTION)
