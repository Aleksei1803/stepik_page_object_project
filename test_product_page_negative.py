from .pages.main_page import MainPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.click_add_product_to_card()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.click_add_product_to_card()
    product_page.should_element_disappeared()
