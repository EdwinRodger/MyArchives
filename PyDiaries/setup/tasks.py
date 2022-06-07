''' Python file to handle repetitive tasks '''

from os.path import expanduser, os

# Finds user home directory on different OS and makes a PyDiaries folder
def home_directory():
    home = expanduser("~")
    newpath = f"{home}\\PyDiaries\\"
    return home, newpath