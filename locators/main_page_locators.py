from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON = By.XPATH, '//a[@href="/account"]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[contains(text(),"Конструктор")]'
    LOGIN_TO_ACCOUNT_BUTTON = By.XPATH, '//button[contains(text(),"Войти в аккаунт")]'
    FLUORESCENT_BUN_IMAGE = By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]'
    INGREDIENTS_DETAILS = By.XPATH, '//h2[contains(text(),"Детали ингредиента")]'
    POPUP_WINDOW_CLOSE_BUTTON = By.XPATH, '//section[contains(@class, "modal_opened")]//button[contains(@class,"close_modified")]'
    BASKET = By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]'
    COUNTER_OF_FLUORESCENT_BUN = By.XPATH, '//p[contains(@class,"counter") and text()="2"]'
    ORDER_ID_TITLE = By.XPATH, '//p[contains(text(),"идентификатор заказа")]'
    PLACE_ORDER_BUTTON = By.XPATH, '//button[contains(text(),"Оформить заказ")]'
    ORDER_ID = By.XPATH, '//h2[contains(@class, "modal__title")]'
    LAST_ORDER_ID = By.XPATH, '//h2[contains(@class,"modal__title")]'
