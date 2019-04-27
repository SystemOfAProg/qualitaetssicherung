import unittest
from passwordmanager import PasswordManager

# Class that depends on the Password Manager
class PasswordManagerUser():

    def __init__(self):
        pass

    # Try with unexpected params I
    def read_master_from_pw(self, pw_from_manager: str, index: int) -> str:
        return pw_from_manager[index:]
