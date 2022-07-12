from .home_dir import home_directory

homepath = home_directory()

def light_theme(window, entry_box, text_box):
    window.configure(bg="#f9f9f9")
    entry_box.configure(bg="#e2e2e2", foreground="black")
    text_box.configure(bg="#e2e2e2", foreground="black")
    with open(f"{homepath}Textfiles/theme.txt", 'w') as f:
        f.write('0')

def dark_theme(window, entry_box, text_box):
    window.configure(bg="#1f1e21")
    entry_box.configure(bg="#353538", foreground="white")
    text_box.configure(bg="#353538", foreground="white")
    with open(f"{homepath}Textfiles/theme.txt", 'w') as f:
        f.write('1')