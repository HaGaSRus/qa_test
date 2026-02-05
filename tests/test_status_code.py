import pytest
from playwright.sync_api import Page

from pages.main_page import BASE_URL


@pytest.mark.parametrize("run", range(5))
def test_main_page_returns_200(page: Page, run: int) -> None:
    response = page.request.get(BASE_URL)
    assert response.status == 200
