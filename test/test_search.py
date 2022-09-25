import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.utils import random_str, random_num


class TestSearch:
    log = logging.getLogger("[create search]")

    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        from pages.start_page import StartPage
        yield StartPage(driver)
        # Post-conditions
        driver.close()

    @pytest.fixture()
    def hello_page(self, start_page):
        """Sign Up as the user and return the page"""
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        return start_page.sign_up_and_verify(username_value, email_value, password_value)

    def test_unsuccessful_search(self, hello_page):
        """
         - Pre-conditions:
             - Sign Up/Sign In as an user
             - Steps:
                - Navigate to Search Page
                - Type random text
                - Verify the result
        """
        # Navigatte to search page
        search = hello_page.header.navigate_to_search_page()
        self.log.info("Moved to Search page")

        # Type text
        search.search_text(placeholder=random_str(13))
        self.log.info("Typing text")

        # Verify the result
        search.verify_unsuccessful_search()
        self.log.info("Message was verified")

    def test_successful_search(self, hello_page):
        """
         - Pre-conditions:
             - Sign Up/Sign In as an user
             - Steps:
                - Navigate to Search Page
                - Type text
                - Verify the result
        """
        # Navigatte to search page
        search = hello_page.header.navigate_to_search_page()
        self.log.info("Moved to Search page")

        # Type text
        search.search_text(placeholder='test')
        self.log.info("Typing text")

        # Verify the result
        search.verify_successful_search()
        self.log.info("Message was verified")
