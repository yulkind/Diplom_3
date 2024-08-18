from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON = By.XPATH, '//a[@href="/account"]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[contains(text(),"Конструктор")]'
    LOGIN_TO_ACCOUNT_BUTTON = By.XPATH, '//button[contains(text(),"Войти в аккаунт")]'
    FLUORESCENT_BUN_IMAGE = By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]'
    INGREDIENTS_DETAILS = By.XPATH, '//h2[contains(text(),"Детали ингредиента")]'
    POPUP_WINDOW_CLOSE_BUTTON = By.XPATH, '//body/div[@id="root"]/div[1]/section[1]/div[1]/button[1]/*[1]'
    BASKET = By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]'
    COUNTER_OF_FLUORESCENT_BUN = By.XPATH, '//p[@class="counter_counter__num__3nue1" and text()="2"]'
    ORDER_ID_TITLE = By.XPATH, '//p[contains(text(),"идентификатор заказа")]'
    PLACE_ORDER_BUTTON = By.XPATH, '//button[contains(text(),"Оформить заказ")]'
    ORDER_ID = By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'
    ORDER_POPUP_WINDOW_CLOSE_BUTTON = By.XPATH, '//body/div[@id="root"]/div[1]/section[1]/div[1]/button[1]'
    LAST_ORDER_ID = By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]'