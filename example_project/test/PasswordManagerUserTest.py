import unittest
from passwordmanager import PasswordManager
from passwordmanager_user import PasswordManagerUser

class PasswordManagerTest2(unittest.TestCase):
 
    _master_password = "MySecretPassword"

    # Try with unexpected params I
    def test_bad_params_one(self):
        manager = PasswordManager("Master", 16)
        user = PasswordManagerUser()
        read_master = user.read_master_from_pw(manager.generate_password_for("fabian", "github"),
                                               manager.get_password_length())
        self.assertEqual(read_master, "Master")


if __name__ == '__main__':
    unittest.main()