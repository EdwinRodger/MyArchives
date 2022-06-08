from setup.tasks import home_directory
import os

_, newpath = home_directory()



# Command to create a MyArchives folder in User directory if not already exists
def setup_folder():
    
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    if not os.path.exists(f"{newpath}Textfiles\\"):
        os.makedirs(f"{newpath}Textfiles\\")
    with open(f"{newpath}Textfiles\\path.txt", "w") as homedir:
        homedir.write(newpath)