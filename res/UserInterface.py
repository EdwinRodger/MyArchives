# Python Modules Used
from tkinter import *
from res import DiaryEntry as ds, ShowSettings as ss, OnlineHelp as oh
from res.GUI import today_entry as te, another_entry as ae, edit_entry as ee, view_entry as ve

# Clear command to make a five line space to lessen the congestion

def clear():
    print("\n"*5)

# Online Help UI for CMD-Diary

def onlinehelpUI():
    while True:
        clear()
        print("O n l i n e H e l p")
        print("-"*19)
        print("1. Website")
        print("2. Changelog")
        print("3. Code of Conduct")
        print("4. Contributing")
        print("5. License")
        print("6. Releases")
        print("7. Back to settings")
        try:
            choice = int(input("Enter Your Choice (1 - 7): "))
            if choice==1:
                oh.website()
            elif choice==2:
                oh.changelog()
            elif choice==3:
                oh.code_of_conduct()
            elif choice==4:
                oh.contributing()
            elif choice==5:
                oh.license()
            elif choice==6:
                oh.releases()
            elif choice==7:
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
        print("-"*19)
        print("1. Entry Folder Path")
        print("2. About")
        print("3. Contribution")
        print("4. Help")
        print("5. Diary Template")
        print("6. Online Help")
        print("7. Back To Main Menu")
        try:
            choice = int(input("Enter Your Choice (1 - 7): "))
            if choice==1:
                ds.entry_path()
            elif choice==2:
                ss.about()
            elif choice==3:
                ss.contribution()
            elif choice==4:
                ss.help()
            elif choice==5:
                ss.template()
            elif choice==6:
                onlinehelpUI()
            elif choice==7:
                break
            else:
                print("Please Choose From 1 to 7 Only")
                wait = input()
        except:
            print("\n\nInvalid choice")
            wait = input()

# Main Menu of the CMD-Diary program

def main_menuUI():
    while True:
        try:
            clear()
            print("   P y D i a r y")
            print("-"*19)
            print("1. Add Today's Entry")
            print("2. Add Other Day Entry")
            print("3. Add To Entry")
            print("4. View An Entry")
            print("5. Settings")
            print("6. Exit")
            choice = int(input("\n\nEnter Your Choice (1 - 6): "))
            if choice==1:
                te.today_entry()
            elif choice==2:
                ae.another_entry()
            elif choice==3:
                ee.edit_entry()
            elif choice==4:
                ve.view_entry()
            elif choice==5:
                settingsUI()
            elif choice==6:
                break
            else:
                print("Please choose from 1 to 6 Only")
                wait = input()
        except:
            print("\n\nInvalid choice")
            wait = input()


main_menuUI()