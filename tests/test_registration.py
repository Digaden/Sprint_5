import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from urls import BASE_URL

DEFAULT_WAIT = 10

class TestRegistration:

    def test_successful_registration(self, browser, new_user_credentials):
        browser.get(f"{BASE_URL}/register")
        wait = WebDriverWait(browser, DEFAULT_WAIT)
        wait.until(EC.visibility_of_element_located(REGISTER_NAME_INPUT))

        browser.find_element(*REGISTER_NAME_INPUT).send_keys(new_user_credentials['name'])
        browser.find_element(*REGISTER_EMAIL_INPUT).send_keys(new_user_credentials['email'])
        browser.find_element(*REGISTER_PASSWORD_INPUT).send_keys(new_user_credentials['password'])
        browser.find_element(*REGISTER_SUBMIT_BUTTON).click()

        wait.until(EC.url_contains("profile"))
        assert "profile" in browser.current_url

    def test_registration_invalid_password(self, browser, new_user_credentials):
        browser.get(f"{BASE_URL}/register")
        wait = WebDriverWait(browser, DEFAULT_WAIT)
        wait.until(EC.visibility_of_element_located(REGISTER_NAME_INPUT))

        browser.find_element(*REGISTER_NAME_INPUT).send_keys(new_user_credentials['name'])
        browser.find_element(*REGISTER_EMAIL_INPUT).send_keys(new_user_credentials['email'])
        browser.find_element(*REGISTER_PASSWORD_INPUT).send_keys("123")
        browser.find_element(*REGISTER_SUBMIT_BUTTON).click()

        error = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert error.is_displayed()