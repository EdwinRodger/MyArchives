from shutil import make_archive
import zipfile
from tkinter.filedialog import askdirectory, askopenfilename
from .home_dir import home_directory
from os import listdir

homepath = home_directory()


def export_zip():
    save_dir = askdirectory(title="Select folder to save zip file", mustexist=True)
    make_archive(f"{save_dir}/MyArchives-Export", "zip", f"{homepath}MyArchive")


def import_zip():
    zip_dir = askopenfilename(
        title="Select A .zip File To Import",
        filetypes=(("zip files", "*.zip"), ("all files", "*.*")),
    )
    # print(zip_dir)
    with zipfile.ZipFile(zip_dir, "r") as zip_ref:
        zip_ref.extractall(f"{homepath}/MyArchive")


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
