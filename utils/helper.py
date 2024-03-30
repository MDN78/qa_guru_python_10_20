import os
import requests
from selene import browser
from allure_commons._allure import step


class Helper:
    def get_auth_cookie(self):
        url_api = os.getenv('API_URL')
        email = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        with step(f'API-POST: USER: {email} URL: {url_api}'):
            response = requests.post(url=url_api + "login",
                                     data={"Email": email, "Password": password},
                                     allow_redirects=False)
        with step('API-GET: get auth cookie'):
            cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        return cookie

    def clean_cart(self):
        with step('UI: clean cart'):
            browser.element('.qty-input').set_value('0')
            browser.element('.button-2.update-cart-button').click()


helper = Helper()
