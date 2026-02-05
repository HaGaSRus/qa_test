from playwright.sync_api import Page, expect

from pages.main_page import BASE_URL


def test_main_page_seo_data(page: Page) -> None:
    page.goto(BASE_URL)

    title = page.title()
    assert title, "Ожидали непустой <title> у главной страницы"

    h1 = page.locator("h1").first
    expect(h1).to_be_visible()

    meta_description = page.locator("meta[name='description']").first
    content = meta_description.get_attribute("content")
    assert content, "Ожидали непустой meta[name='description']"
