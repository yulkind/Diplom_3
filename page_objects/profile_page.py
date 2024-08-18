from locators.profile_page_locators import ProfilePageLocators


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_order_feed_section(self):
        self.driver.find_element(*ProfilePageLocators.ORDER_FEED_SECTION).click()

    def click_on_logout_section(self):
        self.driver.find_element(*ProfilePageLocators.LOGOUT_SECTION).click()