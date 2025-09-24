import pytest
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import BASE_URL

DEFAULT_WAIT = 10  # константа таймаута

def test_successful_registration(browser, new_user_credentials):
    browser.get(f"{BASE_URL}/register")

    # Явное ожидание появления полей регистрации
    wait = WebDriverWait(browser, DEFAULT_WAIT)
    wait.until(EC.visibility_of_element_located(REGISTER_NAME_INPUT))
    wait.until(EC.visibility_of_element_located(REGISTER_EMAIL_INPUT))
    wait.until(EC.visibility_of_element_located(REGISTER_PASSWORD_INPUT))
    wait.until(EC.element_to_be_clickable(REGISTER_SUBMIT_BUTTON))

    browser.find_element(*REGISTER_NAME_INPUT).send_keys(new_user_credentials['name'])
    browser.find_element(*REGISTER_EMAIL_INPUT).send_keys(new_user_credentials['email'])
    browser.find_element(*REGISTER_PASSWORD_INPUT).send_keys(new_user_credentials['password'])
    browser.find_element(*REGISTER_SUBMIT_BUTTON).click()

    # Ждем перехода на страницу профиля (или любую другую страницу успешной регистрации)
    wait.until(EC.url_contains("profile"))

    assert "profile" in browser.current_url


def test_registration_with_invalid_password(browser, new_user_credentials):
    browser.get(f"{BASE_URL}/register")

    wait = WebDriverWait(browser, DEFAULT_WAIT)
    wait.until(EC.visibility_of_element_located(REGISTER_NAME_INPUT))
    wait.until(EC.visibility_of_element_located(REGISTER_EMAIL_INPUT))
    wait.until(EC.visibility_of_element_located(REGISTER_PASSWORD_INPUT))
    wait.until(EC.element_to_be_clickable(REGISTER_SUBMIT_BUTTON))

    browser.find_element(*REGISTER_NAME_INPUT).send_keys(new_user_credentials['name'])
    browser.find_element(*REGISTER_EMAIL_INPUT).send_keys(new_user_credentials['email'])
    
    # Вводим неверный пароль
    browser.find_element(*REGISTER_PASSWORD_INPUT).send_keys("123")
    browser.find_element(*REGISTER_SUBMIT_BUTTON).click()

    # Ожидаем появления сообщения об ошибке.
    # Лучше использовать локатор из locators.py, если есть. Если нет, стоит добавить туда:

    INVALID_PASSWORD_ERROR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")

    error_element = wait.until(EC.visibility_of_element_located(INVALID_PASSWORD_ERROR))
    assert error_element.is_displayed()
