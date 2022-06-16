from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as tk
from datetime import date
from tkinter import *

import customtkinter as ctk

from .home_dir import home_directory
from .online_sites import *

today = date.today()
y = today.strftime("%Y")
m = today.strftime("%m")
d = today.strftime("%d")
newpath = home_directory()


def main():
    master = ctk.CTk()
    master.geometry("837x484")
    master.title("MyArchives")
    master.iconbitmap(f"{newpath}Diary.ico")

    date_frame = Frame(master, background="#2a2d2e")
    # date_frame.place(x=0,y=0)
    date_frame.pack()

    box = ScrolledText(master, width=104, height=27, undo=True)
    box.insert(
        0.0, "Choose a date then leave the date box with cursor to see the entry"
    )
    # box.place(x=0, y=40)
    box.pack()

    def save(e):
        with open(
            f"{newpath}MyArchive/{year.get()}-{month.get()}-{date1.get()}.txt", "w"
        ) as f:
            f.write(box.get(0.0, END))

    box.bind("<Key>", save)

    yearL = ctk.CTkLabel(date_frame, text="Year :")
    yearL.grid(row=0, column=0)

    year = tk.Spinbox(date_frame, from_=1990, to=2100)
    year.insert(1, y)
    year.grid(row=0, column=1)

    monthL = ctk.CTkLabel(date_frame, text="Month :")
    monthL.grid(row=0, column=2)

    month = tk.Spinbox(date_frame, from_=1, to=12)
    month.insert(1, m)
    month.grid(row=0, column=3)

    dateL = ctk.CTkLabel(date_frame, text="Date :")
    dateL.grid(row=0, column=4)

    date1 = tk.Spinbox(date_frame, from_=1, to=31)
    date1.insert(1, d)
    date1.grid(row=0, column=5)

    def printer(e):
        try:
            with open(
                f"{newpath}MyArchive/{year.get()}-{month.get()}-{date1.get()}.txt", "r"
            ) as f:
                box.delete(0.0, END)
                box.insert(0.0, f.read())
        except:
            box.delete(0.0, END)
            box.insert(0.0, "No entry found! Start typing to save an entry...")

    date1.bind("<Leave>", printer)


    # Menubar
    my_menu = Menu(master)
    master.config(menu=my_menu)

    # Cut Text
    def cut_text(e):
        global selected
        # Check to see if keyboard shortcut used
        if e:
            selected = master.clipboard_get()
        else:
            if box.selection_get():
                # Grab selected text from text box
                selected = box.selection_get()
                # Delete Selected Text from text box
                box.delete("sel.first", "sel.last")
                # Clear the clipboard then append
                master.clipboard_clear()
                master.clipboard_append(selected)
    # Copy Text
    def copy_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = master.clipboard_get()

        if box.selection_get():
            # Grab selected text from text box
            selected = box.selection_get()
            # Clear the clipboard then append
            master.clipboard_clear()
            master.clipboard_append(selected)

    # Paste Text
    def paste_text(e):
        global selected
        #Check to see if keyboard shortcut used
        if e:
            selected = master.clipboard_get()
        else:
            if selected:
                position = box.index(INSERT)
                box.insert(position, selected)
    
    # Select all Text
    def select_all(e):
        # Add sel tag to select all text
        box.tag_add('sel', '1.0', 'end')

    # Clear All Text
    def clear_all():
        box.delete(1.0, END)

    # Add Edit Menu
    edit_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
    edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
    edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo", command=box.edit_undo, accelerator="(Ctrl+Z)")
    edit_menu.add_command(label="Redo", command=box.edit_redo, accelerator="(Ctrl+y)")
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All", command=lambda: select_all(True), accelerator="(Ctrl+a)")
    edit_menu.add_command(label="Clear", command=clear_all)

    #Create an Options menu item
    help_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Online", menu=help_menu)
    help_menu.add_command(label="Website", command=website)
    help_menu.add_separator()
    help_menu.add_command(label="Changelog", command=changelog)
    help_menu.add_command(label="Code of conduct", command=code_of_conduct)
    help_menu.add_command(label="License", command=license)
    help_menu.add_separator()
    help_menu.add_command(label="Contributing", command=contributing)
    help_menu.add_command(label="Releases", command=releases)
    master.mainloop()
