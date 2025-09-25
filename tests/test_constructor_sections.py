import pytest
from locators import *
from urls import BASE_URL

@pytest.mark.usefixtures("open_constructor")
class TestConstructorSections:

    @pytest.mark.parametrize(
        "section_locator, expected_text",
        [
            (SECTION_BUNS, "Булки"),
            (SECTION_SAUCES, "Соусы"),
            (SECTION_FILLINGS, "Начинки"),
        ],
        ids=["buns", "sauces", "fillings"]
    )
    def test_section_active(self, browser, section_locator, expected_text):
        browser.find_element(*section_locator).click()
        active_tab = browser.find_element(*ACTIVE_TAB)
        assert active_tab.text == expected_text