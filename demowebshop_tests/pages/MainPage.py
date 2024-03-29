from selene import browser, have
import os

class MainPage:

    def login_form(self):
        browser.element(".account").should(have.text(os.getenv('LOGIN')))

    def go_to_cart(self):
        browser.element('#topcartlink').click()

    def check_item_in_cart(self):
        browser.element('.product-name').should(have.text('14.1-inch Laptop'))

main_mage = MainPage()