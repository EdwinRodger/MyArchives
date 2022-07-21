# Python Libraries
import threading
import tkinter as tk
from os import remove
from tkinter.messagebox import askyesno, showerror

# Third Party Libraries
from pyttsx3 import init
from sounddevice import rec, wait
from speech_recognition import AudioFile, Recognizer
from wavio import write

# MyArchives Libraries
from .home_dir import home_directory

homepath = home_directory()


# pyttsx3.init()
engine = init()

# Cut Text
def cut_text(e, window, text_box):
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

            # Clear the clipboard then apptk.end
            window.clipboard_clear()
            window.clipboard_apptk.end(selected)


# Copy Text
def copy_text(e, window, text_box):
    global selected
    # check to see if we used keyboard shortcuts
    if e:
        selected = window.clipboard_get()

    if text_box.selection_get():
        # Grab selected text from text box
        selected = text_box.selection_get()

        # Clear the clipboard then apptk.end
        window.clipboard_clear()
        window.clipboard_apptk.end(selected)


# Paste Text
def paste_text(e, window, text_box):
    global selected
    # Check to see if keyboard shortcut used
    if e:
        selected = window.clipboard_get()
    else:
        if selected:
            position = text_box.index(tk.INSERT)
            text_box.insert(position, selected)


# Select all Text
def select_all(e, text_box):
    # Add sel tag to select all text
    text_box.tag_add("sel", "1.0", "tk.end")


# Clear All Text
def clear_all(text_box):
    text_box.delete(1.0, tk.END)


# Text-To-Speech (threading)
def ttst(text_box, entry_box):
    def tts():
        voices = engine.getProperty("voices")
        with open(f"{homepath}Textfiles/voices.txt", "r") as f:
            voice = f.read()
        if voice == "0":
            engine.setProperty(
                "voice", voices[0].id
            )  # changing index, changes voices. 0 for male
            engine.say(entry_box.get())
            engine.say(text_box.get(0.0, tk.END))
            engine.runAndWait()
        elif voice == "1":
            engine.setProperty(
                "voice", voices[1].id
            )  # changing index, changes voices. 1 for female
            engine.say(entry_box.get())
            engine.say(text_box.get(0.0, tk.END))
            engine.runAndWait()
        else:
            engine.say(
                "There is some problem with Text To Speech, Try to change narrators voice and try again"
            )
            engine.runAndWait()

    tts_threading = threading.Thread(target=tts)
    tts_threading.start()


# Speech-To-Text (threading)
def sttt(text_box, cal):
    # tkinter.messagebox.askyesno()
    imp = askyesno(
        title="Important!",
        message="Some information before you use speech to text-\n\n1. You should have an active internet connection as STT uses google speech recognition to work\n2. If you don't say anything, the program will show an error\n3. Right now you can only record for 20 seconds in one go without able to stop the recording in between\n4. Because of privacy issues, you should not say very personal/explicit things as this recording first goes to google which then extracts text from it\n5. As of now, only English language is written irrespective of the language you speak\n6. The text will be placed at the current position of your cursor in the text box, do not place cursor in the title box as it will give an error\n7. The results may not meet your expectations\n8. You will hear a sound and then you can start to speak. When 20 seconds are up, another sound will be played asking you to wait\n\nDo you wish to continue?\n",
    )

    def stt():
        # Initialize the recognizer
        r = Recognizer()  # speech_recognition.Recognizer()

        # Sampling frequency
        frequency = 44400

        # Recording duration in seconds
        duration = 20
        try:
            engine.say("Listening!")
            engine.runAndWait()

            # to record audio from
            # sound-device into a Numpy
            recording = rec(
                int(duration * frequency), samplerate=frequency, channels=2
            )  # sounddevice.rec()

            # Wait for the audio to complete
            wait()  # sounddevice.wait()

            engine.say("Processing Audio, Please wait")
            engine.runAndWait()

            # using wavio to save the recording in .wav format
            # This will convert the NumPy array to an audio
            # file with the given sampling frequency
            write(
                f"{homepath}recording1.wav", recording, frequency, sampwidth=2
            )  # wavio.write()

            # speech_recognition.AudioFile()
            file_audio = AudioFile(f"{homepath}recording1.wav")

            with file_audio as source:
                audio_text = r.record(source)

            rt = r.recognize_google(audio_text)

            # os.remove()
            remove(f"{homepath}recording1.wav")

            text_box.insert(text_box.index(tk.INSERT), rt)

            with open(f"{homepath}MyArchive/{cal.selection_get()}.txt", "w") as f:
                f.write(text_box.get(0.0, tk.END))
        except Exception as e:
            # tkinter.messagebox.showerror()
            showerror(
                title="Error!",
                message=f"There is some error while using speech to text\n\n{e}",
            )

    if imp == True:
        stt_threading = threading.Thread(target=stt)
        stt_threading.start()
    else:
        pass


def narrator(voice):
    if voice == "male":
        with open(f"{homepath}Textfiles/voices.txt", "w") as f:
            f.write("0")
    elif voice == "female":
        with open(f"{homepath}Textfiles/voices.txt", "w") as f:
            f.write("1")
    else:
        showerror("Error!", "There is some error while changing narrator's voice")
