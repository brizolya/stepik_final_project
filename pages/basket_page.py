from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def is_basket_empty(self):
       assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Basket is not empty"

    def is_message_empty_basket(self): 
        basket_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESS).text
        assert "empty" in basket_empty_message, "There is no message, that basket is empty" 
