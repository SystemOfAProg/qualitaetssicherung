import unittest
from passwordmanager import PasswordManager
from passwordmanager_user import PasswordManagerUser

class PasswordManagerUserTest(unittest.TestCase):
 
    _master_password = "MySecretPassword"

    # Try with unexpected params I
    def test_read_master_from_password(self):
        manager = PasswordManager("Master")
        user = PasswordManagerUser()
        password = manager.generate_password_for("fabian", "circleci")['password']
        self.assertEqual(user.hash_password(password), user.hash_password(password))


if __name__ == '__main__':
    unittest.main()