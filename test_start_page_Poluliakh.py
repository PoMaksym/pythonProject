import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        # Steps
        yield StartPage(driver)
        # Post-conditions
        driver.close()

    def test_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Prepare data
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@gmail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)

        # Verify success message
        start_page.verify_success_sign_up(username_value)
        self.log.info("Hello message was verified")

    def test_sign_in(self, start_page):
        """Pre-conditions:
        - open start page
        Steps:
        - Fill login and password fields
        - Click Sign in
        - Verify registration"""

        start_page.sign_in(username='Aa1234', password="test@test44.com")
        start_page.verify_sign_in(username='Aa1234', password='test@test44.com')

    def test_sign_up_empty_username(self, start_page):
        user = random_str()
        username_value = ""
        email_value = f"{user}{random_num()}@gmail.com"
        password_value = f"{random_str(6)}{random_num()}"
        # Fill fields
        start_page.sign_up(username_value, email_value, password_value)
        # Verify error
        start_page.empty_username_sign_up()

    def test_sign_up_empty_email(self, start_page):
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = ""
        password_value = f"{random_str(6)}{random_num()}"

        # Fill fields
        start_page.sign_up(username_value, email_value, password_value)
        # Verify error
        start_page.empty_email_sign_up()

    def test_sign_up_empty_password(self, start_page):
        user = random_str()
        username_value = f"{user}{random_num()}"
        email_value = f"{user}{random_num()}@gmail.com"
        password_value = ""

        start_page.sign_up(username_value, email_value, password_value)
        start_page.empty_password_sign_up()

    def test_sign_up_space_username(self, start_page):
        user = random_str()
        username_value = "               "
        email_value = f"{user}{random_num()}@gmail.com"
        password_value = f"{random_str(6)}{random_num()}"

        start_page.sign_up(username_value, email_value, password_value)
        start_page.space_username_sign_up()
