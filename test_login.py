import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Login")
@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login(login_page):
    inventory = login_page.login("standard_user", "secret_sauce")
    expect(inventory.title).to_have_text("Products")
    assert inventory.items.count() == 6


# Data-driven negative tests
@allure.feature("Login")
@pytest.mark.ui
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_invalid_login(login_page, username, password, expected_error):
    login_page.login(username, password)
    expect(login_page.error_message).to_be_visible()
    assert expected_error in login_page.get_error_text()
