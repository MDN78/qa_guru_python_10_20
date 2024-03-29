import time
from demowebshop_tests.pages.main_page import main_mage



def test_auth_form():
    main_mage.login_form()
    time.sleep(3)
