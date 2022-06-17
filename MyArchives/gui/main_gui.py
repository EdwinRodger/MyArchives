import tkinter.ttk as tk
from time import strftime
from tkinter import *
from tkinter.scrolledtext import ScrolledText

import customtkinter as ctk
import tkcalendar

from .home_dir import home_directory
from .online_sites import *
from .password import new_pass, password_ui

newpath = home_directory()


def main():
    password_ui()
    ctk.set_default_color_theme("dark-blue")
    master = ctk.CTk()
    master.geometry("1077x600")
    master.title("MyArchives")
    master.iconbitmap(f"{newpath}Diary.ico")

    cal = tkcalendar.Calendar(master, font="comic_sans 18", showweeknumbers=False)
    cal.place(x=0, y=0)

    def get_date(e):
        try:
            with open(f"{newpath}MyArchive/{cal.selection_get()}.txt", "r") as f:
                box.delete(0.0, END)
                box.insert(0.0, f.read())
        except:
            box.delete(0.0, END)
            box.insert(0.0, "No entry found! Start typing to save an entry...")

    cal.bind("<Leave>", get_date)

    box = ScrolledText(master, width=82, height=30, undo=True)
    box.insert(
        0.0,
        "Choose a date then leave the calendar with cursor to see the entry\n\nAfter completing the writing, add an extra space to save the whole entry properly",
    )
    box.place(x=400)

    def save(e):
        if "<Key>" == "<Return>":
            box.insert("\n\n")
        with open(f"{newpath}MyArchive/{cal.selection_get()}.txt", "w") as f:
            f.write(box.get(0.0, END))

    def two_spaces(e):
        box.insert(float(box.index(INSERT)), "\n")

    box.bind("<Key>", save)
    box.bind("<Return>", two_spaces)

    # Clock
    def time():
        try:
            string = strftime("%I:%M:%S %p")
            ctime = Label(master, font=("Arial", 50), background="#1a1a1a", foreground="Green")
            ctime.config(text=string)
            ctime.after(1000, time)
            ctime.place(y=270, x=7)
        except:
            pass
    time()

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
        # Check to see if keyboard shortcut used
        if e:
            selected = master.clipboard_get()
        else:
            if selected:
                position = box.index(INSERT)
                box.insert(position, selected)

    # Select all Text
    def select_all(e):
        # Add sel tag to select all text
        box.tag_add("sel", "1.0", "end")

    # Clear All Text
    def clear_all():
        box.delete(1.0, END)

    # Add Edit Menu
    edit_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(
        label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)"
    )
    edit_menu.add_command(
        label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)"
    )
    edit_menu.add_command(
        label="Paste", command=lambda: paste_text(False), accelerator="(Ctrl+v)"
    )
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo", command=box.edit_undo, accelerator="(Ctrl+Z)")
    edit_menu.add_command(label="Redo", command=box.edit_redo, accelerator="(Ctrl+y)")
    edit_menu.add_separator()
    edit_menu.add_command(
        label="Select All", command=lambda: select_all(True), accelerator="(Ctrl+a)"
    )
    edit_menu.add_command(label="Clear", command=clear_all)

    # Create an Options menu item
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

    # Change Password menu
    password_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Change Password", menu=password_menu)
    password_menu.add_command(label="Change Password", command=new_pass)
    #If we comment the below line, the window will get close but the whole program will remain to run in background (In windows, you can see it using task manager under "background processes"). While developing, you will know it when you will close main window but the program won't get out of terminal
    master.protocol("WM_DELETE_WINDOW", quit)
    master.mainloop()
