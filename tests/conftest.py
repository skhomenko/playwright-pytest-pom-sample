from os import environ

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from infrastructure import pages as p

load_dotenv()

HEADLESS = bool(int(environ.get("HEADLESS")))


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = getattr(p, environ.get("BROWSER")).launch(headless=HEADLESS)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def login_page(page):
    heroku_app_login = p.LoginPage(page)
    heroku_app_login.goto("https://the-internet.herokuapp.com/login")
    return heroku_app_login
