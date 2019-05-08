import hashlib
from passwordmanager import PasswordManager

# Class with porblematic implementation
class PasswordManagerUser():

    def __init__(self):
        pass

    # Check password manager and create a hash if it is ok
    def hash_password(self, pw_from_manager: str) -> str:
        if not isinstance(pw_from_manager, str):
            raise ValueError("Password is not a string")
        if not len(pw_from_manager) == 16:
            raise ValueError("Password is too short")
        return (hashlib.sha256(('%s' % (pw_from_manager)).encode('utf-8')).hexdigest())
