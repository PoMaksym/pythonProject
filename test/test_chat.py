import pytest

from pages.utils import random_str


class TestChat:

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    def test_open_chat(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as an user
        - Steps:
            - Open chat
            - Send message
            - Verify message
        """
        # Open chat
        chat = hello_page.header.open_chat()
        # Send message
        message = random_str(15)
        chat.type_message(message)
        # Verify message
        chat.verify_message(message)
