from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is your master password? ")
key = load_key() 
fer = Fernet(key)

def view_passwords():
    with open("passwords.txt", "r") as f:
        for line in  f.readlines():
            data = line.strip()
            name, pwd = data.split("|")
            print(f"Account: {name}, Password: {fer.decrypt(pwd.encode()).decode()}")

def add_password():
    name = input("Account name: ")
    pwd = input ("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")
    print(f"Password for {name} added successfully.")

while True:
    mode = input("Would you like to add a new password or view an existing ones? (Type 'add' or 'view'), press 'q' to quit: ").lower()
    if mode == "q":
        print("Exiting the password manager. Goodbye!")
        break

    if mode == "add":
        add_password()
    elif mode == "view":
        view_passwords()
    else:
        print("Invalid choice. Please type 'add' or 'view'.")


