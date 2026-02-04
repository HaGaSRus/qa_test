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

    def open_request_form(self) -> None:
        self.page.get_by_role("button", name="Оставить заявку").first.click()

    def fill_request_form(self, name: str, phone: str) -> None:
        self.page.get_by_placeholder("Ваше имя").fill(name)
        self.page.get_by_placeholder("Телефон").fill(phone)

    def submit_request(self) -> None:
        self.page.get_by_role("button", name="Отправить заявку").click()
