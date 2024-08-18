from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_BUTTON = By.XPATH, '//p[contains(text(),"Лента Заказов")]'
    ORDER_FEED_TITLE = By.XPATH, '//h1[contains(@class, "text_type_main-large") and contains(text(), "Лента заказов")]'
    LAST_ORDER = By.XPATH, '//body/div[@id="root"]/div[1]/main[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]'
    INGREDIENTS_TITLE = By.XPATH, '//p[contains(text(),"Cостав")]'
    ORDER_FEED_ORDER_ID = By.XPATH, '//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"][1]'
    ORDER_FEED_LAST_ORDER_ID = By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/p[1]'
    ORDER_FEED_ORDER_ID_TODAY = By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[3]/p[2]'
    ORDER_IN_PROGRESS = By.XPATH, '//li[@class="text text_type_main-small"]'





