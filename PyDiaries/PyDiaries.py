import sqlite3
from gui.MainUI import main
from os.path import expanduser, os

# Command to create a CMD-Diary folder in User directory if not already exists
home = expanduser("~")
newpath = f"{home}\\PyDiaries\\"
if not os.path.exists(newpath):
    os.makedirs(newpath)
if not os.path.exists(f"{newpath}\\Textfiles\\"):
    os.makedirs(f"{newpath}\\Textfiles\\")
with open(f"{home}\\PyDiaries\\Textfiles\\path.txt", "w") as homedir:
    homedir.write(newpath)

# Creating database and tables using sqlite

# creating data base
conn = sqlite3.connect(f"{newpath}Diary.db")

# creating cursor
c = conn.cursor() 

# creating table

c.execute("""CREATE TABLE if not exists Entries (
    date text,
    time text,
    title text,
    text text
)""")

# commiting changes
conn.commit() 

# close connection
conn.close() 


if __name__=="__main__":
    main()