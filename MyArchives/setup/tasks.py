""" Python file to handle repetitive tasks """

from os.path import expanduser


# Finds user home directory on different OS and makes a MyArchives folder
def home_directory():
    home = expanduser("~")
    homepath = f"{home}\\MyArchives\\"
    return homepath
