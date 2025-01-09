from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    BUTTON_ADD_PRODUCT = (By.CSS_SELECTOR, ".btn-add-to-basket")

class LoginPageLocators :
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
