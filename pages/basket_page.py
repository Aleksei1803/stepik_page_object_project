from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, 'div.basket-items'), "Basket contains products"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(By.XPATH, '//*[contains(@class , "content")]'), "Basket is not empty"
