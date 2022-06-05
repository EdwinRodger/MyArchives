from gui.MainUI import main
from os.path import expanduser, os

# Command to create a CMD-Diary folder in User directory if not already exists
home = expanduser("~")
newpath = f"{home}\\CMD-Diary\\"
if not os.path.exists(newpath):
    os.makedirs(newpath)
if not os.path.exists(f"{newpath}\\Textfiles\\"):
    os.makedirs(f"{newpath}\\Textfiles\\")
with open(f"{home}\\CMD-Diary\\Textfiles\\path.txt", "w") as homedir:
    homedir.write(newpath)


if __name__=="__main__":
    main()