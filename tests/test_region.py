import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage


TARGET_REGION = "Санкт-Петербург"


@pytest.mark.parametrize("run", range(5))
def test_change_region_affects_header(page: Page, run: int) -> None:
    main = MainPage(page)
    main.open()
    main.change_region(TARGET_REGION)
    main.current_region_should_be(TARGET_REGION)
