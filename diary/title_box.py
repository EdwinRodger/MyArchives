from tkinter import *

class titlebox():
    def __init__(self, master):
        title_box = Entry(master, width=23, font="Ariel 31")
        with open("text_files/title_template.txt", "r") as tb:
            r = tb.read()
        if r == "1":
            title_box.insert(0, "Title")
        else:
            pass
        title_box.place(x=525, y=25)
        #title_box = Entry(master, width=26, font="Ariel 32")
        #title_box.grid(row=0, column=1)