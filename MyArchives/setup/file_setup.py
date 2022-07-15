from os.path import exists
from .tasks import home_directory

homepath = home_directory()

def files_setup():
    # Creates a files for theme configuration
    if not exists(f"{homepath}Textfiles/theme.txt"):
        with open(f"{homepath}Textfiles/theme.txt", "w") as f:
            f.write("0")
    # Creates a file for Weekly Backup Day
    if not exists(f"{homepath}Textfiles/weekly_backup_day.txt"):
        with open(f"{homepath}Textfiles/weekly_backup_day.txt", "w") as f:
            f.write("none")