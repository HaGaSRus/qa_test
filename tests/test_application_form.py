import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage

STREET = "Тестовая линия"
HOUSE = "1"
NAME = "Автотест"
PHONE = "1111111111"


@pytest.mark.parametrize("run", range(5))
def test_submit_application_success(page: Page, run: int) -> None:
    main = MainPage(page)
    main.open()
    main.search_address(STREET, HOUSE)
    main.open_request_form()
    main.fill_request_form(NAME, PHONE)
    main.submit_request()
    main.should_see_success_message()
