import pytest
from allure_commons._allure import step
from dotenv import load_dotenv

from selene import browser
from utils.helper import helper


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def auth_driver():
    with step('UI: authorization user'):
        cookie = helper.get_auth_cookie()
        browser.open("http://demowebshop.tricentis.com")
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    browser.open("http://demowebshop.tricentis.com")
    yield browser

    with step('UI: close driver'):
        browser.quit()
