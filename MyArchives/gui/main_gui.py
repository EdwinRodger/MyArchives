# Python Libraries
from sys import exit
from time import strftime
from tkinter import *
from tkinter.messagebox import askyesno, showerror
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Entry

# Third Party Libraries
import customtkinter as ctk
import pyttsx3
import sounddevice as sd
import speech_recognition as sr
import tkcalendar
import wavio as wv

# User Made Libraries
from .home_dir import home_directory
from .online_sites import *
from .password import new_pass

homepath = home_directory()
engine = pyttsx3.init()


def main():
    ctk.set_default_color_theme("dark-blue")
    window = ctk.CTk()
    app_height = 444
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

    cal = tkcalendar.Calendar(window, font="comic_sans 18", showweeknumbers=False)
    cal.place(x=0, y=0)

    def get_date(e):
        try:
            with open(f"{homepath}MyArchive/{cal.selection_get()}.txt", "r") as f:
                lines = f.readlines()
            entry_box.delete(0, END)
            text_box.delete(0.0, END)
            entry_box.insert(0, lines[0])
            for j in lines[-1:0:-1]:
                text_box.insert(0.0, j)
        except:
            entry_box.delete(0, END)
            text_box.delete(0.0, END)
            entry_box.insert(0, "No entry found!")
            text_box.insert(0.0, "Start typing to save an entry...")

    cal.bind("<Leave>", get_date)

    entry_box = Entry(window, font="Calibri 21", width=48)
    entry_box.insert(0, "Title")
    entry_box.place(x=400)

    text_box = ScrolledText(window, width=82, height=20, font="Calibri", undo=True)
    text_box.insert(
        0.0,
        "Choose a date then leave the calendar with cursor to see the entry\n\nAfter completing the writing, add an extra space to save the whole entry properly",
    )
    text_box.place(x=400, y=40)

    def save(e):
        if "<Key>" == "<Return>":
            text_box.insert("\n\n")
        with open(f"{homepath}MyArchive/{cal.selection_get()}.txt", "w") as f:
            f.write(entry_box.get())
            f.write("\n")
            f.write(text_box.get(0.0, END))

    def two_spaces(e):
        text_box.insert(float(text_box.index(INSERT)), "\n")

    text_box.bind("<Key>", save)
    text_box.bind("<Return>", two_spaces)
    entry_box.bind("<Key>", save)

    # Clock
    def time():
        try:
            string = strftime("%I:%M:%S %p")
            ctime = Label(
                window, font=("Arial", 50), background="#1a1a1a", foreground="Green"
            )
            ctime.config(text=string)
            ctime.after(1000, time)
            ctime.place(y=270, x=7)
        except:
            pass

    time()

    # Menubar
    my_menu = Menu(window)
    window.config(menu=my_menu)

    # Cut Text
    def cut_text(e):
        global selected
        # Check to see if keyboard shortcut used
        if e:
            selected = window.clipboard_get()
        else:
            if text_box.selection_get():
                # Grab selected text from text box
                selected = text_box.selection_get()
                # Delete Selected Text from text box
                text_box.delete("sel.first", "sel.last")
                # Clear the clipboard then append
                window.clipboard_clear()
                window.clipboard_append(selected)

    # Copy Text
    def copy_text(e):
        global selected
        # check to see if we used keyboard shortcuts
        if e:
            selected = window.clipboard_get()

        if text_box.selection_get():
            # Grab selected text from text box
            selected = text_box.selection_get()
            # Clear the clipboard then append
            window.clipboard_clear()
            window.clipboard_append(selected)

    # Paste Text
    def paste_text(e):
        global selected
        # Check to see if keyboard shortcut used
        if e:
            selected = window.clipboard_get()
        else:
            if selected:
                position = text_box.index(INSERT)
                text_box.insert(position, selected)

    # Select all Text
    def select_all(e):
        # Add sel tag to select all text
        text_box.tag_add("sel", "1.0", "end")

    # Clear All Text
    def clear_all():
        text_box.delete(1.0, END)

    # Text-To-Speech
    def tts():
        engine.say(text_box.get(0.0, END))
        engine.runAndWait()

    # Speech-To-Text
    def stt():
        # Initialize the recognizer
        r = sr.Recognizer()

        # Sampling frequency
        frequency = 44400

        # Recording duration in seconds
        duration = 20
        try:
            imp = askyesno(
                title="Important!",
                message="Some information before you use speech to text-\n\n1. You should have an active internet connection as STT uses google speech recognition to work\n2. If you don't say anything, the program will show an error\n3. Right now you can only record for 20 seconds in one go without able to stop the recording in between\n4. Because of privacy issues, you should not say very personal/explicit things as this recording first goes to google which then extracts text from it\n5. As of now, only English language is written irrespective of the language you speak\n6. The program may stop responding while you use STT but it is expected behaviour, wait for few moments and your speech will be converted to text\n7. The results may not meet your expectations\n8. You will hear a sound and then you can start to speak. When 20 seconds are up, another sound will be played asking you to wait\n\nDo you wish to continue?\n",
            )
            if imp == True:
                engine.say("Listening!")
                engine.runAndWait()

                # to record audio from
                # sound-device into a Numpy
                recording = sd.rec(
                    int(duration * frequency), samplerate=frequency, channels=2
                )

                # Wait for the audio to complete
                sd.wait()

                engine.say("Processing Audio, Please wait")
                engine.runAndWait()

                # using wavio to save the recording in .wav format
                # This will convert the NumPy array to an audio
                # file with the given sampling frequency
                wv.write(f"{homepath}recording1.wav", recording, frequency, sampwidth=2)

                file_audio = sr.AudioFile(f"{homepath}recording1.wav")

                with file_audio as source:
                    audio_text = r.record(source)

                rt = r.recognize_google(audio_text)

                text_box.insert(0.0, f"\n\n{rt}\n\n")

                with open(f"{homepath}MyArchive/{cal.selection_get()}.txt", "w") as f:
                    f.write(text_box.get(0.0, END))
            else:
                pass
        except Exception as e:
            showerror(
                title="Error!",
                message=f"There is some error while using speech to text\n\n{e}",
            )

    # MyArchives menu
    myarchives_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=myarchives_menu)
    myarchives_menu.add_command(label="Text-To-Speech", command=tts)
    myarchives_menu.add_command(label="Speech-To-Text", command=stt)
    myarchives_menu.add_separator()
    myarchives_menu.add_command(label="Change Password", command=new_pass)

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
    edit_menu.add_command(
        label="Undo", command=text_box.edit_undo, accelerator="(Ctrl+Z)"
    )
    edit_menu.add_command(
        label="Redo", command=text_box.edit_redo, accelerator="(Ctrl+y)"
    )
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

    # If we comment the below line, the window will get close but the whole program will remain to run in background (In windows, you can see it using task manager under "background processes"). While developing, you will know it when you will close main window but the program won't get out of terminal
    window.protocol("WM_DELETE_WINDOW", exit)
    window.mainloop()
