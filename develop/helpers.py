import random
import string

BASE_URL = "https://qa-desk.education-services.ru/"


def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return f"{username}@test.ru"