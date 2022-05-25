# Python Modules Used
from os import name, system
from tkinter import *

from res import OnlineHelp as oh
from res import PassWord as pw
from res import ShowSettings as ss
from res.GUI import another_entry as ae
from res.GUI import edit_entry as ee
from res.GUI import today_entry as te
from res.GUI import view_entry as ve

# Clear command to make a five line space to lessen the congestion


# define our clear function
def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


# Online Help UI for CMD-Diary


def onlinehelpUI():
    while True:
        clear()
        print("O n l i n e H e l p")
        print("-" * 19)
        print("1. Website")
        print("2. Changelog")
        print("3. Code of Conduct")
        print("4. Contributing")
        print("5. License")
        print("6. Releases")
        print("7. Back to settings")
        try:
            choice = int(input("Enter Your Choice (1 - 7): "))
            if choice == 1:
                oh.website()
            elif choice == 2:
                oh.changelog()
            elif choice == 3:
                oh.code_of_conduct()
            elif choice == 4:
                oh.contributing()
            elif choice == 5:
                oh.license()
            elif choice == 6:
                oh.releases()
            elif choice == 7:
                break
            else:
                wait = input("Please Choose From 1 to 7 Only")
        except:
            print("\n\nInvalid choice")
            wait = input()


# Settings UI for CMD-Diary


def settingsUI():
    while True:
        clear()
        print("  S e t t i n g s")
        print("-" * 19)
        print("1. Entry Folder Path")
        print("2. Change Password")
        print("3. About")
        print("4. Contribution")
        print("5. Help")
        print("6. Diary Template")
        print("7. Online Help")
        print("8. Back To Main Menu")
        try:
            choice = int(input("Enter Your Choice (1 - 8): "))
            if choice == 1:
                ss.change_path()
            elif choice == 2:
                pw.change_password()
            elif choice==3:
                ss.about()
            elif choice == 4:
                ss.contribution()
            elif choice == 5:
                ss.help()
            elif choice == 6:
                ss.template()
            elif choice == 7:
                onlinehelpUI()
            elif choice == 8:
                break
            else:
                print("Please Choose From 1 to 8 Only")
                wait = input()
        except:
            print("\n\nInvalid choice")
            wait = input()


# Main Menu of the CMD-Diary program


def main_menuUI():
    while True:
        try:
            clear()
            print("  C m d D i a r y")
            print("-" * 19)
            print("1. Add Today's Entry")
            print("2. Add Other Day Entry")
            print("3. Add To Entry")
            print("4. View An Entry")
            print("5. Settings")
            print("6. Exit")
            choice = int(input("\n\nEnter Your Choice (1 - 6): "))
            if choice == 1:
                te.today_entry()
            elif choice == 2:
                ae.another_entry()
            elif choice == 3:
                ee.edit_entry()
            elif choice == 4:
                ve.view_entry()
            elif choice == 5:
                settingsUI()
            elif choice == 6:
                break
            else:
                print("Please choose from 1 to 6 Only")
                wait = input()
        except:
            print("\n\nInvalid choice")
            wait = input()


pw.passwordUI()
main_menuUI()
