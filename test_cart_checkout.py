import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Cart")
@pytest.mark.ui
def test_add_item_to_cart(logged_in_inventory):
    logged_in_inventory.add_to_cart("sauce-labs-backpack")
    assert logged_in_inventory.get_cart_count() == 1

    cart = logged_in_inventory.open_cart()
    assert cart.get_item_names() == ["Sauce Labs Backpack"]


@allure.feature("Cart")
@pytest.mark.ui
def test_add_multiple_items(logged_in_inventory):
    logged_in_inventory.add_to_cart("sauce-labs-backpack")
    logged_in_inventory.add_to_cart("sauce-labs-bike-light")
    assert logged_in_inventory.get_cart_count() == 2


@allure.feature("Checkout")
@pytest.mark.ui
@pytest.mark.smoke
def test_complete_checkout(logged_in_inventory):
    logged_in_inventory.add_to_cart("sauce-labs-backpack")
    cart = logged_in_inventory.open_cart()
    checkout = cart.start_checkout()
    checkout.fill_details("Ashly", "Shaji", "682001")
    checkout.finish_order()
    expect(checkout.confirmation_header).to_have_text("Thank you for your order!")


@allure.feature("Checkout")
@pytest.mark.ui
def test_checkout_without_details_shows_error(logged_in_inventory):
    logged_in_inventory.add_to_cart("sauce-labs-backpack")
    checkout = logged_in_inventory.open_cart().start_checkout()
    checkout.continue_button.click()
    expect(checkout.error_message).to_contain_text("First Name is required")
