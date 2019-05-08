from passwordmanager.PasswordManager import PasswordManager
from passwordmanager_user.PasswordManagerUser import PasswordManagerUser

def main():
    print("Create a password")
    master_password: str = input("Your Master Password:         ")
    login: str =           input("Your login (email/username):  ")
    service: str =         input("The service:                  ")
    manager: PasswordManager = PasswordManager(master_password)
    user: PasswordManagerUser = PasswordManagerUser()
    password: str = manager.generate_password_for(login, service)
    print("Your Password is:             " + password['password'])
    hash = user.hash_password(password['password'])
    print("Hash of Password is:          " + hash)

if __name__ == "__main__":
    main()