from tkinter import *

class entrybox():
    def __init__(self,master):
        global my_text
        my_text = Text(master, width=66, height=18, undo=True)
        with open("text_files/text_template.txt", "r") as bt:
            r = bt.read()
        if r == "1":
            my_text.insert(0.0, "Time I am writing this: \n\nWhat I did today -\n\n\n\nWhat i learned today -\n1.\n2.\n3.\n\nPlans for tommorow -\n")
        else:
            pass
        my_text.place(x=525, y=75)
        #my_text = Text(master, width=79, height=18)
        #my_text.grid(row=1, column=1)