import os

from setup.tasks import home_directory

homepath = home_directory()


def folder_setup():
    # Creates MyArchives folder in user directory
    # Creates MyArchive folder (to store entry files)
    if not os.path.exists(f"{homepath}MyArchive"):
        os.makedirs(f"{homepath}MyArchive")
    # Create Textfiles folder (to store software config files)
    if not os.path.exists(f"{homepath}Textfiles"):
        os.makedirs(f"{homepath}Textfiles")
