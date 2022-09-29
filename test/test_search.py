import logging

from pages.utils import random_str


class TestSearch:
    log = logging.getLogger("[create search]")

    def test_unsuccessful_search(self, hello_page):
        """
         - Pre-conditions:
             - Sign Up/Sign In as an user
             - Steps:
                - Navigate to Search Page
                - Type random text
                - Verify the result
        """
        # Navigate to search icon
        hello_page.header.navigate_to_search_icon()

        # Type text
        hello_page.header.search_fill_text(placeholder=random_str(13))

        # Verify the result
        hello_page.header.verify_unsuccessful_search()

    def test_successful_search(self, hello_page):
        """
         - Pre-conditions:
             - Sign Up/Sign In as an user
             - Steps:
                - Navigate to Search icon
                - Type text
                - Verify the result
        """
        # Navigate to search page
        hello_page.header.navigate_to_search_icon()

        # Type text
        hello_page.header.search_fill_text(placeholder='test')

        # Verify the result
        hello_page.header.verify_successful_search()
