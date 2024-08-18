from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ORDER_FEED_SECTION = By.XPATH, '//a[contains(text(),"История заказов")]'
    LOGOUT_SECTION = By.XPATH, '//button[contains(text(),"Выход")]'
    ORDER_ID_IN_ORDER_FEED = By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/div[1]/p[1]'
    LAST_ORDER_IN_ORDER_FEED_SECTION = By.XPATH, '(//p[@class="text text_type_digits-default"])[last()]'