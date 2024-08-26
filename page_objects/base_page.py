from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_on_element(self, *locator):
        self.find_element(*locator).click()

    def perform_action(self, action):
        action.perform()

    def move_element(self, source_locator, target_locator):
        actions = ActionChains(self.driver)
        source_element = self.find_element(*source_locator)
        target_element = self.find_element(*target_locator)
        actions.click_and_hold(source_element).move_to_element(target_element).release()
        self.perform_action(actions)

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))

    def go_to(self, base_url):
        self.driver.get(base_url)

    def send_keys_to_element(self, *locator, keys):
        self.find_element(*locator).send_keys(keys)

    def scroll_to_element(self, *locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.find_element(*locator))

    def get_element_text(self, *locator):
        return self.find_element(*locator).text

    def get_element_attribute(self, *locator, attribute_name):
        return self.find_element(*locator).get_attribute(attribute_name)
