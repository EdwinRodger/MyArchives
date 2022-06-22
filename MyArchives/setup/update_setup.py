import hashlib
import os.path
from tkinter.messagebox import showinfo
from urllib.request import Request, urlopen
from webbrowser import open_new_tab

from .tasks import home_directory

newpath = home_directory()

# setting the URL you want to monitor
url = Request(
    "https://api.github.com/repos/EdwinRodger/MyArchives/releases/latest",
    headers={"User-Agent": "Mozilla/5.0"},
)


def updater():
    # again read the website
    response = urlopen(url).read()

    # create a hash
    currentHash = hashlib.sha224(response).hexdigest()

    with open(f"{newpath}Textfiles/versionhash.txt", "w") as f:
        f.write(currentHash)


# to perform a GET request and load the
# content of the website and store it in a var
def update():
    # to create and save the initial hash
    if not os.path.exists(f"{newpath}/Textfiles/versionhash.txt"):
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        with open(f"{newpath}Textfiles/versionhash.txt", "w") as f:
            f.write(currentHash)
    else:
        try:
            with open(f"{newpath}Textfiles/versionhash.txt", "r") as f:
                currentHash = f.read()

            # perform the get request
            response = urlopen(url).read()

            # create a new hash
            newHash = hashlib.sha224(response).hexdigest()

            # check if new hash is same as the previous hash
            if newHash == currentHash:
                pass

            # if something changed in the hashes
            else:
                # notify
                upd = showinfo(
                    title="Update Available!",
                    message="A new version of MyArchives has been released!\nDo you want to download it?",
                )
                if upd == True:
                    updater()
                    open_new_tab(
                        "https://github.com/EdwinRodger/MyArchives/releases/latest/"
                    )
                else:
                    updater()
        except Exception:
            pass
