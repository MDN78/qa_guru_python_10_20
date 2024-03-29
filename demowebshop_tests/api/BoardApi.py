import os
import requests
from utils.helper import helper

class BoardApi:

    def add_item_to_card(self):
        url_api = os.getenv('API_URL')
        cookie = helper.get_auth_cookie()
        requests.post(f'{url_api}addproducttocart/catalog/31/1/1', cookies={"NOPCOMMERCE.AUTH": cookie})

    def add_book_to_cart(self):
        url_api = os.getenv('API_URL')
        cookie = helper.get_auth_cookie()
        requests.post(f'{url_api}addproducttocart/catalog/13/1/1', cookies={"NOPCOMMERCE.AUTH": cookie})

# board_api = BoardApi()