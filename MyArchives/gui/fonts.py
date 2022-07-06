from .home_dir import home_directory

homepath = home_directory()

def current_font():
    with open(f"{homepath}Textfiles/font.txt", 'r') as f:
            f.read()

def ariel():
    with open(f"{homepath}Textfiles/font.txt", 'w') as f:
            f.write("Ariel")

def calibri():
    with open(f"{homepath}Textfiles/font.txt", 'w') as f:
            f.write("Calibri")

def comic_sans():
    with open(f"{homepath}Textfiles/font.txt", 'w') as f:
            f.write("Comic_Sans")