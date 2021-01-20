from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #driver = WebDriver()
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, "URL-adress is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "There is no the login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_LINK), "There is no registration form"
    
    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTR_EMAIL_INPUT)
        reg_email.send_keys(email)
        reg_pass = self.browser.find_element(*LoginPageLocators.REGISTR_PASS)
        reg_pass.send_keys(password)
        reg_pass_conf = self.browser.find_element(*LoginPageLocators.REGISTR_PASS_CONFIRM)
        reg_pass_conf.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTR_SUBM_BUTT).click()