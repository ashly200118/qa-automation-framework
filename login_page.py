from playwright.sync_api import Page

from pages.inventory_page import InventoryPage


class LoginPage:
    """Page Object for the SauceDemo login page."""

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def open(self, base_url: str):
        self.page.goto(base_url)

    def login(self, username: str, password: str) -> InventoryPage:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return InventoryPage(self.page)

    def get_error_text(self) -> str:
        return self.error_message.inner_text()
