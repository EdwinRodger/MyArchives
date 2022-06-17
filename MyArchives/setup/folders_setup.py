import os

from setup.tasks import home_directory

newpath = home_directory()


def folder_setup():
    # Creates MyArchives folder in user directory
    # Creates MyArchive folder (to store entry files)
    if not os.path.exists(f"{newpath}MyArchive"):
        os.makedirs(f"{newpath}MyArchive")
    # Create Textfiles folder (to store software config files)
    if not os.path.exists(f"{newpath}Textfiles"):
        os.makedirs(f"{newpath}Textfiles")
