import pytest
from selenium import webdriver
from pages_methods.base_page import BasePage
from pages_methods.catalog_page import Catalog, Auth
from pages_methods.check_out_page import CheckOut
from pages_methods.online_page import Online


@pytest.fixture()  
def browser(opt_country, opt_branch):
    options = webdriver.ChromeOptions()
    options.add_argument("start-fullscreen")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.sitexample.com")                                 
    if opt_country == "de": 
        driver.add_cookie({"name": "country", "value": "de"})
    elif opt_country == "ru":
        driver.add_cookie({"name": "country", "value": "ru"})
    elif opt_branch == "param1":
        driver.add_cookie({"name":"branch", "value": "feature.param1"})
    elif opt_branch == "param2":
        driver.add_cookie({"name":"branch", "value": "feature.param2"})
    elif opt_branch == "param3":
        driver.add_cookie({"name":"branch", "value": "feature.param3"})
    driver.refresh()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--country", default="ru", choices=("de", "us", "fr", "ru"))
    parser.addoption("--branch", default="", choices=("param1", "param2", "param3"))

@pytest.fixture
def opt_country(request):
    return request.config.getoption("--country")

@pytest.fixture
def opt_branch(request):
    return request.config.getoption("--branch")

@pytest.fixture
def base(browser):
    return BasePage(browser)

@pytest.fixture
def auth(browser):
    return Auth(browser)
    
@pytest.fixture
def catalog(browser):
    return Catalog(browser)

@pytest.fixture
def checkout(browser):
    return CheckOut(browser)

@pytest.fixture
def online(browser):
    return Online(browser)
