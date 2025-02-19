from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_product_to_card(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT)
        login_link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_element_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should be"

    def should_be_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_card = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CARD)
        assert product_name.text == product_name_in_card.text, "The title of the book doesn't match"

    def should_be_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_card = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CARD)
        assert product_price.text == product_price_in_card.text, "The price of the book doesn't match"

