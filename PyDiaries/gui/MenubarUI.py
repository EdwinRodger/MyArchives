import customtkinter as ctk
import tkinter as tk

def menubar(master):
    file_menu = tk.Menu(master)
    master.config(menu = file_menu)

    edit_menu = tk.Menu(file_menu, tearoff=False)
    edit_menu.add_command(label = "Undo", command=None, accelerator="Ctrl+z")
    edit_menu.add_command(label = "Redo", command=None, accelerator="Ctrl+y")
    edit_menu.add_separator()
    edit_menu.add_command(label = "Cut", command=None, accelerator="Ctrl+x")
    edit_menu.add_command(label = "Copy", command=None, accelerator="Ctrl+c")
    edit_menu.add_command(label = "Paste", command=None, accelerator="Ctrl+v")
    edit_menu.add_command(label = "Select All", command=None, accelerator="Ctrl+z")
    file_menu.add_cascade(label = "Edit", menu=edit_menu)

    settings_menu = tk.Menu(file_menu, tearoff=False)
    settings_menu.add_checkbutton(label="Title template", onvalue=1, offvalue=0, variable=None, command=None)
    settings_menu.add_checkbutton(label="Body Template", onvalue=1, offvalue=0, variable=None, command=None)
    #settings_menu.add_checkbutton(label='Darkmode', onvalue=1, offvalue=0, variable=darkmode, command=darkMode)
    file_menu.add_cascade(label = "Settings", menu=settings_menu)

    help_menu = tk.Menu(file_menu, tearoff=False)
    help_menu.add_command(label = "Website", command=None)
    help_menu.add_separator()
    help_menu.add_command(label = "Changelog", command=None)
    help_menu.add_command(label = "Code Of Conduct", command=None)
    help_menu.add_command(label = "License", command=license)
    file_menu.add_cascade(label = "Help", menu=help_menu)