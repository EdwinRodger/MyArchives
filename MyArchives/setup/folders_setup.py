import os
from setup.tasks import home_directory

newpath = home_directory()

class folder_setup():
    # Makes MyArchives folder if not exists already
    def myarchives():
        if not os.path.exists(newpath):
            os.makedirs(newpath)
    
    def myarchive():
        if not os.path.exists(f"{newpath}MyArchive"):
            os.makedirs(f"{newpath}MyArchive")

    # Makes Textfiles folder in MyArchives if not exists already
    def textfiles():
        if not os.path.exists(f"{newpath}Textfiles"):
            os.makedirs(f"{newpath}Textfiles")