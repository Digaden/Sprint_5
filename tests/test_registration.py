import pytest
from locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://stellarburgers.nomoreparties.site"

def test_successful_registration(driver, new_user_credentials):
    driver.get(f"{BASE_URL}/register")

    driver.find_element(*REGISTER_NAME_INPUT).send_keys(new_user_credentials['name'])
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(new_user_credentials['email'])
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(new_user_credentials['password'])
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    # ждем перехода на страницу после успешной регистрации — например, в личный кабинет
    WebDriverWait(driver, 5).until(EC.url_contains("profile"))

    assert "profile" in driver.current_url

def test_registration_with_invalid_password(driver, new_user_credentials):
    driver.get(f"{BASE_URL}/register")

    driver.find_element(*REGISTER_NAME_INPUT).send_keys(new_user_credentials['name'])
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(new_user_credentials['email'])
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys("123")  # короткий пароль
    driver.find_element(*REGISTER_SUBMIT_BUTTON).click()

    # Ожидаем появления ошибки — здесь пример, надо уточнить по сайту
    error_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]"))
    )
    assert error_element.is_displayed()