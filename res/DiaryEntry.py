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

# diary_template command to provide a template to write the diary entry

def diary_template():
    with open("textFiles/template.txt", "r") as tempt:
        mode = tempt.read()

    if mode == "1":
        clear()
        path1 = read_path()
        name_of_file = today
        completeName = os.path.join(path1, name_of_file+".txt") 
        title = input("Title: ")
        print("\n\n")
        time = input("Time I am writing this: ")
        print("\n\n")
        objective = input("What I did today -\n\n")
        print("\n\n")
        print("What I learned today -")
        learn1 = input("1. ")
        learn2 = input("2. ")
        learn3 = input("3. ")
        print("\n\n")
        tomo = input("plans for tomorrow -")
        with open(completeName, "w") as entry:
            entry.write(f"Title: {title}\n\n")
            entry.write(f"Time: {time}\n\n")
            entry.write(f"What I did today -\n\n{objective}\n\n")
            entry.write(f"What I learned today -\n1. {learn1}\n2. {learn2}\n3. {learn3}\n\n")
            entry.write(f"Plans for tomorrow -\n\n{tomo}")
    else:
        new_entry()
    

# entry_path command to specify the directory or folder where the text files will be kept

def entry_path():
    clear()
    with open('textFiles/path.txt', 'r') as path:
        print("This is your current path ", path.readline(), "\n")
    with open('path.txt','w') as path:
        ogpath = input("Enter a valid folder path: ")
        newpath = ogpath.replace('\\','/')
        newpath = newpath + '/'
        path.write(newpath)

# read_path command to read the path of the directory or folder where the text files are kept

def read_path():
    with open('textFiles/path.txt', 'r') as path:
        a = path.readline()
        return a
