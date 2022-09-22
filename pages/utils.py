import random
import string
from random import choice
from string import ascii_lowercase
from string import ascii_uppercase


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
