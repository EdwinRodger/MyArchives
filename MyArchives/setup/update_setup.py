# Python Libraries
from hashlib import sha224
from os.path import exists
from tkinter.messagebox import askyesnocancel
from urllib.request import Request, urlopen
from webbrowser import open_new_tab

# MyArchives Libraries
from .tasks import home_directory

homepath = home_directory()

# Setting the URL you want to monitor
url = Request(
    "https://api.github.com/repos/EdwinRodger/MyArchives/releases/latest",
    headers={"User-Agent": "Mozilla/5.0"},
)


# To perform a GET request and load the
# content of the website and store it in a var
def update():
    # To create and save the initial hash
    if not exists(f"{homepath}/Textfiles/versionhash.txt"):
        response = urlopen(url).read()
        currentHash = sha224(response).hexdigest()
        with open(f"{homepath}Textfiles/versionhash.txt", "w") as f:
            f.write(currentHash)
    else:
        try:
            with open(f"{homepath}Textfiles/versionhash.txt", "r") as f:
                currentHash = f.read()

            # Perform the get request
            response = urlopen(url).read()

            # Create a new hash
            newHash = sha224(response).hexdigest()

            # Check if new hash is same as the previous hash
            if newHash == currentHash:
                pass

            # If something changed in the hashes
            else:
                # notify
                upd = askyesnocancel(
                    title="Update Available!",
                    message="A new version of MyArchives has been released!\nDo you want to download it?\n\nYes = Will take you to download website\nNo = Will promt you when next update will be available\nCancel = Will prompt you next time you open MyArchives",
                )

                if upd == True or upd == False:
                    open_new_tab(
                        "https://github.com/EdwinRodger/MyArchives/releases/latest/"
                    )

                    # Again read the website
                    response = urlopen(url).read()

                    # Create a hash
                    currentHash = sha224(response).hexdigest()

                    with open(f"{homepath}Textfiles/versionhash.txt", "w") as f:
                        f.write(currentHash)
                
                else:
                    pass

        except Exception:
            pass
