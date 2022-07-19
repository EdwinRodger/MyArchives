# Python Libraries
from os.path import exists
from sys import exit
from tkinter import messagebox
from tkinter.simpledialog import askstring

# Third Party Libraries
from customtkinter import CTk

# MyArchives Libraries
from .home_dir import home_directory
from .encrypt_decrypt import decrypt

import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

homepath = home_directory()

# Uses MyArchives icon for messagebox
try:
    CTk().iconbitmap(default=f"{homepath}Diary.ico")
except:
    pass


def new_pass():
    dialog = askstring(title="Password", prompt="\t\tEnter New Password\t\t", show="●")

    if dialog == None:
        exit()
    elif dialog == "":
        messagebox.showinfo("Invailid Password", "Password can't be a empty string")
        new_pass()
    else:
        password = str.encode(dialog)
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        with open(f"{homepath}Textfiles/pass.key", "wb") as f:
            f.write(key)
        with open(f"{homepath}Textfiles/salt.txt", "wb") as f:
            f.write(salt)
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
        with open(f"{homepath}Textfiles/salt.txt", "rb") as f:
            salt = f.read()

        password = str.encode(dialog)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        # Password checking
        if key == passwrd:
            # If the files are not encrypted, decrypt will raise an error but files will get decrypted once the program get closed and after that decrypt won't give any more errors, try-except block is used for backward compatibility
            try:
                decrypt()
            except:
                pass

        else:
            messagebox.showwarning(
                "Wrong Password", "The password you have entered is wrong... Try Again!"
            )


def change_password():
    check_pass()
    new_pass()


def password_ui():
    if not exists(f"{homepath}Textfiles/pass.key"):
        new_pass()
    elif not exists(f"{homepath}Textfiles/salt.txt"):
        new_pass()
    else:
        check_pass()
