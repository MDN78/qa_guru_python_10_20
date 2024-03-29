import time
from demowebshop_tests.pages.MainPage import main_mage
from demowebshop_tests.api.BoardApi import board_api
from selene import browser

def test_auth_form():
    main_mage.login_form()
    time.sleep(3)

def test_add_item_to_cart():
    board_api.add_item_to_card()
    main_mage.go_to_cart()
    main_mage.check_item_in_cart()

    time.sleep(4)