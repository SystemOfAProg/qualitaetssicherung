import random, string

class PasswordManager():

    def __init__(self, master_password: str, password_length: int = 16):
        if not isinstance(master_password, str) or not isinstance(password_length, int):
            raise TypeError("The passed parameters have the wrong type.")
        elif len(master_password) <= 0 or password_length < 16:
            raise ValueError("Master Password or Password length are too short")
        master_password = master_password.strip()
        self.__master_password = master_password
        self.__password_length = password_length

    def get_password_length(self):
        return self.__password_length

    def generate_password_for(self, login: str, service_name: str) -> str:
        if not isinstance(login, str) or not isinstance(service_name, str):
            raise TypeError("A password cannot be created from the given parameters, because they have the wrong type.")
        elif len(login) <= 0 or len(service_name) <= 0:
            raise ValueError("A password cannot be created from the given parameters, because they are to short.")
        login = login.strip()
        service_name = service_name.strip()
        master_binary: str = ''.join(format(ord(x), 'b') for x in self.__master_password)
        master_int: int = int(master_binary, 2)
        password: str = ''
        for i in range(0, self.__password_length + 1):
            password += self.__next_character(login + service_name, i, master_binary, master_int)
        return password[1:] + self.__master_password

    def __next_character(self, lsn: str, i: int, mb: str, mi: int) -> str:
        possible_characters: str = string.ascii_letters + string.digits
        random.seed(len(mb) * mi + i)
        return possible_characters[random.randint(0,len(possible_characters) - 1)]
