from password_manager import PasswordManager

def main():
    manager: PasswordManager = PasswordManager(12345)
    print(manager.generate_password_for("fabian.sorn@icloud.com", "github.com"))

if __name__ == "__main__":
    main()