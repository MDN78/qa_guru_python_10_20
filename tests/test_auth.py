import time
from demowebshop_tests.application import app
from utils.helper import helper


def test_auth_form():
    app.main_page.check_login_form()
    time.sleep(3)


def test_add_item_to_cart():
    app.board_api.add_item_to_card()
    app.main_page.go_to_cart()
    app.main_page.check_item_in_cart('14.1-inch Laptop')
    helper.clean_cart()
    time.sleep(4)


def test_add_new():
    app.board_api.add_book_to_cart()
    app.main_page.go_to_cart()
    app.main_page.check_item_in_cart('Computing and Internet')
    helper.clean_cart()
    time.sleep(6)
