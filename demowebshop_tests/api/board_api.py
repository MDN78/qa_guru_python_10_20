import os
from utils.helper import helper
from allure_commons._allure import step
from utils.logger import post_request_logger


class BoardApi:

    def add_item_to_card(self, item):
        url_api = os.getenv('API_URL')
        cookie = helper.get_auth_cookie()
        with step(f'API-POST: add item: {item} to cart'):
            post_request_logger(f'{url_api}addproducttocart/catalog/{item}', cookies={"NOPCOMMERCE.AUTH": cookie})


board_api = BoardApi()
