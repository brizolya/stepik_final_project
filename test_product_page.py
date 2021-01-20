from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import pytest
import time

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        page_register = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = "H8PywKmDte278Ls"
        page_register.register_new_user(email, password)
        page_register.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser): 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        page_with_messages = ProductPage(browser, browser.current_url, 5)
        page_with_messages.is_element_in_basket()
        page_with_messages.is_item_price_in_basket()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        page_basket = BasketPage(browser, browser.current_url)
        page_basket.is_basket_empty()
        page_basket.is_message_empty_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page_with_messages = ProductPage(browser, browser.current_url, 5)
    page_with_messages.is_element_in_basket()
    page_with_messages.is_item_price_in_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.is_basket_empty()
    page_basket.is_message_empty_basket()