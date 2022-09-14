from random import choice
from string import ascii_uppercase
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def random():
    random_username = (''.join(choice(ascii_uppercase) for i in range(12)))
    return random_username


def random_email():
    random_email = (''.join(choice(ascii_uppercase) for i in range(12))) + "@gmail.com"
    return random_email


class TestStartPage:

    def test_sign_up_successful(self):
        # Create driver
        driver = webdriver.Chrome(r"C:\Users\HomeWork\PycharmProjects\pythonProject\chromedriver.exe")

        # Open page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        sleep(1)

        username = driver.find_element(by=By.XPATH, value='.//*[@id="username-register"]')
        print(username.send_keys())
        username.send_keys(random())
        sleep(1)

        email = driver.find_element(by=By.XPATH, value='.//*[@id="email-register"]')
        email.send_keys(random_email())
        sleep(1)

        password = driver.find_element(by=By.XPATH, value='.//*[@id="password-register"]')
        password.send_keys('Testfr7777test')
        sleep(1)

        button = driver.find_element(by=By.XPATH, value='.//*[@type="submit"]')
        button.click()
        sleep(1)

        # Verify sign up successful
        verify_element = driver.find_element(by=By.XPATH, value='.//*/button[contains(text(),"Sign Out")]')
        assert verify_element.text == "Sign Out"

        # Close driver
        driver.close()

    def test_empty_username(self):
        driver = webdriver.Chrome(r"C:\Users\HomeWork\PycharmProjects\pythonProject\chromedriver.exe")

        # Open page
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        sleep(1)

        username = driver.find_element(by=By.XPATH, value='.//*[@id="username-register"]')
        username.send_keys('')
        sleep(1)

        email = driver.find_element(by=By.XPATH, value='.//*[@id="email-register"]')
        email.send_keys(random_email())
        sleep(1)

        password = driver.find_element(by=By.XPATH, value='.//*[@id="password-register"]')
        password.send_keys('Testfr7777test')
        sleep(1)

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
        username.send_keys(random())
        sleep(1)

        email = driver.find_element(by=By.XPATH, value='.//*[@id="email-register"]')
        email.send_keys('')
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
