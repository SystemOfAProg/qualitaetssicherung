import random, string

class PasswordManager():

    def __init__(self, master_password: str, password_length:int=16):
        self.master_password = master_password
        self.password_length = password_length

    def generate_password_for(self, login: str, service_name: str) -> str:
        master_binary: str = ''.join(format(ord(x), 'b') for x in self.master_password)
        master_int: int = int(master_binary, 2)
        password: str = ''
        for i in range(0, self.password_length + 1):
            password += self.__next_character(login + service_name, i, master_binary, master_int)
        return password[1:]

    def __next_character(self, lsn:str, i:int, mb:str, mi:int) -> str: 
        possible_characters: str = string.ascii_letters + string.digits
        random.seed(len(mb) * mi + i)
        return possible_characters[random.randint(0,len(possible_characters) - 1)]
    