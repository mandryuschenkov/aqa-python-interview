from playwright.sync_api import Page


def test_search_autocomplete_fill(page: Page):
    page.goto("https://example.com/search")
    
    page.get_by_placeholder("Search").fill("Playwright")
    page.get_by_role("option").first.click()


def test_search_autocomplete_type(page: Page):
    page.goto("https://example.com/search")
    
    page.get_by_placeholder("Search").type("Playwright", delay=100)
    page.get_by_role("option").first.click()
