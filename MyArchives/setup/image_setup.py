## Importing Necessary Modules
from os.path import exists
from shutil  import copyfileobj # to save it locally
from tkinter import messagebox

from requests  import get # to get image from the web

from .tasks import home_directory

homepath = home_directory()


def icon_download():
    if not exists(f"{homepath}Diary.ico"):
        ## Set up the image URL and filename
        image_url = "https://raw.githubusercontent.com/EdwinRodger/MyArchives/main/.github/images/Diary.ico"
        filename = image_url.split("/")[-1]

        # Open the url image, set stream to True, this will return the stream content.
        r = get(image_url, stream=True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(f"{homepath}Diary.ico", "wb") as f:
                copyfileobj(r.raw, f)
        else:
            messagebox.showerror(
                "Image Download Error",
                "Cannot able to download Diary.ico at the moment\nPlease try again later",
            )
            quit()
    else:
        pass
