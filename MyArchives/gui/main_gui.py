# Python Libraries
import tkinter as tk
from sys import exit
from tkinter.scrolledtext import ScrolledText

# Third Party Libraries
import customtkinter as ctk
from tkcalendar import Calendar

# MyArchives Libraries
from .encrypt_decrypt import encrypt
from .home_dir import home_directory
from .import_export import *
from .menubar_functions import *
from .online_sites import *
from .password import change_password
from .themes import *

homepath = home_directory()


# This is Pyinstaller special import and doesn't come with python and can't be downloaded with package manager.
try:
    import pyi_splash

    # Close the splash screen
    pyi_splash.close()
except:
    pass


def main():
    ctk.set_default_color_theme("dark-blue")
    window = ctk.CTk()
    app_height = 443
    app_width = 1077

    # Taking primary monitor's screen height and width
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Placing app in the middle of the screen
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
    window.title("MyArchives")
    window.iconbitmap(f"{homepath}Diary.ico")

    # tkcaltk.endar.Caltk.endar()
    cal = Calendar(window, font="comic_sans 18", showweeknumbers=False)
    cal.place(x=0, y=0)

    # Checking if given date has a entry to it or not
    def get_date(e):
        try:
            with open(f"{homepath}MyArchive/{cal.selection_get()}.txt", "r") as f:
                lines = f.readlines()
            entry_box.delete(0, tk.END)
            text_box.delete(0.0, tk.END)
            entry_box.insert(0, lines[0])
            for j in lines[-1:0:-1]:
                text_box.insert(0.0, j)
        except:
            entry_box.delete(0, tk.END)
            text_box.delete(0.0, tk.END)
            entry_box.insert(0, "No entry found!")
            text_box.insert(0.0, "Start typing to save an entry...")

    cal.bind("<Leave>", get_date)

    entry_box = tk.Entry(
        window,
        font="Calibri 21 bold",
        width=48,
        bg="#353538",
        foreground="white",
        relief=tk.FLAT,
    )
    entry_box.insert(0, "Title")
    entry_box.place(x=400)

    # tkinter.scrolledtext.ScrolledText()
    text_box = ScrolledText(
        window,
        width=82,
        height=20,
        font="Calibri",
        bg="#353538",
        foreground="white",
        undo=True,
        relief=tk.FLAT,
    )
    text_box.insert(
        0.0,
        "Choose a date then leave the calendar with cursor to see the entry\n\nIf you edit the title then write something in entry to avoid bugs\n\nAvoid having <space>, <backspace> or any non-ascii character to be typped in the end to avoid bugs\n\nThat is all for instructions and bugs, you can start writing your entry :)",
    )
    text_box.place(x=400, y=39)

    def save(e):
        with open(f"{homepath}MyArchive/{cal.selection_get()}.txt", "w") as f:
            f.write(str(entry_box.get()))
            f.write("\n" + str(text_box.get(0.0, tk.END + "-1c") + e.char))

    def two_spaces(e):
        text_box.insert(float(text_box.index(tk.INSERT)), "\n")

    text_box.bind("<Key>", save)
    text_box.bind("<Return>", two_spaces)
    entry_box.bind("<Key>", save)

    # Menubar
    my_menu = tk.Menu(window)
    window.config(menu=my_menu)

    # MyArchives menu
    myarchives_menu = tk.Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=myarchives_menu)
    myarchives_menu.add_command(
        label="Speech-To-Text", command=lambda: sttt(text_box, cal)
    )
    myarchives_menu.add_command(label="Text-To-Speech", command=lambda: ttst(text_box, entry_box))
    narrator_menu = tk.Menu(my_menu, tearoff=False)
    myarchives_menu.add_cascade(label="Narrator's Voice", menu=narrator_menu)
    narrator_menu.add_command(label="Male", command=lambda: narrator("male"))
    narrator_menu.add_command(label="Female", command=lambda: narrator("female"))
    myarchives_menu.add_separator()
    import_menu = tk.Menu(my_menu, tearoff=False)
    myarchives_menu.add_cascade(label="Import", menu=import_menu)
    import_menu.add_command(
        label="JSON", command=import_json, accelerator="(MyArchives)"
    )
    import_menu.add_command(label="Zip", command=import_zip, accelerator="(MyArchives)")
    export_menu = tk.Menu(my_menu, tearoff=False)
    myarchives_menu.add_cascade(label="Export", menu=export_menu)
    export_menu.add_command(
        label="JSON", command=export_json, accelerator="(MyArchives)"
    )
    export_menu.add_command(
        label="Text", command=export_txt, accelerator="(MyArchives)"
    )
    export_menu.add_command(label="Zip", command=export_zip, accelerator="(MyArchives)")
    myarchives_menu.add_separator()
    myarchives_menu.add_command(
        label="Change Password", command=change_password
    )  # password.py/change_password()
    theme_menu = tk.Menu(my_menu, tearoff=False)
    myarchives_menu.add_cascade(label="Theme", menu=theme_menu)
    theme_menu.add_command(
        label="Light", command=lambda: light_theme(window, entry_box, text_box, cal)
    )
    theme_menu.add_command(
        label="Dark", command=lambda: dark_theme(window, entry_box, text_box, cal)
    )
    theme_menu.add_command(
        label="Hacker", command=lambda: hacker_theme(window, entry_box, text_box, cal)
    )
    backup_menu = tk.Menu(my_menu, tearoff=False)
    myarchives_menu.add_cascade(label="Weekly Backup", menu=backup_menu)
    backup_menu.add_command(label="Monday", command=monday_backup)
    backup_menu.add_command(label="Tuesday", command=tuesday_backup)
    backup_menu.add_command(label="Wednesday", command=wednesday_backup)
    backup_menu.add_command(label="Thursday", command=thursday_backup)
    backup_menu.add_command(label="Friday", command=friday_backup)
    backup_menu.add_command(label="Saturday", command=saturday_backup)
    backup_menu.add_command(label="Sunday", command=sunday_backup)
    backup_menu.add_command(label="No Backup", command=no_backup)
    weekly_backup()

    # Add Edit Menu
    edit_menu = tk.Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(
        label="Cut",
        command=lambda: cut_text(False, window, text_box),
        accelerator="(Ctrl+x)",
    )
    edit_menu.add_command(
        label="Copy",
        command=lambda: copy_text(False, window, text_box),
        accelerator="(Ctrl+c)",
    )
    edit_menu.add_command(
        label="Paste",
        command=lambda: paste_text(False, window, text_box),
        accelerator="(Ctrl+v)",
    )
    edit_menu.add_separator()
    edit_menu.add_command(
        label="Undo", command=text_box.edit_undo, accelerator="(Ctrl+Z)"
    )
    edit_menu.add_command(
        label="Redo", command=text_box.edit_redo, accelerator="(Ctrl+y)"
    )
    edit_menu.add_separator()
    edit_menu.add_command(
        label="Select All",
        command=lambda: select_all(True, text_box),
        accelerator="(Ctrl+a)",
    )
    edit_menu.add_command(label="Clear", command=lambda: clear_all(text_box))

    # Create an Options menu item
    help_menu = tk.Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Website", command=website)
    help_menu.add_separator()
    help_menu.add_command(label="Changelog", command=changelog)
    help_menu.add_command(label="Code of conduct", command=code_of_conduct)
    help_menu.add_command(label="License", command=license)
    help_menu.add_separator()
    help_menu.add_command(label="Contributing", command=contributing)
    help_menu.add_command(label="Releases", command=releases)
    help_menu.add_command(label="Give A Star", command=github_star)

    # Themeing Options

    def check_theme():
        with open(f"{homepath}Textfiles/theme.txt", "r") as f:
            mode = f.read()
        if mode == "0":
            light_theme(window, entry_box, text_box, cal)
        elif mode == "1":
            dark_theme(window, entry_box, text_box, cal)
        elif mode == "2":
            hacker_theme(window, entry_box, text_box, cal)

    check_theme()

    def end_processes():
        try:
            encrypt()  # encrypt_decrypt.py/encrypt()
            exit()  # sys.exit()
        except:
            exit()  # sys.exit()

    # If we comment the below line, the window will get close but the whole program
    # will remain to run in background (In windows, you can see it using task manager
    # under "background processes"). While developing, you will know it when you will
    # close main window but the program won't get out of terminal
    window.protocol("WM_DELETE_WINDOW", end_processes)
    window.mainloop()
