import pytest
from selenium import webdriver
from urls import BASE_URL
from helpers import ensure_logged_in, go_to_constructor
from utils import generate_login, generate_password

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def open_constructor(browser):
    browser.get(BASE_URL)
    ensure_logged_in(browser)
    go_to_constructor(browser)

@pytest.fixture
def new_user_credentials():
    email = generate_login()
    password = generate_password()
    return {'email': email, 'password': password, 'name': 'Test User'}

@pytest.fixture(scope="function")
def login(browser):
    browser.get(BASE_URL)
    ensure_logged_in(browser)
    yield
    browser.find_element(*LOGOUT_BUTTON).click()