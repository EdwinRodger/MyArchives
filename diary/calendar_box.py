from tkinter import *
from tkcalendar import *

class calen():
	def __init__(self, master):
		cal = Calendar(master, selectmode="day", date_pattern="dd-mm-yyyy", borderwidth=5, font="Arial 18")
		cal.place(x=50, y=75)
		#cal = Calendar(master, selectmode="day", date_pattern="dd-mm-yyyy", borderwidth=5, font="Arial 18")
		#cal.grid(row=1, column=0, rowspan=2)
		
		def grab_date():
			my_label.config(text="Selected date is " + cal.get_date())

		my_button = Button(master, text="Get Date", command=grab_date, padx=80, pady=20)
		my_button.place(x=150, y=395)
		#my_button = Button(master, text="Get Date", command=grab_date, padx=40, pady=20)
		#my_button.grid(row=3, column=0)

		my_label = Label(master, text="", pady=40)
		my_label.place(x=180, y=475)
		#my_label = Label(master, text="", pady=40)
		#my_label.grid(row= 4, column=0)
		