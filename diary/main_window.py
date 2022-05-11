from tkinter import *
from .calendar_box import calen
from .menu_bar import menubar
from .entry_box import entrybox
from .title_box import titlebox
#from menubar import menubar
#from entrybox import entrybox
#from titlebox import titlebox

class root():
    root = Tk()
    root.title("CMD Diary")
    root.iconbitmap("images/py.ico")
    root.geometry("1100x600")
    root.resizable(0,0)

    # Menubar
    m = menubar(root)

    # Calendar
    c = calen(root)

    # Titlebox
    tb = titlebox(root)

    # Textbox
    t = entrybox(root)


    root.mainloop()