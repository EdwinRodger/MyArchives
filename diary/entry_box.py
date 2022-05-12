from tkinter import *
from tkinter import ttk

class entrybox():
    def __init__(self,master):

        frame = Frame(master, width=40, height=15)
        frame.place(x=525, y=75)

        my_text = Text(frame, undo=True)
        with open("text_files/text_template.txt", "r") as bt:
            r = bt.read()
        if r == "1":
            my_text.insert(0.0, "Time I am writing this: \n\nWhat I did today -\n\n\n\nWhat i learned today -\n1.\n2.\n3.\n\nPlans for tommorow -\n")
        else:
            pass
        my_text.pack(side=LEFT,expand=True)

        sb_ver = Scrollbar(frame,orient=VERTICAL)
        sb_ver.pack(side=RIGHT, fill=Y)

        my_text.config(yscrollcommand=sb_ver.set)
        sb_ver.config(command=my_text.yview)