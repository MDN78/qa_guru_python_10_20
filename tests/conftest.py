import pytest
import os
from dotenv import load_dotenv
import requests
from selene import browser
from utils.helper import get_auth_cookie


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def auth_driver():
    cookie = get_auth_cookie()
    browser.open("http://demowebshop.tricentis.com")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    browser.open("http://demowebshop.tricentis.com")
    yield browser

    browser.quit()

