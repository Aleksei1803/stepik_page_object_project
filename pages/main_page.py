from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_product_name(self):
        product_name = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".product_main h1"))
        )
        product_name_in_card = self.browser.find_element(By.CSS_SELECTOR, "#messages :nth-child(1) strong")
        assert product_name.text == product_name_in_card.text, "The title of the book doesn't match"

    def should_be_product_price(self):
        product_price = self.browser.find_element(By.CSS_SELECTOR, '[class="price_color"]')
        product_price_in_card = self.browser.find_element(By.CSS_SELECTOR, "#messages :nth-child(3) strong")
        assert product_price.text == product_price_in_card.text, "The price of the book doesn't match"
