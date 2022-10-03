class StartPageConstants:
    # Sign in
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"
    SIGN_IN_LOGIN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_LOGIN_ERROR_TEXT = "Invalid username / pasword"

    # Sign up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    SIGN_UP_EMPTY_USERNAME_XPATH = ".//div[@class='alert alert-danger small liveValidateMessage liveValidateMessage--visible']"
    SIGN_UP_EMPTY_EMAIL_ERROR_XPATH = ".//*/div[contains(text(),'You must provide a valid email address.')]"
    SIGN_UP_EMPTY_PASSWORD_ERROR_XPATH = ".//*/div[contains(text(),'Password must be at least 12 characters.')]"
    SIGN_OUT_BUTTON_XPATH = ".//*/button[contains(text(),'Sign Out')]"
    SIGN_UP_EMPTY_USERNAME_TEXT = "Username must be at least 3 characters."
    SIGN_UP_EMPTY_EMAIL_ERROR_TEXT = "You must provide a valid email address."
    SIGN_UP_EMPTY_PASSWORD_ERROR_TEXT = "Password must be at least 12 characters."
    SIGN_UP_SPACE_USERNAME_ERROR_TEXT = "Username can only contain letters and numbers."
    SIGN_UP_SPACE_USERNAME_ERROR_XPATH = ".//*/div[contains(text(),'Username can only contain letters and numbers.')]"
    SIGN_UP_USED_EMAIL_ERROR_XPATH = './/*/div[contains(text(),"That email is already being used.")]'
    SIGN_UP_USED_EMAIL_ERROR_TEXT = 'That email is already being used.'

    HELLO_MESSAGE_XPATH = ".//h2"
    HELLO_MESSAGE_USERNAME_XPATH = ".//strong"
    HELLO_MESSAGE_TEXT = "Hello {username}, your feed is empty."
