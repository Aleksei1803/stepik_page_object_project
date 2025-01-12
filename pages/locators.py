from selenium.webdriver.common.by import By


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    PRODUCT_PRICE_IN_CARD = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")

class LoginPageLocators :
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    BUTTON_CONFIRM = (By.CSS_SELECTOR, '[name="registration_submit"]')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, '[class ="page_inner"] [class ="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT_LINK = (By.ID, "logout_link")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "#div.basket-items")
    CONTENT_MESSAGE = (By.XPATH, '//*[contains(@class , "content")]')
