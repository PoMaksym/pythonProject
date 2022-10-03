from constants.header import HeaderConsts
from pages.base_page import BasePage
from pages.chat import Chat
from pages.profile import ProfileHeader
from pages.utils import log_decorator


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConsts()

    def navigate_to_create_post_page(self):
        """Click on create post button"""
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    @log_decorator
    def navigate_to_search_icon(self):
        """Click on search icon"""
        self.click(self.constants.SEARCH_ICON_XPATH)

    @log_decorator
    def search_fill_text(self, placeholder):
        """Fill random text in placeholder"""
        self.fill_field(xpath=self.constants.SEARCH_PLACEHOLDER, value=placeholder)

    @log_decorator
    def verify_unsuccessful_search(self):
        """Verify error when unsuccessful search"""
        assert self.get_element_text(self.constants.SEARCH_UNSUCCESSFUL) == self.constants.SEARCH_UNSUCCESSFUL_TEXT, \
            f"Actual: {self.get_element_text(self.constants.SEARCH_UNSUCCESSFUL)}"

    @log_decorator
    def verify_successful_search(self):
        """Verify error when successful search"""
        assert self.get_element_text(self.constants.SEARCH_SUCCESSFUL_XPATH)

    @log_decorator
    def open_chat(self):
        """Open chat"""
        self.click(self.constants.CHAT_ICON_XPATH)
        return Chat(self.driver)

    @log_decorator
    def open_profile(self):
        """Open profile"""
        self.click(self.constants.PROFILE_ICON_XPATH)
        return ProfileHeader(self.driver)

    @log_decorator
    def profile_opened_verify(self, username):
        assert self.get_element_text(self.constants.VERIFY_PROFILE_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.constants.VERIFY_PROFILE_XPATH)}"
