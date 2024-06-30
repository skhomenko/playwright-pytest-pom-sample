from dataclasses import dataclass

from playwright.sync_api import Page

from infrastructure import pages as p
from infrastructure.pages.base_page import BasePage


@dataclass
class SecurePageSelectors:
    banner = "#flash-messages"
    header = "h2:has(.icon-lock)"
    text = "h4.subheader"
    logout_button = 'i.icon-2x.icon-signout:has-text("Logout")'


class SecurePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.s = SecurePageSelectors()
        self.page.locator(self.s.header).wait_for()

    @property
    def is_open(self):
        return self.page.url == "https://the-internet.herokuapp.com/secure"

    def logout(self):
        self.page.locator(self.s.logout_button).click()
        return p.LoginPage(self.page)

    @property
    def header_text(self):
        return self.page.locator(self.s.header).inner_text()

    @property
    def banner_text(self):
        return self.page.locator(self.s.banner).inner_text()

    @property
    def body_text(self):
        return self.page.locator(self.s.text).inner_text()
