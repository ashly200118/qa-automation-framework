from playwright.sync_api import Page


class CartPage:
    """Page Object for the shopping cart."""

    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("#checkout")

    def get_item_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def start_checkout(self):
        from pages.checkout_page import CheckoutPage

        self.checkout_button.click()
        return CheckoutPage(self.page)
