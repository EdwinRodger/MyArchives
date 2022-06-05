import customtkinter as ctk
from gui.CalendarUI import calendar
# from gui.EntryboxUI import entrybox
# from gui.MenubarUI import menubar

root = ctk.CTk()
root.geometry("1100x600")
# root.resizable(0,0)

cal = calendar(root)




root.mainloop()