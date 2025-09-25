from locators import *
import pytest

@pytest.mark.usefixtures("login")
class TestNavigation:

    def test_profile_to_constructor(self, browser):
        browser.find_element(*PROFILE_LINK).click()
        assert "account" in browser.current_url or browser.find_element(*LOGOUT_BUTTON).is_displayed()

        browser.find_element(*CONSTRUCTOR_LINK).click()
        assert "react-burger" in browser.current_url or browser.find_element(*SECTION_BUNS).is_displayed()

    def test_logout(self, browser):
        browser.find_element(*PROFILE_LINK).click()
        browser.find_element(*LOGOUT_BUTTON).click()
        assert browser.find_element(*LOGIN_BUTTON_MAIN).is_displayed()