from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_item_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BSK)
        button_basket.click()

    def is_element_in_basket(self):
        messages_success = self.browser.find_element(*ProductPageLocators.MESS_SUCCESS).text
        book_titel = self.browser.find_element(*ProductPageLocators.TITLE_OF_BOOK).text
        assert book_titel == messages_success, "Incorrect message! There is no title of the book"

    def is_item_price_in_basket(self):
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESS).text
        price_item = self.browser.find_element(*ProductPageLocators.PRICE_IN_ITEM).text
        assert price_message == price_item, "The price of the item matches the price in the message"
