from tkinter import *

with open(r"textFiles\path.txt", "r") as f:
    path = f.read()

monthrange = ("01","02","03","04","05","06","07","08","09","10","11","12")
dayrange = ("01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")

def view_entry():
    root = Tk()
    root.title("View Entry")
    root.geometry("715x450")
    root.resizable(0,0)
    root.iconbitmap("Diary.ico")

    date_frame = LabelFrame(root, text = "Date")
    date_frame.place(x = 10, y = 10)

    year = Label(date_frame, text = "Year:")
    year.grid(row = 0, column = 1)
    selected_year = Spinbox(date_frame, from_=1980, to=2030, wrap=True)
    selected_year.delete(0, END)
    selected_year.insert(0, "2022")
    selected_year.grid(row = 0, column = 2)
    seperator1 = Label(date_frame, text = "\t")
    seperator1.grid(row = 0, column = 3)
    month = Label(date_frame, text = "Month:")
    month.grid(row = 0, column = 4)
    selected_month = Spinbox(date_frame, values=monthrange, wrap=True)
    selected_month.grid(row = 0, column = 5)
    seperator2 = Label(date_frame, text = "\t")
    seperator2.grid(row = 0, column = 6)
    date = Label(date_frame, text = "Date:")
    date.grid(row = 0, column = 7)
    day = Spinbox(date_frame, values=dayrange, wrap=True)
    day.grid(row = 0, column = 8)

    textbox_frame = Frame(root)
    textbox_frame.place(x = 10, y = 50)

    scroll = Scrollbar(textbox_frame)
    scroll.pack(side=RIGHT, fill=Y)

    textbox = Text(textbox_frame, yscrollcommand=scroll.set)
    textbox.pack()

    scroll.config(command=textbox.yview)

    def view_entry():
        try:
            with open(f"{path}{selected_year.get()}-{selected_month.get()}-{day.get()}.txt", "r") as entry:
                textbox.delete(1.0, END)
                textbox.insert(1.0, entry.read())
        except:
            textbox.delete(1.0, END)
            textbox.insert(1.0, "No entry on this day")

    view_button = Button(root, text="View Date", command=view_entry, padx=7, pady=4)
    view_button.place(x = 640, y = 16)

    root.mainloop()