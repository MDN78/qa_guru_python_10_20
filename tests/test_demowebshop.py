import os
from utils.helper import helper
from demowebshop_tests.api.BoardApi import board_api
from demowebshop_tests.pages.MainPage import main_page


def test_auth_form():
    main_page.check_login_form()


def test_add_notebook_to_cart():
    item = os.getenv('NOTEBOOK_API')
    item_in_cart = os.getenv('NOTEBOOK_NAME')
    board_api.add_item_to_card(item)
    main_page.go_to_cart()
    main_page.check_item_in_cart(item_in_cart)
    helper.clean_cart()


def test_add_book_to_cart():
    item = os.getenv('BOOK_API')
    item_in_cart = os.getenv('BOOK_NAME')
    board_api.add_item_to_card(item)
    main_page.go_to_cart()
    main_page.check_item_in_cart(item_in_cart)
    helper.clean_cart()
