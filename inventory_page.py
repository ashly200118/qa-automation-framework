from playwright.sync_api import Page


class InventoryPage:
    """Page Object for the products page."""

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_link .shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_to_cart(self, product_slug: str):
        # e.g. product_slug = "sauce-labs-backpack"
        self.page.locator(f"#add-to-cart-{product_slug}").click()

    def get_cart_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def open_cart(self):
        from pages.cart_page import CartPage

        self.cart_link.click()
        return CartPage(self.page)
