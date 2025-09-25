from locators import *

def ensure_logged_in(browser, email="testuser@example.com", password="correct_password"):
    """Логин в систему, если пользователь не авторизован."""
    if browser.find_elements(*LOGIN_BUTTON_MAIN):
        browser.find_element(*LOGIN_BUTTON_MAIN).click()
        browser.find_element(*LOGIN_EMAIL_INPUT).clear()
        browser.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        browser.find_element(*LOGIN_PASSWORD_INPUT).clear()
        browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        browser.find_element(*LOGIN_SUBMIT_BUTTON).click()

def go_to_constructor(browser):
    """Открыть страницу конструктора."""
    browser.find_element(*CONSTRUCTOR_LINK).click()