from dataclasses import dataclass

from playwright.sync_api import Page

from infrastructure import pages as p
from infrastructure.pages.base_page import BasePage


@dataclass
class LoginPageSelectors:
    banner = "#flash-messages"
    header = "h2"
    text = "h4.subheader"
    user_name = 'input[name="username"]'
    user_password = 'input[name="password"]'
    login_button = 'button[type="submit"]'


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.page.locator('input[name="username"]').fill(username)
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('button[type="submit"]')
        if self.page.url == "https://the-internet.herokuapp.com/secure":
            return p.SecurePage(self.page)
        return self

    @property
    def is_open(self):
        return self.page.url == "https://the-internet.herokuapp.com/login"

    @property
    def banner_text(self):
        return self.page.locator(LoginPageSelectors.banner).inner_text()

    @property
    def header_text(self):
        return self.page.locator(LoginPageSelectors.header).inner_text()

    @property
    def body_text(self):
        return self.page.locator(LoginPageSelectors.text).inner_text()
