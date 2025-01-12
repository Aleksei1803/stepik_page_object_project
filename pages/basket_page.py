from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket contains products"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.CONTENT_MESSAGE), "Basket is not empty"
