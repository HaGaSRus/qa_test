import re
from playwright.sync_api import Page, expect


BASE_URL = "https://piter-online.net/"


class MainPage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.goto(BASE_URL, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")

    def open_search_by_address(self) -> None:
        self.page.goto(f"{BASE_URL}orders/tohome")

    def search_address(self, street: str, house: str) -> None:
        full_address = f"{street}, {house}"
        address_input = (
            self.page.get_by_role("combobox")
            .or_(self.page.locator("input[placeholder*='адрес']"))
            .or_(self.page.get_by_label("Введите адрес"))
            .first
        )
        address_input.fill(full_address)
        try:
            self.page.get_by_role("option").first.click(timeout=2000)
        except Exception:
            pass
        self.page.get_by_role("button", name="Найти тарифы").first.click()

    def open_request_form(self) -> None:
        self.page.get_by_role("button", name="Подключить").first.click()

    def fill_request_form(self, name: str, phone: str) -> None:
        form = self.page.get_by_role("dialog").or_(self.page.locator("form")).first
        form.get_by_role("textbox").first.fill(name)
        form.locator("input[type='tel']").fill(phone)

    def submit_request(self) -> None:
        self.page.get_by_role("button", name="Отправить заявку").click()

    def should_see_success_message(self) -> None:
        success = self.page.get_by_text(re.compile(r"заявк|принят|отправлен|спасибо|успешно", re.I))
        expect(success.first).to_be_visible(timeout=10000)

    def change_region(self, region_name: str) -> None:
        self.page.goto(f"{BASE_URL}select-region")
        self.page.get_by_role("link", name=region_name).first.click()

    def current_region_should_be(self, region_name: str) -> None:
        header_region = self.page.get_by_text(region_name).first
        expect(header_region).to_be_visible()