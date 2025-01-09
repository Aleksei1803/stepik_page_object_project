from .base_page import BasePage
from .locators import MainPageLocators


class ProductPage(BasePage):
    def click_add_product_to_card(self):
        login_link = self.browser.find_element(*MainPageLocators.BUTTON_ADD_PRODUCT)
        login_link.click()