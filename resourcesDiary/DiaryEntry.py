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
    with open('path.txt', 'r') as path:
        print("This is your current path ", path.readline(), "\n")
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
