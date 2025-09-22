import pytest
from selenium import webdriver
from utils import generate_login, generate_password

@pytest.fixture
def driver():
    # Инициализируем браузер (Google Chrome для примера)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def new_user_credentials():
    email = generate_login()
    password = generate_password()
    return {'email': email, 'password': password, 'name': 'Test User'}