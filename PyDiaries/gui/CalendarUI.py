import tkcalendar as tkc

def calendar(master):
    cal = tkc.Calendar(master, font="Comic_Sans 21", showweeknumbers=False, date_pattern="y-mm-dd")
    cal.place(x=0)