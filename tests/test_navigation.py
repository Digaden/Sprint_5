import pytest
from locators import *

BASE_URL = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture(scope="function")
def login(browser):
    browser.get(BASE_URL)
    browser.find_element(*LOGIN_BUTTON_MAIN).click()
    browser.find_element(*LOGIN_EMAIL_INPUT).send_keys("testuser@example.com")
    browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys("correct_password")
    browser.find_element(*LOGIN_SUBMIT_BUTTON).click()
    yield
    # В конце теста сделать выход
    browser.find_element(*LOGOUT_BUTTON).click()

def test_navigate_profile_and_constructor(browser, login):
    # Находим и кликаем "Личный кабинет"
    browser.find_element(*PROFILE_LINK).click()
    assert "account" in browser.current_url or browser.find_element(*LOGOUT_BUTTON).is_displayed()
    
    # Кликаем на конструктор
    browser.find_element(*CONSTRUCTOR_LINK).click()
    assert "react-burger" in browser.current_url or browser.find_element(*SECTION_BUNS).is_displayed()

def test_logout_function(browser, login):
    # В личном кабинете нажимаем выход
    browser.find_element(*PROFILE_LINK).click()
    browser.find_element(*LOGOUT_BUTTON).click()
    # Проверяем, что вернулись на главную или нажата кнопка "Войти в аккаунт"
    assert browser.find_element(*LOGIN_BUTTON_MAIN).is_displayed()