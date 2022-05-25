import os
from os import name, system
import hashlib
from time import sleep

with open("textFiles/password.txt", "r") as f:
    check = int(f.read())


# define our clear function
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def check_password():
    clear()
    with open("textFiles/pass.key", "rb") as f:
        passwrd = f.read()

    passwrd_salt = passwrd[:32]
    passwrd_key = passwrd[32:]

    password_to_check = input(
        "Enter Password: "
    )  # The password provided by the user to check

    # Use the exact same setup you used to generate the key, but this
    # time put in the password to check
    new_key = hashlib.pbkdf2_hmac(
        "sha256",
        password_to_check.encode("utf-8"),  # Convert the password to bytes
        passwrd_salt,
        100000,
    )

    if new_key == passwrd_key:
        pass

    else:
        wait = input("Password is incorrect... Try again!")
        check_password()


def new_password():
    clear()
    password = input("Enter Your New Password: ")

    # Password generation
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)

    # Store them as:
    storage = salt + key

    # Getting the values back out
    salt_from_storage = storage[:32]  # 32 is the length of the salt
    key_from_storage = storage[32:]

    with open("textFiles/pass.key", "wb") as f:
        f.write(storage)
    with open("textFiles/password.txt", "w") as f:
        f.write("1")
    check_password()


def passwordUI():
    if check == 0:
        new_password()
    else:
        check_password()
