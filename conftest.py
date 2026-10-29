import pytest
import requests

from pages.login_page import LoginPage

UI_BASE_URL = "https://www.saucedemo.com"
API_BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def login_page(page):
    """Open the SauceDemo login page and return its page object."""
    lp = LoginPage(page)
    lp.open(UI_BASE_URL)
    return lp


@pytest.fixture
def logged_in_inventory(login_page):
    """Log in as a valid user and return the inventory page."""
    return login_page.login("standard_user", "secret_sauce")


@pytest.fixture(scope="session")
def api_base_url():
    return API_BASE_URL


@pytest.fixture(scope="session")
def auth_token(api_base_url):
    """Get an auth token for Restful-Booker (needed for PUT / DELETE)."""
    resp = requests.post(
        f"{api_base_url}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=30,
    )
    assert resp.status_code == 200
    return resp.json()["token"]


@pytest.fixture
def booking_payload():
    return {
        "firstname": "Ashly",
        "lastname": "Shaji",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def created_booking(api_base_url, booking_payload):
    """Create a booking before the test, delete it after (setup + teardown)."""
    resp = requests.post(f"{api_base_url}/booking", json=booking_payload, timeout=30)
    assert resp.status_code == 200
    booking_id = resp.json()["bookingid"]
    yield booking_id
    # teardown: try to clean up (ignore if already deleted by the test)
    token = requests.post(
        f"{api_base_url}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=30,
    ).json()["token"]
    requests.delete(
        f"{api_base_url}/booking/{booking_id}",
        headers={"Cookie": f"token={token}"},
        timeout=30,
    )
