from selene import browser, have
import os

class MainPage:

    def login_form(self):
        browser.element(".account").should(have.text(os.getenv('LOGIN')))



main_mage = MainPage()