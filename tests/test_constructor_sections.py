import pytest
from locators import *

BASE_URL = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture(scope="function")
def open_constructor(browser):
    browser.get(BASE_URL)
    # Авторизоваться, если нужно (зависит от сайта)
    if browser.find_elements(*LOGIN_BUTTON_MAIN):
        browser.find_element(*LOGIN_BUTTON_MAIN).click()
        browser.find_element(*LOGIN_EMAIL_INPUT).send_keys("testuser@example.com")
        browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys("correct_password")
        browser.find_element(*LOGIN_SUBMIT_BUTTON).click()
    # Перейти на конструктор
    browser.find_element(*CONSTRUCTOR_LINK).click()
    yield

def test_buns_section_active(browser, open_constructor):
    browser.find_element(*SECTION_BUNS).click()
    active_tab = browser.find_element(*ACTIVE_TAB)
    assert active_tab.text == "Булки"

def test_sauces_section_active(browser, open_constructor):
    browser.find_element(*SECTION_SAUCES).click()
    active_tab = browser.find_element(*ACTIVE_TAB)
    assert active_tab.text == "Соусы"

def test_fillings_section_active(browser, open_constructor):
    browser.find_element(*SECTION_FILLINGS).click()
    active_tab = browser.find_element(*ACTIVE_TAB)
    assert active_tab.text == "Начинки"