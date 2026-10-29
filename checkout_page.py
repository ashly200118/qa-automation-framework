from playwright.sync_api import Page


class CheckoutPage:
    """Page Object for the checkout steps."""

    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.error_message = page.locator("[data-test='error']")
        self.confirmation_header = page.locator(".complete-header")

    def fill_details(self, first: str, last: str, postal: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()
