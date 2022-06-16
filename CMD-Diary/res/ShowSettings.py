from tkinter import *
from tkinter import filedialog


def change_path():
    root = Tk()
    root.iconbitmap("Diary.ico")
    root.title("Change Folder")
    with open("textFiles/path.txt", "r") as f:
        path = f.read()
    info = Label(root, text=f"Your current Diary Folder: {path}").pack()
    foldername = filedialog.askdirectory(
        initialdir="~", title="Select folder to save Diary files", mustexist=True
    )
    if foldername == "":
        root.destroy()
        pass
    else:
        with open("textFiles/path.txt", "w") as new_folder:
            new_folder.write(f"{foldername}\\")
            root.destroy()


def about():
    with open("textFiles/about.txt", "r") as abt:
        print("\n\n" + abt.read())
    wait = input("\n\nPress enter to continue...")


def contribution():
    with open("textFiles/contribution.txt", "r") as contri:
        print("\n\n" + contri.read())
    wait = input("\n\nPress enter to continue...")


def help():
    with open("textFiles/helpme.txt", "r") as helpmeh:
        print("\n\n" + helpmeh.read())
    wait = input("\n\nPress enter to continue...")


def template():
    print("\n" * 5)
    tempt = input("Do you want a template to write your diary?(y/n)")
    if tempt == "y":
        with open("textFiles/template.txt", "w") as tt:
            tt.write("1")
        print("\n" * 5)
        text = input("Diary template ON")
    elif tempt == "n":
        with open("textFiles/template.txt", "w") as tt:
            tt.write("0")
        print("\n" * 5)
        text = input("Diary template OFF")
    else:
        print("\n" * 5)
        print("Enter on y or n (y = yes, n = no)")
        template()
