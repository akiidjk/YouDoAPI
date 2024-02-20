import random
import string
from locust import HttpUser, task, between


def genera_stringa_casuale(lunghezza, caratteri=string.ascii_letters + string.digits):
    return ''.join(random.choice(caratteri) for _ in range(lunghezza))


class ApiUser(HttpUser):
    """Class that inherits from the HttpUser class from Locust."""
    wait_time = between(1, 5)


