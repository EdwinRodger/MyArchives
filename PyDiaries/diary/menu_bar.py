from tkinter import *
import webbrowser

class menubar():
    def __init__(self, master):

        # edit_menu ##################################################

       

        # settings_menu ##################################################

        def titleTemplate():
            if titletemplate.get() == 1:
                with open("text_files/title_template.txt", "w") as title:
                    title.write("1")
            else:
                with open("text_files/title_template.txt", "w") as title:
                    title.write("0")
        titletemplate = BooleanVar()
        with open("text_files/title_template.txt", "r") as titletemp:
            if titletemp.read() == "1":
                titletemplate.set(True)
            else:
                titletemplate.set(False)
        
        def textTemplate():
            if texttemplate.get() == 1:
                with open("text_files/text_template.txt", "w") as text:
                    text.write("1")
            else:
                with open("text_files/text_template.txt", "w") as text:
                    text.write("0")
        texttemplate = BooleanVar()
        with open("text_files/text_template.txt", "r") as texttemp:
            if texttemp.read() == "1":
                texttemplate.set(True)
            else:
                texttemplate.set(False)
        
        '''def darkMode():
            if darkmode.get() == 1:
                master.config(background='black')
                with open("text_files/darkmode.txt", "w") as dark:
                    dark.write("1")
            else:
                master.config(background='white')
                with open("text_files/darkmode.txt", "w") as dark:
                    dark.write("0")                
        darkmode = BooleanVar()
        with open("text_files/darkmode.txt","r") as darkm:
            if darkm.read() == "1":
                darkmode.set(True)
            else:
                darkmode.set(False)'''

        # help_menu ##################################################

        def website():
            webbrowser.open("https://github.com/EdwinRodger/CMD-Diary", new=2, autoraise=True)
        
        def license():
            webbrowser.open("https://github.com/EdwinRodger/CMD-Diary/blob/main/LICENSE", new=2, autoraise=True)

        def code_of_conduct():
            webbrowser.open("https://github.com/EdwinRodger/CMD-Diary/blob/main/CODE_OF_CONDUCT.md", new=2, autoraise=True)


        # Menu Bar ##################################################

        file_menu = Menu(master)
        master.config(menu = file_menu)

        edit_menu = Menu(file_menu, tearoff=False)
        edit_menu.add_command(label = "Undo", command=None, accelerator="Ctrl+z")
        edit_menu.add_command(label = "Redo", command=None, accelerator="Ctrl+y")
        edit_menu.add_separator()
        edit_menu.add_command(label = "Cut", command=None, accelerator="Ctrl+x")
        edit_menu.add_command(label = "Copy", command=None, accelerator="Ctrl+c")
        edit_menu.add_command(label = "Paste", command=None, accelerator="Ctrl+v")
        edit_menu.add_command(label = "Select All", command=None, accelerator="Ctrl+z")
        file_menu.add_cascade(label = "Edit", menu=edit_menu)

        settings_menu = Menu(file_menu, tearoff=False)
        settings_menu.add_checkbutton(label="Title template", onvalue=1, offvalue=0, variable=titletemplate, command=titleTemplate)
        settings_menu.add_checkbutton(label="Body Template", onvalue=1, offvalue=0, variable=texttemplate, command=textTemplate)
        #settings_menu.add_checkbutton(label='Darkmode', onvalue=1, offvalue=0, variable=darkmode, command=darkMode)
        file_menu.add_cascade(label = "Settings", menu=settings_menu)

        help_menu = Menu(file_menu, tearoff=False)
        help_menu.add_command(label = "Website", command=website)
        help_menu.add_separator()
        help_menu.add_command(label = "License", command=license)
        help_menu.add_command(label = "Code Of Conduct", command=code_of_conduct)
        file_menu.add_cascade(label = "Help", menu=help_menu)