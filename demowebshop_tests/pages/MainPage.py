from selene import browser, have
import os

class MainPage:

    def check_login_form(self):
        browser.element(".account").should(have.text(os.getenv('LOGIN')))

    def go_to_cart(self):
        browser.element('#topcartlink').click()

    def check_item_in_cart(self, item):
        browser.element('.product-name').should(have.text(item))

