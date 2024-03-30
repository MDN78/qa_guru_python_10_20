import pytest
from allure_commons._allure import step

from selene import browser
from utils.helper import helper


@pytest.fixture(scope="function", autouse=True)
def auth_driver():
    with step('UI: get authorization cookie'):
        cookie = helper.get_auth_cookie()
    with step('UI: driver config'):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open("http://demowebshop.tricentis.com")
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})

    browser.open("http://demowebshop.tricentis.com")
    yield browser

    with step('UI: close driver'):
        browser.quit()
