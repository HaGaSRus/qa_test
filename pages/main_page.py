from playwright.sync_api import Page, expect


BASE_URL = "https://piter-online.net/"


class MainPage:
    """Page Object для главной страницы piter-online.net."""

    def __init__(self, page: Page) -> None:
        self.page = page

