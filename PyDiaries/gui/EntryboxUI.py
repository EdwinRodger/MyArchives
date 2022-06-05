import customtkinter as ctk
import tkinter as tk

def entrybox(master):
    box_frame = ctk.CTkFrame(master, width=616, height=600)
    box_frame.place(x=484)
    entry_box = tk.Text(box_frame)
    entry_box.pack(expand=True, fill="both")