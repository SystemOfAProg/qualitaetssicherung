import hashlib
from passwordmanager import PasswordManager

# Class with porblematic implementation
class PasswordManagerUser():

    def __init__(self):
        pass

    # Try with unexpected params I
    def hash_password(self, pw_from_manager: str) -> str:
        print(pw_from_manager)
        if not isinstance(pw_from_manager, str):
            raise ValueError("Password is not a string")
        if not len(pw_from_manager) == 16:
            raise ValueError("Password is too short")
        return (hashlib.sha256(('%s' % (pw_from_manager)).encode('utf-8')).hexdigest())
