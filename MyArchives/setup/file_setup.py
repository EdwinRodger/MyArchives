from os.path import exists
from .tasks import home_directory

homepath = home_directory()

def theme_setup():
    if not exists(f"{homepath}Textfiles/theme.txt"):
        with open(f"{homepath}Textfiles/theme.txt", "w") as f:
            f.write("0")
    else:
        pass