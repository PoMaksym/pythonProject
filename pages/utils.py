import datetime
import logging
import random
import string
from random import choice
from string import ascii_lowercase
from string import ascii_uppercase
from time import sleep


def random_upper():
    """Generate random string"""
    random_string = (''.join(choice(ascii_uppercase) for i in range(12)))
    return random_string


def random_low():
    """Generate random string"""
    random_string_low = (''.join(choice(ascii_lowercase) for i in range(12)))
    return random_string_low


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=5, period=0.5):
    """Reties until OK"""

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator
