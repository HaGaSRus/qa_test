import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage


STREET = "Тестовая линия"
HOUSE = "1"
NAME = "Автотест"
PHONE = "1111111111"


@pytest.mark.parametrize("run", range(5))
def test_submit_application_success(page: Page, run: int) -> None:
    """Проверка успешной отправки заявки через форму на сайте.

    Сценарий:
    1. Открываем главную страницу.
    2. Вводим адрес.
    3. Открываем форму заявки по найденному адресу.
    4. Заполняем поля имени и телефона.
    5. Отправляем форму и убеждаемся, что появилось подтверждение.
    """
    main = MainPage(page)
    main.open()
    main.search_address(STREET, HOUSE)
    main.open_request_form()
    main.fill_request_form(NAME, PHONE)
    main.submit_request()
    main.should_see_success_message()

