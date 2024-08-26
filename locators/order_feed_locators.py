from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_BUTTON = By.XPATH, '//p[contains(text(),"Лента Заказов")]'
    ORDER_FEED_TITLE = By.XPATH, '//h1[contains(@class, "text_type_main-large") and contains(text(), "Лента заказов")]'
    INGREDIENTS_TITLE = By.XPATH, '//p[contains(text(),"Cостав")]'
    ORDER_FEED_ORDER_ID = By.XPATH, '//p[contains(@class,"OrderFeed_number")][1]'
    ORDER_FEED_LAST_ORDER_ID = By.XPATH, '//p[contains(@class, "text") and contains(text(), "#")][1]'
    ORDER_FEED_ORDER_ID_TODAY = By.XPATH, '//p[contains(@class,"OrderFeed_number")][2]'
    ORDER_IN_PROGRESS = By.XPATH, '//li[contains(@class,"text_type_main")]'
