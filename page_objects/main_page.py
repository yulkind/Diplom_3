from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):

    def open_base_url(self):
        self.go_to(self.base_url)

    def click_on_profile_button(self):
        self.wait_for_element_to_be_visible(MainPageLocators.PROFILE_BUTTON)
        self.click_on_element(*MainPageLocators.PROFILE_BUTTON)
