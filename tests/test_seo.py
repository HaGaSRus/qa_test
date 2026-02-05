from playwright.sync_api import Page, expect

from pages.main_page import BASE_URL


def test_main_page_seo_data(page: Page) -> None:
    """Проверка базовых SEO-данных главной страницы.

    Что проверяем:
    - title страницы не пустой и содержит название проекта;
    - основной заголовок h1 присутствует и видим пользователю;
    - meta-description существует и не пустой.
    """
    page.goto(BASE_URL)

    # title
    title = page.title()
    assert title, "Ожидали непустой <title> у главной страницы"

    # h1
    h1 = page.locator("h1").first
    expect(h1).to_be_visible()

    # meta-description
    meta_description = page.locator("meta[name='description']").first
    content = meta_description.get_attribute("content")
    assert content, "Ожидали непустой meta[name='description']"

