from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class BasicFunctionality(BasePage):

    def go_to_constructor(self):
        self.click_on_element(*MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_on_ingredient(self):
        self.click_on_element(*MainPageLocators.FLUORESCENT_BUN_IMAGE)

    def close_popup_window(self):
        self.click_on_element(*MainPageLocators.POPUP_WINDOW_CLOSE_BUTTON)

    def add_ingredient_to_order(self):
        self.move_element(MainPageLocators.FLUORESCENT_BUN_IMAGE, MainPageLocators.BASKET)

    def place_order(self):
        self.click_on_element(*MainPageLocators.PLACE_ORDER_BUTTON)
