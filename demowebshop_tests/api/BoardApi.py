import os
import requests
from utils.helper import helper
from allure_commons._allure import step
from utils.logger import *


class BoardApi:

    def add_item_to_card(self):
        url_api = os.getenv('API_URL')
        cookie = helper.get_auth_cookie()
        with step('API-POST: add item to cart'):
            post_request_logger(f'{url_api}addproducttocart/catalog/31/1/1', cookies={"NOPCOMMERCE.AUTH": cookie})

    def add_book_to_cart(self):
        url_api = os.getenv('API_URL')
        cookie = helper.get_auth_cookie()
        with step('API-POST: add item to cart'):
            post_request_logger(f'{url_api}addproducttocart/catalog/13/1/1', cookies={"NOPCOMMERCE.AUTH": cookie})

board_api = BoardApi()
