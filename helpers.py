import random
import string

def get_random_email():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(7)) + '@test.com'
