import os
from selene import browser, have
from allure_commons._allure import step


class MainPage:

    def check_login_form(self):
        with step('UI: checking authorization'):
            browser.element(".account").should(have.text(os.getenv('LOGIN')))

    def go_to_cart(self):
        with step('UI: go to cart'):
            browser.element('#topcartlink').click()

    def check_item_in_cart(self, item):
        with step(f'UI: checking item {item} in cart'):
            browser.element('.product-name').should(have.text(item))


main_page = MainPage()
