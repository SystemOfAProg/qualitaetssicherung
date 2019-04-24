import random

class PasswordManager():

    def __init__(self, secret:int):
        self.secret = secret

    def generate_password_for(self, login: str, service_url: str) -> str:
        random.seed(a=self.secret)
        return str(random.randint(0,1000000)) + "-" + login + "-" + service_url
    