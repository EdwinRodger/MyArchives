import sqlite3
from os.path import expanduser


# Command to create a CMD-Diary folder in User directory if not already exists
home = expanduser("~")
newpath = f"{home}\\PyDiaries\\"

# Creating database and tables using sqlite

def database():
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
