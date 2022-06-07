import customtkinter as ctk
import tkinter as tk

def entrybox(master):
    box_frame = ctk.CTkFrame(master, width=616, height=600)
    box_frame.place(x=484, y=50)
    entry_box = tk.Text(box_frame, width=77, height=32)
    entry_box.pack(expand=True, fill="both")
    # def print1(e):
    #     print(entry_box.get(0.0,tk.END))
    # entry_box.bind("<Leave>", print1)