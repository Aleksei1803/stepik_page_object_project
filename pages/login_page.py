from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login substring is missing from the address"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        input_password.send_keys(password)
        input_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        input_confirm_password.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_CONFIRM)
        button_registration.click()
        success_message = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#messages :nth-child(1) div"))
        )
        success_message = success_message.text
        assert "Thanks for registering!" == success_message
