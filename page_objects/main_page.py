from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_base_url(self):
        self.driver.get(Urls.base_url)

    def click_on_profile_button(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((MainPageLocators.PROFILE_BUTTON)))
        self.driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()
