import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage


TARGET_REGION = "Санкт-Петербург"


@pytest.mark.parametrize("run", range(5))
def test_change_region_affects_header(page: Page, run: int) -> None:
    """Проверка смены региона и отображения выбранного региона в шапке.

    Сценарий:
    1. Открываем главную страницу.
    2. Открываем селектор региона.
    3. Выбираем регион TARGET_REGION.
    4. Убеждаемся, что выбранный регион отображается в шапке.
    """
    main = MainPage(page)
    main.open()
    main.change_region(TARGET_REGION)
    main.current_region_should_be(TARGET_REGION)

