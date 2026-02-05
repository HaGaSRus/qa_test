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

    def should_see_success_message(self) -> None:
        success = self.page.get_by_text("заявка принята", exact=False)
        expect(success).to_be_visible()

    def change_region(self, region_name: str) -> None:
        self.page.get_by_role("button", name="Ваш регион").click()
        self.page.get_by_role("button", name=region_name).click()

    def current_region_should_be(self, region_name: str) -> None:
        header_region = self.page.get_by_role("button", name=region_name)
        expect(header_region).to_be_visible()