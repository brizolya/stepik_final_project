from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REG_LINK = (By.CSS_SELECTOR, "#register_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    BTN_ADD_TO_BSK = (By.CLASS_NAME, "btn-add-to-basket")
    MESS_SUCCESS = (By.CSS_SELECTOR, ".alertinner > strong")
    TITLE_OF_BOOK = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_IN_MESS = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRICE_IN_ITEM = (By.CSS_SELECTOR, ".product_main > .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")