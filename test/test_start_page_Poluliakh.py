import logging


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    def test_register(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Sign Up and Verify as a user
        start_page.sign_up_and_verify(random_user)

    def test_sign_in(self, start_page, sign_in_user_fix):
        """Pre-conditions:
        - open start page
        Steps:
        - Fill login and password fields
        - Click Sign in
        - Verify registration"""
        user = sign_in_user_fix
        start_page.sign_in(user)
        start_page.verify_sign_in(username=user.username, password=user.password)

    def test_sign_up_empty_username(self, start_page, random_user):
        user = random_user
        user.username = ""
        start_page.sign_up(user)
        start_page.empty_username_sign_up()

    def test_sign_up_empty_email(self, start_page, random_user):
        user = random_user
        user.email = ""
        start_page.sign_up(user)
        start_page.empty_email_sign_up()

    def test_sign_up_empty_password(self, start_page, random_user):
        user = random_user
        user.password = ""
        start_page.sign_up(user)
        start_page.empty_password_sign_up()

    def test_sign_up_space_username(self, start_page, random_user):
        user = random_user
        user.username = "                  "
        start_page.sign_up(user)
        start_page.space_username_sign_up()
