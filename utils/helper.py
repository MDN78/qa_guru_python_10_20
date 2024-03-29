import os
import requests


def get_auth_cookie():
    url_api = os.getenv('API_URL')
    email = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    response = requests.post(url=url_api + "login",
                             data={"Email": email, "Password": password},
                             allow_redirects=False)
    cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    return cookie
