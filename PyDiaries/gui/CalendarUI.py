import tkcalendar as tkc
import customtkinter as ctk
import tkinter as tk

def calendar(master):
    cal = tkc.Calendar(master, font="Comic_Sans 21", showweeknumbers=False)
    cal.place(x=0)