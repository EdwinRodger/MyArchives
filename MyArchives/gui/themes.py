from .home_dir import home_directory

homepath = home_directory()


def light_theme(window, entry_box, text_box, cal):
    window.config(bg="#e2e2e2")
    entry_box.config(bg="#f9f9f9", foreground="black")
    text_box.config(bg="#f9f9f9", foreground="black")
    cal.config(
        background="#e2e2e2",
        foreground="black",
        bordercolor="#e2e2e2",
        headersbackground="#e2e2e2",
        headersforeground="grey",
        selectbackground="grey",
        selectforeground="white",
        normalbackground="#e2e2e2",
        normalforeground="black",
        weekendbackground="#e2e2e2",
        weekendforeground="black",
        othermonthforeground="3b3a3c",
        othermonthweforeground="3b3a3c",
        othermonthbackground="#e2e2e2",
        othermonthwebackground="#e2e2e2",
    )
    with open(f"{homepath}Textfiles/theme.txt", "w") as f:
        f.write("0")


def dark_theme(window, entry_box, text_box, cal):
    window.config(bg="#1f1e21")
    entry_box.config(bg="#353538", foreground="white")
    text_box.config(bg="#353538", foreground="white")
    cal.config(
        background="#1f1e21",
        foreground="white",
        bordercolor="#1f1e21",
        headersbackground="#1f1e21",
        headersforeground="grey",
        selectbackground="grey",
        selectforeground="white",
        normalbackground="#1f1e21",
        normalforeground="white",
        weekendbackground="#1f1e21",
        weekendforeground="white",
        othermonthforeground="3b3a3c",
        othermonthweforeground="3b3a3c",
        othermonthbackground="#1f1e21",
        othermonthwebackground="#1f1e21",
    )
    with open(f"{homepath}Textfiles/theme.txt", "w") as f:
        f.write("1")

'''Use below template to create custom themes. Replace custom_theme with your theme name and replace the "color name/hash" with your desired theme colors. You can remove the options which you didn't used.'''
def custom_theme(window, entry_box, text_box, cal):
    window.config(bg="color name/hash") # backgroud color of main window
    entry_box.config(
        bg="color name/hash", # backgroud color.
        foreground="color name/hash" # font color.
    )
    text_box.config(
        bg="color name/hash", # backgroud Color.
        foreground="color name/hash" # font color.
    )
    cal.config(
        background = "color name/hash", # background color of calendar border and month/year name
        foreground = "color name/hash", # foreground color of month/year name
        disabledbackground = "color name/hash", # background color of calendar border and month/year name in disabled state
        disabledforeground = "color name/hash", # foreground color of month/year name in disabled state
        bordercolor = "color name/hash", # day border color
        headersbackground = "color name/hash", # background color of day names and week numbers
        headersforeground = "color name/hash", # foreground color of day names and week numbers
        selectbackground = "color name/hash", # background color of selected day
        selectforeground = "color name/hash", # foreground color of selected day
        disabledselectbackground = "color name/hash", # background color of selected day in disabled state
        disabledselectforeground = "color name/hash", # foreground color of selected day in disabled state
        normalbackground = "color name/hash", # background color of normal week days
        normalforeground = "color name/hash", # foreground color of normal week days
        weekendbackground = "color name/hash", # background color of week-end days
        weekendforeground = "color name/hash", # foreground color of week-end days
        othermonthforeground = "color name/hash", # foreground color of normal week days belonging to the previous/next month
        othermonthbackground = "color name/hash", # background color of normal week days belonging to the previous/next month
        othermonthweforeground = "color name/hash", # foreground color of week-end days belonging to the previous/next month
        othermonthwebackground = "color name/hash", # background color of week-end days belonging to the previous/next month
        disableddaybackground = "color name/hash", # background color of days in disabled state
        disableddayforeground = "color name/hash", # foreground color of days in disabled state
    )