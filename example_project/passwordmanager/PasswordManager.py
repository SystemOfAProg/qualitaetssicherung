import random, string
import hashlib

# Generate passwords out of a master-password, a login- and a service-name
class PasswordManager():

    def __init__(self, master_password: str):
        if not isinstance(master_password, str):
            raise TypeError("The passed parameters have the wrong type.")
        elif len(master_password) <= 0:
            raise ValueError("Master Password are too short")
        master_password = master_password.strip()
        self.__master_password = master_password
        self.__password_length = 18

    def get_password_length(self):
        return self.__password_length

    def generate_password_for(self, login: str, service_name: str) -> str:
        if not isinstance(login, str) or not isinstance(service_name, str):
            raise TypeError("A password cannot be created from the given parameters, because they have the wrong type.")
        elif len(login) <= 0 or len(service_name) <= 0:
            raise ValueError("A password cannot be created from the given parameters, because they are to short.")
        login = login.strip()
        service_name = service_name.strip()
        master_hash = hashlib.sha256(('%s' % (self.__master_password)).encode('utf-8')).hexdigest()
        password: str = ''
        for i in range(0, self.__password_length + 1):
            password += self.__next_character(login + service_name, i, master_hash)
        return {
            'login': login,
            'service': service_name,
            'password': password[1:]
        }

    def __next_character(self, lsn: str, i: int, mh: str) -> str:
        possible_characters: str = string.ascii_letters + string.digits
        random.seed(len(lsn) + len(mh) * i)
        return possible_characters[random.randint(0,len(possible_characters) - 1)]
