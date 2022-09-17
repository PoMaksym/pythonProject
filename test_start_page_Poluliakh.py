from random import choice
from string import ascii_uppercase
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def random():
    random_string = (''.join(choice(ascii_uppercase) for i in range(12)))
    return random_string


class TestStartPage:

    def test_sign_up_successful(self):
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\HomeWork\PycharmProjects\pythonProject\chromedriver.exe")

        # Open page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        sleep(1)

        # Fill username
        user = random()
        username = driver.find_element(by=By.XPATH, value='.//*[@id="username-register"]')
        username.clear()
        username.send_keys(user)
        sleep(1)

        # Fill email
        email = driver.find_element(by=By.XPATH, value='.//*[@id="email-register"]')
        email.clear()
        email.send_keys(f"{random()}@gmail.com")
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value='.//*[@id="password-register"]')
        password.clear()
        password.send_keys('Testfr7777test')
        sleep(1)

        button = driver.find_element(by=By.XPATH, value='.//*[@type="submit"]')
        button.click()
        sleep(1)

        # Verify sign up successful
        verify_element = driver.find_element(by=By.XPATH, value='.//*/button[contains(text(),"Sign Out")]')
        assert verify_element.text == "Sign Out"
        assert driver.find_element(by=By.XPATH, value=".//strong").text == user.lower()


        # Close driver
        driver.close()

    def test_empty_username(self):
        driver = webdriver.Chrome(r"C:\Users\HomeWork\PycharmProjects\pythonProject\chromedriver.exe")

        # Open page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        sleep(1)

        # Leave usernames field clear
        username = driver.find_element(by=By.XPATH, value='.//*[@id="username-register"]')
        username.clear()
        sleep(1)

        # Fill email
        email = driver.find_element(by=By.XPATH, value='.//*[@id="email-register"]')
        email.clear()
        email.send_keys(f"{random()}@gmail.com")
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value='.//*[@id="password-register"]')
        password.clear()
        password.send_keys('Testfr7777test')
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value='.//*[@type="submit"]')
        button.click()
        sleep(1)

        # Verify sign up successful
        verify_element = driver.find_element(by=By.XPATH,
                                             value='.//*/div[contains(text(),"Username must be at least 3 characters")]')
        assert verify_element.text == "Username must be at least 3 characters."

        driver.close()

    def test_empty_email(self):
        driver = webdriver.Chrome(r"C:\Users\HomeWork\PycharmProjects\pythonProject\chromedriver.exe")

        # Open page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        sleep(1)

        username = driver.find_element(by=By.XPATH, value='.//*[@id="username-register"]')
        username.clear()
        username.send_keys(random())
        sleep(1)

        email = driver.find_element(by=By.XPATH, value='.//*[@id="email-register"]')
        email.clear()
        sleep(1)

        password = driver.find_element(by=By.XPATH, value='.//*[@id="password-register"]')
        password.send_keys('Testfr7777test')
        sleep(1)

        button = driver.find_element(by=By.XPATH, value='.//*[@type="submit"]')
        button.click()
        sleep(1)

        # Verify sign up successful
        verify_element = driver.find_element(by=By.XPATH,
                                             value='.//*/div[contains(text(),"You must provide a valid email address.")]')
        assert verify_element.text == "You must provide a valid email address."

        driver.close()

    def test_empty_password(self):
        driver = webdriver.Chrome(r"C:\Users\HomeWork\PycharmProjects\pythonProject\chromedriver.exe")

        # Open page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        sleep(1)

        username = driver.find_element(by=By.XPATH, value='.//*[@id="username-register"]')
        username.clear()
        username.send_keys(random())
        sleep(1)

        email = driver.find_element(by=By.XPATH, value='.//*[@id="email-register"]')
        email.clear()
        email.send_keys(f"{random()}@gmail.com")
        sleep(1)

        password = driver.find_element(by=By.XPATH, value='.//*[@id="password-register"]')
        password.clear()
        sleep(1)

        button = driver.find_element(by=By.XPATH, value='.//*[@type="submit"]')
        button.click()
        sleep(1)

        # Verify sign up successful
        verify_element = driver.find_element(by=By.XPATH,
                                             value='.//*/div[contains(text(),"Password must be at least 12 characters.")]')
        assert verify_element.text == "Password must be at least 12 characters."

        driver.close()

    def test_signin_successful(self):
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\HomeWork\PycharmProjects\pythonProject\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Fill login
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        login.send_keys("MaxP")
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("Test7777test")
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify sign in
        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        assert hello_message.text == f"Hello {'MaxP'.lower()}, your feed is empty."

        # Close driver
        driver.close()

    def test_signin_empty(self):
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\HomeWork\PycharmProjects\pythonProject\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Empty login
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        sleep(1)

        # Empty password
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"
