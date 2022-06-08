import customtkinter as ctk
from gui.CalendarUI import calendar
from gui.EntryboxUI import entrybox
from gui.MenubarUI import menubar
from gui.TitleboxUI import titlebox

def main():
    root = ctk.CTk()
    root.title("MyArchives")
    root.geometry("1100x600")
    # root.resizable(0,0)

    cal = calendar(root)

    title = titlebox(root)
    entry = entrybox(root)

    menu_bar = menubar(root)




    root.mainloop()