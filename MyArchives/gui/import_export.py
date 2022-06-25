from shutil import make_archive
import zipfile
from tkinter.filedialog import askdirectory, askopenfile
from tkinter import filedialog
from home_dir import home_directory

homepath = home_directory()

def export_zip():
    save_dir = askdirectory()
    make_archive(f"{save_dir}/MyArchives", 'zip', f"{homepath}MyArchive")

def import_zip():
    zip_dir = filedialog.askopenfilename() # Change This
    # print(zip_dir)
    with zipfile.ZipFile(zip_dir, 'r') as zip_ref:
        zip_ref.extractall(f"{homepath}/MyArchive")


