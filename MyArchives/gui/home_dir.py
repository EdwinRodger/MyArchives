from os.path import expanduser

def home_directory():
    home = expanduser("~")
    newpath = f"{home}\\MyArchives\\"
    return newpath