from playwright.sync_api import Page


class LoginPage:
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = "button[type='submit']"

    def __init__(self, page: Page):
        self.page = page

    def enter_username(self, username: str):
        self.page.locator(self.USERNAME_INPUT).fill(username)

    def enter_password(self, password: str):
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def click_submit(self):
        self.page.locator(self.SUBMIT_BUTTON).click()


def test_user_login(page: Page):
    page.goto("https://example.com/login")
    
    login_page = LoginPage(page)
    login_page.enter_username("test_user")
    login_page.enter_password("secret_pass")
    login_page.click_submit()
