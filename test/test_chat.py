from time import sleep

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


class TestChat:
    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield StartPage(driver)
        # Post-conditions
        driver.close()

    @pytest.fixture()
    def hello_page(self, start_page):
        """Sign Up as the user and return the page"""
        user = User()
        user.fill_data()
        return start_page.sign_up_and_verify(user)

    def test_open_chat(self, hello_page):
        hello_page.header.open_chat()

        hello_page.header.type_message(value='test123')
        sleep(5)

        hello_page.header.verify_message()
