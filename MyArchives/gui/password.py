import hashlib
import os
from tkinter import messagebox

import customtkinter as ctk

from .home_dir import home_directory

newpath = home_directory()

master = ctk.CTk() #I don't know why or how but this line prevents generation of a new window by tkinter


def new_pass():
    dialog = ctk.CTkInputDialog(
        master=None, text="Enter New Password", title="Password"
    )
    password = dialog.get_input()

    if password == None:
        quit()
    elif password == "":
        messagebox.showinfo("Invailid Password", "Password can't be a empty string")
        new_pass()
    else:
        # Password generation
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)

        # Store them as:
        storage = salt + key

        # Getting the values back out
        salt_from_storage = storage[:32]  # 32 is the length of the salt
        key_from_storage = storage[32:]

        with open(f"{newpath}Textfiles/pass.key", "wb") as f:
            f.write(storage)
        messagebox.showinfo("Password Set", "New Password Set!")


def check_pass():
    dialog = ctk.CTkInputDialog(
        master=None, text="Enter Your Password", title="Password"
    )
    password_to_check = dialog.get_input()  # The password provided by the user to check

    if password_to_check == None:
        quit()
    else:
        with open(f"{newpath}Textfiles/pass.key", "rb") as f:
            passwrd = f.read()

        passwrd_salt = passwrd[:32]
        passwrd_key = passwrd[32:]

        # Use the exact same setup you used to generate the key, but this
        # time put in the password to check
        new_key = hashlib.pbkdf2_hmac(
            "sha256",
            password_to_check.encode("utf-8"),
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
    if not os.path.exists(f"{newpath}Textfiles/pass.key"):
        new_pass()
    else:
        check_pass()
