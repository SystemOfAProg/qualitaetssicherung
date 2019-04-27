import unittest
from passwordmanager import PasswordManager

class PasswordManagerTest(unittest.TestCase):
 
    _master_password = "MySecretPassword"

    # Try with unexpected params I
    def test_bad_params_one(self):
        self.assertRaises(ValueError, lambda: PasswordManager(""))
        self.assertRaises(TypeError, lambda: PasswordManager(12345))

    # Try with unexpected params II
    def test_bad_params_two(self):
        manager = PasswordManager(self._master_password)
        self.assertRaises(ValueError, lambda: manager.generate_password_for("", "github"))
        self.assertRaises(ValueError, lambda: manager.generate_password_for("fabian", ""))
        self.assertRaises(TypeError, lambda: manager.generate_password_for(5, "github"))
        self.assertRaises(TypeError, lambda: manager.generate_password_for("fabian", 5))

    def test_password(self):
        manager = PasswordManager(self._master_password)
        self.assertEqual(manager.generate_password_for("fabian", "github"), manager.generate_password_for("fabian", "github"))



if __name__ == '__main__':
    unittest.main()