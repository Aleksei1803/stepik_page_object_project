from .pages.main_page import MainPage
from .pages.product_page import ProductPage

def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.click_add_product_to_card()
    page.solve_quiz_and_get_code()
    page.should_be_product_name()
    page.should_be_product_price()
