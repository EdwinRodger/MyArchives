from shutil import make_archive
import zipfile
from tkinter.filedialog import askdirectory, askopenfile
from tkinter import filedialog
from .home_dir import home_directory
from os import listdir

homepath = home_directory()

def export_zip():
    save_dir = askdirectory()
    make_archive(f"{save_dir}/MyArchives", 'zip', f"{homepath}MyArchive")

def import_zip():
    zip_dir = filedialog.askopenfilename()
    # print(zip_dir)
    with zipfile.ZipFile(zip_dir, 'r') as zip_ref:
        zip_ref.extractall(f"{homepath}/MyArchive")

def export_txt():
    save_dir = askdirectory()
    files = []
    for i in listdir(f"{homepath}MyArchive/"):
        files.append(i)

    with open(f'{save_dir}/export.txt', 'w') as outfile:
        outfile.write("MyArchives\n\n\n\n")
        for fname in files:
            with open(f'{homepath}MyArchive/{fname}') as infile:
                fname1 = fname.rstrip(".txt")
                outfile.write(f"{fname1}")
                outfile.write("\n")
                outfile.write(infile.read())
                outfile.write("-----\n\n")
