from selenium.webdriver import ActionChains

from locators.main_page_locators import MainPageLocators


class BasicFunctionality:
    def __init__(self, driver):
        self.driver = driver

    def go_to_constructor(self):
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    def click_on_ingredient(self):
        self.driver.find_element(*MainPageLocators.FLUORESCENT_BUN_IMAGE).click()

    def close_popup_window(self):
        self.driver.find_element(*MainPageLocators.POPUP_WINDOW_CLOSE_BUTTON).click()

    def add_ingredient_to_order(self, driver):
        actions = ActionChains(driver)
        bun_element = driver.find_element(*MainPageLocators.FLUORESCENT_BUN_IMAGE)
        basket_element = driver.find_element(*MainPageLocators.BASKET)
        actions.click_and_hold(bun_element).move_to_element(basket_element).release().perform()

    def place_order(self):
        self.driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).click()
