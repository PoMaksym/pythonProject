from constants.header import HeaderConsts
from pages.base_page import BasePage


class ProfileHeader(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConsts()

    def profile_opened_verify(self, username):
        assert self.get_element_text(self.constants.VERIFY_PROFILE_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.constants.VERIFY_PROFILE_XPATH)}"
