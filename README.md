# QA Automation Framework (UI + API)

Practice automation framework built to learn test automation with Python.

## Tech stack
Python, Playwright, Pytest, Requests, Allure Reports, GitHub Actions

## What it covers
- **UI tests** on [SauceDemo](https://www.saucedemo.com): login (valid + invalid, data-driven), add to cart, checkout
- **API tests** on [Restful-Booker](https://restful-booker.herokuapp.com): create, read, update, delete bookings + negative cases
- **Page Object Model**: locators and actions live in `pages/`, tests stay clean
- **Pytest fixtures** for setup/teardown (`conftest.py`)
- **CI**: GitHub Actions runs the suite on every push and publishes an Allure report

## Project structure
```
pages/            Page Object classes
tests/ui/         UI tests
tests/api/        API tests
conftest.py       Shared fixtures
pytest.ini        Pytest config and markers
.github/workflows CI pipeline
```

## Run locally
```bash
python -m venv venv
venv\Scripts\activate        # Windows  (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
playwright install chromium

pytest --browser chromium                 # all tests
pytest -m api                             # only API tests
pytest -m smoke --browser chromium        # only smoke tests
pytest --browser chromium --headed        # watch the browser
```

## View the Allure report
```bash
allure serve allure-results
```
(Requires the Allure command-line tool.)
