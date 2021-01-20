from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REG_LINK = (By.CSS_SELECTOR, "#register_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTR_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTR_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTR_PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTR_SUBM_BUTT = (By.NAME, "registration_submit")

class ProductPageLocators():
    BTN_ADD_TO_BSK = (By.CLASS_NAME, "btn-add-to-basket")
    MESS_SUCCESS = (By.CSS_SELECTOR, ".alertinner > strong")
    TITLE_OF_BOOK = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_IN_MESS = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRICE_IN_ITEM = (By.CSS_SELECTOR, ".product_main > .price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini  a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_SUMMARY = (By.CSS_SELECTOR, "form.basket_summary")
    BASKET_IS_EMPTY_MESS = (By.CSS_SELECTOR, "#content_inner > p")