
from tkinter import END
import customtkinter as ctk
# from setup.database_setup import database_connect

# conn, c = database_connect()

def titlebox(master):
    title = ctk.CTkEntry(master, width=616, height=50)
    title.insert(0, "Enter title here")
    title.place(x=484)
    # def save_title(e):
    #     c.execute(f"""INSERT VALUES (title, {title.get(0,END)})""")
    # title.bind("<Return>", save_title)