# Python Libraries
from json import load, dump
from os import listdir
from shutil import make_archive
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.messagebox import showerror
from zipfile import ZipFile
import datetime
import calendar

# MyArchives Libraries
from .home_dir import home_directory
from datetime import datetime, date

# returns current date and time
now = datetime.now()


homepath = home_directory()


def export_zip():
    save_dir = askdirectory(title="Select folder to save zip file", mustexist=True)
    make_archive(f"{save_dir}/MyArchives-Export", "zip", f"{homepath}MyArchive")


def import_zip():
    try:
        zip_dir = askopenfilename(
            title="Select A zip File To Import",
            filetypes=(("zip file", "*.zip"), ("all files", "*.*")),
        )
        if zip_dir == "":
            pass
        else:
            with ZipFile(zip_dir, "r") as zip_ref:
                zip_ref.extractall(f"{homepath}/MyArchive")
    except Exception as e:
        showerror("Import Error!", f"An error has occurred\n\n{e}")
        import_zip()


def export_txt():
    save_dir = askdirectory(title="Select folder to save text file", mustexist=True)
    files = []

    for i in listdir(f"{homepath}MyArchive/"):
        files.append(i)

    with open(f"{save_dir}/MyArchives-Export.txt", "w") as outfile:
        outfile.write("MyArchives\n\n\n\n")
        for fname in files:
            with open(f"{homepath}MyArchive/{fname}") as infile:
                fname1 = fname.rstrip(".txt")
                outfile.write(f"{fname1}")
                outfile.write("\n")
                outfile.write(infile.read())
                outfile.write("-----\n\n")


def export_json():
    save_dir = askdirectory(title="Select folder to save text file", mustexist=True)
    files = []

    for i in listdir(f"{homepath}MyArchive/"):
        files.append(i)

    MyArchives = []

    metadata = {"Author": "EdwinRodger", "Name": "MyArchives", "Export Date": f"{now}"}

    data = {"Metadata": metadata, "MyArchives": MyArchives}

    with open(f"{save_dir}/MyArchives-Export.json", "w") as outfile:
        for fname in files:
            with open(f"{homepath}MyArchive/{fname}") as infile:
                fname1 = fname.rstrip(".txt")
                lines = infile.readlines()
                title = lines[0]
                listed_text = []
                for line in lines[1:]:
                    listed_text.append(line)
                text = " ".join(map(str, listed_text[0:]))
                entry = {
                    "Date": f"{fname1}",
                    "Title": f"{title.rstrip()}",
                    "Text": f"{text.lstrip()}",
                }
                MyArchives.append(entry)
        dump(data, outfile, indent=4)


def import_json():
    try:
        json_dir = askopenfilename(
            title="Select A json File To Import",
            filetypes=(("json file", "*.json"), ("all files", "*.*")),
        )
        if json_dir == "":
            pass
        else:
            with open(json_dir) as f:
                data = load(f)
            for i in data["MyArchives"][1:]:
                with open(f"{homepath}MyArchive\{i['Date']}.txt", "w") as f:
                    f.write(i["Title"] + "\n")
                    f.write(i["Text"])
    except Exception as e:
        showerror("Import Error!", f"An error has occurred\n\n{e}")
        import_json()


def weekly_backup():

    with open(f"{homepath}Textfiles/weekly_backup_day.txt", "r") as f:
        day = f.read()

    today = str(date.today())

    day_number = datetime.strptime(today.replace("-", " "), "%Y %m %d").weekday()
    today_day = calendar.day_name[day_number]

    def backup():
        files = []

        for i in listdir(f"{homepath}MyArchive/"):
            files.append(i)

        MyArchives = []

        metadata = {
            "Author": "EdwinRodger",
            "Name": "MyArchives",
            "Export Date": f"{now}",
        }

        data = {"Metadata": metadata, "MyArchives": MyArchives}

        with open(f"{homepath}Backups/{today}_backup.json", "w") as outfile:
            for fname in files:
                with open(f"{homepath}MyArchive/{fname}") as infile:
                    fname1 = fname.rstrip(".txt")
                    lines = infile.readlines()
                    title = lines[0]
                    listed_text = []
                    for line in lines[1:]:
                        listed_text.append(line)
                    text = " ".join(map(str, listed_text[0:]))
                    entry = {
                        "Date": f"{fname1}",
                        "Title": f"{title.rstrip()}",
                        "Text": f"{text.strip()}",
                    }
                    MyArchives.append(entry)
            dump(data, outfile, indent=4)

    try:
        if day == today_day:
            backup()
        else:
            pass
    except Exception as e:
        showerror("Weekly Export Error!", e)


def monday_backup():
    with open(f"{homepath}Textfiles/weekly_backup_day.txt", "w") as f:
        f.write("Monday")
    weekly_backup()


def tuesday_backup():
    with open(f"{homepath}Textfiles/weekly_backup_day.txt", "w") as f:
        f.write("Tuesday")
    weekly_backup()


def wednesday_backup():
    with open(f"{homepath}Textfiles/weekly_backup_day.txt", "w") as f:
        f.write("Wednesday")
    weekly_backup()


def thursday_backup():
    with open(f"{homepath}Textfiles/weekly_backup_day.txt", "w") as f:
        f.write("Thursday")
    weekly_backup()


def friday_backup():
    with open(f"{homepath}Textfiles/weekly_backup_day.txt", "w") as f:
        f.write("Friday")
    weekly_backup()


def saturday_backup():
    with open(f"{homepath}Textfiles/weekly_backup_day.txt", "w") as f:
        f.write("Saturday")
    weekly_backup()


def sunday_backup():
    with open(f"{homepath}Textfiles/weekly_backup_day.txt", "w") as f:
        f.write("Sunday")
    weekly_backup()


def no_backup():
    with open(f"{homepath}Textfiles/weekly_backup_day.txt", "w") as f:
        f.write("no backup day selected")
