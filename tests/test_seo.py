from playwright.sync_api import Page, expect

from pages.main_page import BASE_URL


def test_main_page_seo_data(page: Page) -> None: