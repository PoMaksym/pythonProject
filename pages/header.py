from constants.header import HeaderConsts
from pages.base_page import BasePage


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConsts()

    def navigate_to_create_post_page(self):
        """Click on create post button"""
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    def navigate_to_search_page(self):
        """Click on search icon"""
        self.click(self.constants.SEARCH_ICON_XPATH)
        from pages.search_page import SearchPage
        return SearchPage(self.driver)
