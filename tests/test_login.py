import pytest
from selenium.webdriver.common.by import By
from locators import *

from urls import BASE_URL

@pytest.mark.parametrize("email,password", [
    ("testuser@example.com", "correct_password"),  # валидные данные
    ("testuser@example.com", "wrong_password"),    # неверный пароль
    ("", "any_password"),                           # пустой email
    ("testuser@example.com", ""),                   # пустой пароль
])
def test_login_variants(browser, email, password):
    # Открыть страницу входа
    browser.get(BASE_URL)
    browser.find_element(*LOGIN_BUTTON_MAIN).click()
    
    # Ввести логин и пароль
    browser.find_element(*LOGIN_EMAIL_INPUT).clear()
    browser.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    browser.find_element(*LOGIN_PASSWORD_INPUT).clear()
    browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    browser.find_element(*LOGIN_SUBMIT_BUTTON).click()
    
    if email == "testuser@example.com" and password == "correct_password":
        # Ожидается вход — появление Личного кабинета
        profile = browser.find_element(*PROFILE_LINK)
        assert profile.is_displayed()
    else:
        # Проверка, что остались на странице входа или есть ошибка
        error_elements = browser.find_elements(*ERROR_MESSAGE)
        assert error_elements and any(e.is_displayed() for e in error_elements)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_via_register_form(browser):
    """Проверка перехода на логин из формы регистрации."""
    browser.get(BASE_URL)
    browser.find_element(*LOGIN_BUTTON_MAIN).click()
    # Нажать ссылку Войти в форме регистрации
    browser.find_element(*REGISTER_LOGIN_LINK).click()
    
    # Явное ожидание появления кнопки "Войти"
    wait = WebDriverWait(browser, 10)
    login_button = wait.until(EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON))

    assert login_button.is_displayed()
