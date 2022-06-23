from os.path import expanduser


def home_directory():
    home = expanduser("~")
    homepath = f"{home}\\MyArchives\\"
    return homepath
