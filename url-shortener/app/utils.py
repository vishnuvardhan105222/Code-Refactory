# TODO: Implement utility functions here
# Consider functions for:
# - Generating short codes
# - Validating URLs
# - Any other helper functions you need

import random
import string
import re

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_valid_url(url):
    regex = re.compile(
        r'^(https?|ftp)://' 
        r'(?:(?:[A-Z0-9-]+\.)+[A-Z]{2,6}|' 
        r'localhost|' 
        r'\d{1,3}(?:\.\d{1,3}){3})' 
        r'(?::\d+)?(?:/?|[/?]\S+)$', 
        re.IGNORECASE)
    return re.match(regex, url) is not None
