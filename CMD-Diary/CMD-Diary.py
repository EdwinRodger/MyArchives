from os.path import exists, expanduser, os

# newpath command to create a CMD-Diary folder in Programfiles if not already exists
home = expanduser("~")
newpath = f"{home}\\CMD-Diary\\"
if not os.path.exists(newpath):
    os.makedirs(newpath)
with open("textFiles/path.txt", "w") as homedir:
    homedir.write(newpath)

if __name__ == "__main__":
    from res import UserInterface
