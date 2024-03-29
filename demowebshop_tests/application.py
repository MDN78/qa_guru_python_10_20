from demowebshop_tests.pages.MainPage import MainPage
from demowebshop_tests.api.BoardApi import BoardApi
from utils.helper import Helper

class ApplicationManager:
    def __init__(self):
        self.main_page = MainPage()
        self.board_api = BoardApi()

app = ApplicationManager()
