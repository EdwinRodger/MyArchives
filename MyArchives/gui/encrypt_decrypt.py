from os import listdir

from cryptography.fernet import Fernet

from .home_dir import home_directory

homepath = home_directory()
try:
    with open(f"{homepath}Textfiles/pass.key", "rb") as f:
        key = f.read()
    f = Fernet(key)
    dir = f"{homepath}MyArchive/"
    files = []

    for i in listdir(f"{homepath}MyArchive/"):
        files.append(i)
except:
    pass


def encrypt():
    for fname in files:
        # opening the original file to encrypt
        with open(f"{homepath}MyArchive/{fname}", "rb") as file:
            original = file.read()

        # encrypting the file
        encrypted = f.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(f"{homepath}MyArchive/{fname}", "wb") as encrypted_file:
            encrypted_file.write(encrypted)


def decrypt():
    for fname in files:
        # opening the encrypted file
        with open(f"{homepath}MyArchive/{fname}", "rb") as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = f.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(f"{homepath}MyArchive/{fname}", "wb") as dec_file:
            dec_file.write(decrypted)
