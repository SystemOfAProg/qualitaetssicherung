from passwordmanager.PasswordManager import PasswordManager
from passwordmanager_user.PasswordManagerUser import PasswordManagerUser

def main():
    print("Create a password")
    master_password: str = input("Your Master Password:")
    login: str = input("Your login (email/username):")
    service: str = input("The service:")
    manager: PasswordManager = PasswordManager(master_password)
    manager_user: PasswordManagerUser = PasswordManagerUser()
    password: str = manager.generate_password_for(login, service)
    print("Your Password is: " + password)
    master_password: str = manager_user.read_master_from_pw(password, manager.get_password_length())
    print("Master Password read from password: " + master_password)

if __name__ == "__main__":
    main()