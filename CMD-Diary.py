# Python Modules Used

import datetime
import os
import os.path

# newpath command to create a CMD-Diary folder in Programfiles if not already exists

newpath = 'C:\\CMD-Diary\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Clear command to make a five line space to lessen the congestion

def clear():
    print("\n"*5)

# new_entry command to make today's entry

tday = datetime.date.today()
today = str(tday)
tdaytime = datetime.time()
todaytime = str(tdaytime)
t = datetime.datetime.today()
ti = t.time()
time = str(ti)

def new_entry():
    clear()
    path1 = read_path()
    name_of_file = today
    completeName = os.path.join(path1, name_of_file+".txt") 
    with open(completeName, "w") as entry:
        entry.write("Date : " + today + "\n")
        entry.write("Time : " + time + "\n\n\n")
        title = input("Title of Entry : ")
        entry.write("Title - " + title + "\n\n")
        toFile = input("\n\nWrite into your entry\t")
        entry.write(toFile)

# other_entry command to make another day's entry

def other_entry():
    clear()
    path1 = read_path()
    name_of_file = input("Enter a date in YYYY-MM-DD format: ")
    completeName = os.path.join(path1, name_of_file+".txt")
    with open(completeName, "w") as entry:
        entry.write("Date : " + today + "\n\n")
        title = input("\nTitle of Entry : ")
        entry.write("Title - " + title + "\n\n")
        toFile = input("\n\nWrite into your entry\t")
        entry.write(toFile)

# edit_entry command to append information in an already existing entry

def edit_entry():
    try:
        clear()
        path1 = read_path()
        date = input("Enter Entry Date That You Want To Add To(YYYY-MM-DD): ")
        save_path = path1 + date
        with open(save_path + ".txt", "a") as entry:
            print("\nAdd to the entry\n")
            edit = input()
            entry.write("\n" + edit)
    except:
        print("Date not found... Check the date again...")

# view_entry command to see an already existing entry

def view_entry():
    try:
        clear()
        path1 = read_path()
        view = input("Enter the date of entry to view(YYYY-MM-DD): ")
        save_path = path1 + view
        with open(save_path + ".txt", "r") as entry:
            see = entry.read()
            print("\n\n\n" + see)
            print("\n\n\nPress Enter to proceed")
            wait = input()
    except:
        print("Date not found... Check the date again...")

# entry_path command to specify the directory or folder where the text files will be kept

def entry_path():
    clear()
    with open('path.txt','w') as path:
        ogpath = input("Enter a valid folder path: ")
        newpath = ogpath.replace('\\','/')
        newpath = newpath + '/'
        path.write(newpath)

# read_path command to read the path of the directory or folder where the text files are kept

def read_path():
    with open('path.txt', 'r') as path:
        a = path.readline()
        return a

# helpme command shows information related to some problems faced during running of program

def helpme():
    clear()
    with open('Help.txt', 'r') as helpmeh:
        print(helpmeh.read())
        wait = input("\nPress enter to continue")

# contribution command to read the information present in Contribution.txt

def contribution():
    clear()
    with open("Contribution.txt", "r") as contri:
        print(contri.read())
        wait = input("\nPress enter to continue...")

# about commant to read the information present in About.txt

def about():
    clear()
    with open("About.txt", "r") as about:
        print(about.read())
        wait = input("\nPress enter to continue...")

# Settings UI for CMD-Diary

def settings():
    while True:
        clear()
        print("  S e t t i n g s")
        print("-"*19)
        print("1. Entry Folder Path")
        print("2. Help")
        print("3. Contribution")
        print("4. About")
        print("5. Back To Main Menu")
        try:
            choice = int(input("Enter Your Choice (1 - 5): "))
            if choice==1:
                entry_path()
            elif choice==2:
                helpme()
            elif choice==3:
                contribution()
            elif choice==4:
                about()
            elif choice==5:
                break
            else:
                print("Please Choose From 1 to 5 Only")
                wait = input()
        except:
            print("\n\nInvalid choice")
            wait = input()

# Main Menu of the CMD-Diary program

def main_menu():
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
            new_entry()
        elif choice==2:
           other_entry()
        elif choice==3:
            edit_entry()
        elif choice==4:
            view_entry()
        elif choice==5:
            settings()
        elif choice==6:
            break
        else:
            print("Please choose from 1 to 6 Only")
            wait = input()


main_menu()
