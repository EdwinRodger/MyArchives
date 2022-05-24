from tkinter import *
from datetime import date


todaydate = str(date.today())
listed_todaydate = todaydate.split("-")

with open(r"textFiles\path.txt", "r") as f:
    path = f.read()

with open(r"textFiles\template.txt", "r") as f:
    template = f.read()


def today_entry():
    root = Tk()
    root.title("Enter Today Entry")
    root.geometry("700x450")
    root.resizable(0, 0)
    root.iconbitmap("Diary.ico")

    date_frame = LabelFrame(root, text="Today Date")
    date_frame.place(x=10, y=10)

    seperator1 = Label(date_frame, text="\t\t\t").grid(row=0, column=0)
    year = Label(date_frame, text="Year:").grid(row=0, column=1)
    thisyear = Label(date_frame, text=listed_todaydate[0]).grid(row=0, column=2)
    seperator2 = Label(date_frame, text="\t").grid(row=0, column=3)
    month = Label(date_frame, text="Month:").grid(row=0, column=4)
    thismonth = Label(date_frame, text=listed_todaydate[1]).grid(row=0, column=5)
    seperator3 = Label(date_frame, text="\t").grid(row=0, column=6)
    date = Label(date_frame, text="Date:").grid(row=0, column=7)
    day = Label(date_frame, text=listed_todaydate[2]).grid(row=0, column=8)
    seperator4 = Label(date_frame, text="\t\t\t").grid(row=0, column=9)

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
        with open(rf"{path}{todaydate}.txt", "w") as todayentry:
            todayentry.write(textbox.get(1.0, END))

    save_button = Button(root, text="Save", command=save_entry, padx=20, pady=4)
    save_button.place(x=600, y=16)

    root.mainloop()
