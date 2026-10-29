import allure
import pytest
import requests


@allure.feature("Booking API")
@pytest.mark.api
@pytest.mark.smoke
def test_get_all_bookings(api_base_url):
    resp = requests.get(f"{api_base_url}/booking", timeout=30)
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert "bookingid" in resp.json()[0]


@allure.feature("Booking API")
@pytest.mark.api
def test_create_booking(api_base_url, booking_payload):
    resp = requests.post(f"{api_base_url}/booking", json=booking_payload, timeout=30)
    assert resp.status_code == 200
    body = resp.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == booking_payload["firstname"]
    assert body["booking"]["totalprice"] == booking_payload["totalprice"]


@allure.feature("Booking API")
@pytest.mark.api
def test_get_booking_by_id(api_base_url, created_booking, booking_payload):
    resp = requests.get(f"{api_base_url}/booking/{created_booking}", timeout=30)
    assert resp.status_code == 200
    assert resp.json()["lastname"] == booking_payload["lastname"]


@allure.feature("Booking API")
@pytest.mark.api
def test_update_booking(api_base_url, created_booking, booking_payload, auth_token):
    booking_payload["firstname"] = "Updated"
    resp = requests.put(
        f"{api_base_url}/booking/{created_booking}",
        json=booking_payload,
        headers={"Cookie": f"token={auth_token}"},
        timeout=30,
    )
    assert resp.status_code == 200
    assert resp.json()["firstname"] == "Updated"


@allure.feature("Booking API")
@pytest.mark.api
def test_delete_booking(api_base_url, created_booking, auth_token):
    resp = requests.delete(
        f"{api_base_url}/booking/{created_booking}",
        headers={"Cookie": f"token={auth_token}"},
        timeout=30,
    )
    assert resp.status_code == 201  # Restful-Booker returns 201 for delete

    # confirm it is really gone
    check = requests.get(f"{api_base_url}/booking/{created_booking}", timeout=30)
    assert check.status_code == 404


# ---------- Negative cases ----------
@allure.feature("Booking API - Negative")
@pytest.mark.api
def test_get_nonexistent_booking(api_base_url):
    resp = requests.get(f"{api_base_url}/booking/99999999", timeout=30)
    assert resp.status_code == 404


@allure.feature("Booking API - Negative")
@pytest.mark.api
def test_update_without_token(api_base_url, created_booking, booking_payload):
    resp = requests.put(
        f"{api_base_url}/booking/{created_booking}", json=booking_payload, timeout=30
    )
    assert resp.status_code == 403


@allure.feature("Booking API - Negative")
@pytest.mark.api
def test_create_booking_missing_fields(api_base_url):
    resp = requests.post(f"{api_base_url}/booking", json={"firstname": "Only"}, timeout=30)
    assert resp.status_code in (400, 500)
