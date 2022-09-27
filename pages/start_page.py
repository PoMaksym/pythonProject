
from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.utils import wait_until_ok


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()


    def sign_in(self, username, password):
        """Sign in as the user"""
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)

        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    def verify_sign_in(self, username, password):
        """Verify Sign in successful"""
        username = username.lower()
        assert self.get_element_text(self.constants.HELLO_MESSAGE_XPATH) == self.constants.HELLO_MESSAGE_TEXT.format(
            username=username), \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_XPATH)}"

        assert self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH)}"

    def verify_sign_in_error(self):
        """Verify invalid Sign In error"""
        assert not self.get_element_text(
            self.constants.SIGN_IN_LOGIN_ERROR_XPATH) == self.constants.SIGN_IN_LOGIN_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_XPATH)}"

    def sign_up(self, username, email, password):
        """Sign up as the user"""
        # Fill username
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)

        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def sign_up_and_verify(self, username, email, password, Verify=True):
        """Sign up as the user"""
        # Fill username
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        # Click button
        self.click_sign_up_and_verify()
        # Return new page
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    @wait_until_ok(period=0.5)
    def click_sign_up_and_verify(self):
        """Click sign up and verify"""
        # Click button
        self.click(self.constants.SIGN_UP_BUTTON_XPATH)
        assert not self.is_exists(self.constants.SIGN_UP_BUTTON_XPATH)

    def verify_success_sign_up(self, username):
        """Verify success Sign Up using hello message"""
        username = username.lower()
        assert self.get_element_text(self.constants.HELLO_MESSAGE_XPATH) == self.constants.HELLO_MESSAGE_TEXT.format(
            username=username)
        assert not self.is_exists(self.constants.SIGN_UP_BUTTON_XPATH)
        assert self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH)}"

    def empty_username_sign_up(self):
        """Verify error with empty username"""
        assert self.get_element_text(
            self.constants.SIGN_UP_EMPTY_USERNAME_XPATH) == self.constants.SIGN_UP_EMPTY_USERNAME_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_UP_EMPTY_USERNAME_XPATH)}"

    def empty_email_sign_up(self):
        """Verify error with empty email"""
        assert self.get_element_text(
            self.constants.SIGN_UP_EMPTY_EMAIL_ERROR_XPATH) == self.constants.SIGN_UP_EMPTY_EMAIL_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_UP_EMPTY_EMAIL_ERROR_XPATH)}"

    def empty_password_sign_up(self):
        """Verify error with empty password"""
        assert self.get_element_text(
            self.constants.SIGN_UP_EMPTY_PASSWORD_ERROR_XPATH) == self.constants.SIGN_UP_EMPTY_PASSWORD_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_UP_EMPTY_PASSWORD_ERROR_XPATH)}"

    def space_username_sign_up(self):
        """Verify error with spaces in username"""
        assert self.get_element_text(
            self.constants.SIGN_UP_SPACE_USERNAME_ERROR_XPATH) == self.constants.SIGN_UP_SPACE_USERNAME_ERROR_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_UP_EMPTY_PASSWORD_ERROR_XPATH)}"
