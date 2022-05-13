# Python Modules Used

from resourcesDiary import DiaryEntry as ds
from resourcesDiary import ShowSettings as ss

# Clear command to make a five line space to lessen the congestion

def clear():
    print("\n"*5)

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
        print("5. Back To Main Menu")
        try:
            choice = int(input("Enter Your Choice (1 - 5): "))
            if choice==1:
                ds.entry_path()
            elif choice==2:
                ss.about()
            elif choice==3:
                ss.contribution()
            elif choice==4:
                ss.help()
            elif choice==5:
                break
            else:
                print("Please Choose From 1 to 5 Only")
                wait = input()
        except:
            print("\n\nInvalid choice")
            wait = input()

# Main Menu of the CMD-Diary program

def main_menuUI():
    while True:
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
            ds.new_entry()
        elif choice==2:
            ds.other_entry()
        elif choice==3:
            ds.edit_entry()
        elif choice==4:
            ds.view_entry()
        elif choice==5:
            settingsUI()
        elif choice==6:
            break
        else:
            print("Please choose from 1 to 6 Only")
            wait = input()


main_menuUI()