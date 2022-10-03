import logging

import pytest


class TestOpenProfile:
    log = logging.getLogger("[Open profile]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    def test_open_profile(self, hello_page, random_user):
        """Open profile page and verify"""
        hello_page.header.open_profile()
        hello_page.header.profile_opened_verify(random_user.username.lower())
