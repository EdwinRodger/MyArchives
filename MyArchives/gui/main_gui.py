import customtkinter as ctk
from .home_dir import home_directory
from datetime import date
import tkinter.ttk as tk
from tkinter import END, Frame, Text

today = date.today()
y = today.strftime("%Y")
m = today.strftime("%m")
d = today.strftime("%d")
newpath = home_directory()

def main():
    master = ctk.CTk()
    master.geometry("837x464")
    master.title("MyArchives")
    master.iconbitmap(f"{newpath}Diary.ico")

    date_frame = Frame(master, background="#2a2d2e")
    # date_frame.place(x=0,y=0)
    date_frame.pack()

    box = Text(master, width=104, height=27)
    box.insert(0.0, "Choose a date then leave the date box with cursor to see the entry")
    # box.place(x=0, y=40)
    box.pack()
    def save(e):
        with open(f"{newpath}MyArchive/{year.get()}-{month.get()}-{date1.get()}.txt", "w") as f:
            f.write(box.get(0.0, END))
    box.bind("<Key>", save)


    yearL = ctk.CTkLabel(date_frame, text="Year :")
    yearL.grid(row=0, column=0)

    year = tk.Spinbox(date_frame, from_=1990, to=2100)
    year.insert(1, y)
    year.grid(row = 0, column=1)


    monthL = ctk.CTkLabel(date_frame, text="Month :")
    monthL.grid(row=0, column=2)

    month = tk.Spinbox(date_frame, from_=1,to=12)
    month.insert(1, m)
    month.grid(row = 0,column=3)

    dateL = ctk.CTkLabel(date_frame, text="Date :")
    dateL.grid(row=0, column=4)

    date1 = tk.Spinbox(date_frame, from_=1, to=31)
    date1.insert(1,d)
    date1.grid(row=0, column=5)
    def printer(e):
        try:
            with open(f"{newpath}MyArchive/{year.get()}-{month.get()}-{date1.get()}.txt", "r") as f:
                box.delete(0.0, END)
                box.insert(0.0, f.read().rstrip())
        except:
            box.delete(0.0, END)
            box.insert(0.0, "No entry found! Start typing to save an entry...")
    date1.bind("<Leave>",printer)
    master.mainloop()