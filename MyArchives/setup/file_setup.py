from .tasks import home_directory
from os.path import exists

homepath = home_directory()

def font_file():
    if not exists(f"{homepath}Textfiles/font.txt"):
        with open(f"{homepath}Textfiles/font.txt", 'w') as f:
            f.write("Calibri")
    else:
        pass