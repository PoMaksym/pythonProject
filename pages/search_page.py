from constants.search import SearchConsts
from pages.base_page import BasePage
from pages.header import Header


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = SearchConsts()
        self.header = Header(self.driver)

    def search_text(self, placeholder):
        """Fill random text in placeholder"""
        self.fill_field(xpath=self.constants.SEARCH_PLACEHOLDER, value=placeholder)

    def verify_unsuccessful_search(self):
        """Verify error when unsuccessful search"""
        assert self.get_element_text(self.constants.SEARCH_UNSUCCESSFUL) == self.constants.SEARCH_UNSUCCESSFUL_TEXT, \
            f"Actual: {self.get_element_text(self.constants.SEARCH_UNSUCCESSFUL)}"
