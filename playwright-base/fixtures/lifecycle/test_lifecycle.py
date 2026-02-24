from playwright.sync_api import Page


def test_user_login(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.evaluate("localStorage.setItem('auth_token', 'super_secret_token_123')")
    token = page.evaluate("localStorage.getItem('auth_token')")
    assert token == 'super_secret_token_123'


def test_user_is_still_logged_in(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")
    token = page.evaluate("localStorage.getItem('auth_token')")
    assert token == 'super_secret_token_123'
