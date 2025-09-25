import pytest
from locators import *
from urls import BASE_URL

@pytest.mark.parametrize(
    "email, password, expected_profile, expected_error",
    [
        ("testuser@example.com", "correct_password", True, False),
        ("testuser@example.com", "wrong_password", False, True),
        ("", "any_password", False, True),
        ("testuser@example.com", "", False, True),
    ],
    ids=["valid_login", "wrong_password", "empty_email", "empty_password"]
)
def test_login_variants(browser, email, password, expected_profile, expected_error):
    browser.get(BASE_URL)
    browser.find_element(*LOGIN_BUTTON_MAIN).click()

    browser.find_element(*LOGIN_EMAIL_INPUT).clear()
    browser.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    browser.find_element(*LOGIN_PASSWORD_INPUT).clear()
    browser.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    browser.find_element(*LOGIN_SUBMIT_BUTTON).click()

    profile_present = browser.find_elements(*PROFILE_LINK)
    profile_displayed = bool(profile_present and profile_present[0].is_displayed())

    error_elements = browser.find_elements(*ERROR_MESSAGE)
    error_displayed = any(e.is_displayed() for e in error_elements)

    assert profile_displayed == expected_profile
    assert error_displayed == expected_error