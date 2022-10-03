from selenium.webdriver.common.keys import Keys

from constants.chat import ChatConsts
from pages.base_page import BasePage
from pages.utils import log_decorator


class Chat(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ChatConsts()

    @log_decorator
    def type_message(self, message):
        self.fill_field(xpath=self.constants.TYPE_MESSAGE_XPATH, value=message + Keys.ENTER)

    @log_decorator
    def verify_message(self, message):
        """Verify messages"""
        assert self.get_element_text(self.constants.CHAT_MESSAGES_XPATH) == message
