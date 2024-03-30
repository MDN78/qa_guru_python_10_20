import time
from utils.helper import helper
from demowebshop_tests.api.BoardApi import board_api
from demowebshop_tests.pages.MainPage import main_page


def test_auth_form():
    main_page.check_login_form()


def test_add_item_to_cart():
    board_api.add_item_to_card()
    main_page.go_to_cart()
    main_page.check_item_in_cart('14.1-inch Laptop')
    helper.clean_cart()


def test_add_new():
    board_api.add_book_to_cart()
    main_page.go_to_cart()
    main_page.check_item_in_cart('Computing and Internet')
    helper.clean_cart()
