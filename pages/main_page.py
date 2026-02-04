from playwright.sync_api import Page, expect


BASE_URL = "https://piter-online.net/"


class MainPage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.goto(BASE_URL)

    def search_address(self, street: str, house: str) -> None:
        full_address = f"{street}, {house}"
        address_input = self.page.get_by_placeholder("Улица и дом").first
        address_input.fill(full_address)
        self.page.get_by_role("button", name="Найти").click()

    