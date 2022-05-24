from tkinter import *

with open("textFiles/path.txt", "r") as f:
    path = f.read()

with open("textFiles/template.txt", "r") as f:
    template = f.read()

monthrange = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
dayrange = (
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
)


def another_entry():
    root = Tk()
    root.title("Enter Another Day Entry")
    root.geometry("750x450")
    root.resizable(0, 0)
    root.iconbitmap("Diary.ico")

    date_frame = LabelFrame(root, text="Enter Date")
    date_frame.place(x=10, y=10)

    seperator1 = Label(date_frame, text="\t")
    seperator1.grid(row=0, column=0)
    year = Label(date_frame, text="Year:")
    year.grid(row=0, column=1)
    thisyear = Spinbox(date_frame, from_=1980, to=2030, wrap=True)
    thisyear.delete(0, END)
    thisyear.insert(0, "2022")
    thisyear.grid(row=0, column=2)
    seperator2 = Label(date_frame, text="\t")
    seperator2.grid(row=0, column=3)
    month = Label(date_frame, text="Month:")
    month.grid(row=0, column=4)
    thismonth = Spinbox(date_frame, values=monthrange, wrap=True)
    thismonth.grid(row=0, column=5)
    seperator3 = Label(date_frame, text="\t")
    seperator3.grid(row=0, column=6)
    date = Label(date_frame, text="Date:")
    date.grid(row=0, column=7)
    day = Spinbox(date_frame, values=dayrange, wrap=True)
    day.grid(row=0, column=8)
    seperator4 = Label(date_frame, text="\t")
    seperator4.grid(row=0, column=9)

    textbox_frame = Frame(root)
    textbox_frame.place(x=10, y=50)

    scroll = Scrollbar(textbox_frame)
    scroll.pack(side=RIGHT, fill=Y)

    textbox = Text(textbox_frame, yscrollcommand=scroll.set)
    textbox.pack()

    scroll.config(command=textbox.yview)

    if template == "1":
        textbox.insert(
            0.0,
            "Title - \n\nTime - \n\nWhat I did today - \n\n\n\nWhat I learned today -\n1.\n2.\n3.\n\nPlans for tomorrow -\n\n",
        )
    else:
        pass

    def save_entry():
        with open(
            f"{path}{thisyear.get()}-{thismonth.get()}-{day.get()}.txt", "w"
        ) as entry:
            entry.write(textbox.get(1.0, END))

    save_button = Button(root, text="Save", command=save_entry, padx=20, pady=182)
    save_button.place(x=670, y=50)

    root.mainloop()
