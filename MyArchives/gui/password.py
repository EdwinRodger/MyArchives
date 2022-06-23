import hashlib
import os
from sys import exit
from tkinter import messagebox
from tkinter.simpledialog import askstring
from customtkinter import CTk

from .home_dir import home_directory

homepath = home_directory()

# Uses MyArchives password for messagebox
CTk().iconbitmap(default=f"{homepath}Diary.ico")


def new_pass():
    dialog = askstring(title="Password", prompt="\t\tEnter New Password\t\t", show="●")

    if dialog == None:
        exit()
    elif dialog == "":
        messagebox.showinfo("Invailid Password", "Password can't be a empty string")
        new_pass()
    else:
        # Password generation
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac("sha256", dialog.encode("utf-8"), salt, 100000)

        # Store them as:
        storage = salt + key

        # Getting the values back out
        salt_from_storage = storage[:32]  # 32 is the length of the salt
        key_from_storage = storage[32:]

        with open(f"{homepath}Textfiles/pass.key", "wb") as f:
            f.write(storage)
        messagebox.showinfo("Password Set", "New Password Set!")


def check_pass():
    dialog = askstring(
        title="Password", prompt="\t\tEnter Your Password\t\t", show="●"
    )  # The password provided by the user to check

    if dialog == None:
        exit()
    else:
        with open(f"{homepath}Textfiles/pass.key", "rb") as f:
            passwrd = f.read()

        passwrd_salt = passwrd[:32]
        passwrd_key = passwrd[32:]

        # Use the exact same setup you used to generate the key, but this
        # time put in the password to check
        new_key = hashlib.pbkdf2_hmac(
            "sha256",
            dialog.encode("utf-8"),
            passwrd_salt,
            100000,
        )

        if new_key == passwrd_key:
            pass

        else:
            messagebox.showwarning(
                "Wrong Password", "The password you have entered is wrong... Try Again!"
            )
            check_pass()


def password_ui():
    if not os.path.exists(f"{homepath}Textfiles/pass.key"):
        new_pass()
    else:
        check_pass()
