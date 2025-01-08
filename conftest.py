import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                 help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = chrome_options()
    options.add_argument('lang=' + user_language)
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
