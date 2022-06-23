import json
import os

from setup.tasks import home_directory

homepath = home_directory()

metadata = {
    "metadata": {
        "application": "MyArchives",
        "version": "3.2.0",
        "author": "EdwinRodger",
    }
}


class file_setup:
    def pathtxt_setup():
        if not os.path.exists(f"{homepath}Textfiles\\path.txt"):
            with open(f"{homepath}Textfiles\\path.txt", "w") as f:
                f.write(str(homepath))

    def md_setup():
        if not os.path.exists(f"{homepath}metadata.json"):
            with open(f"{homepath}metadata.json", "w") as f:
                json.dump(metadata, f, indent=4)

        with open(f"{homepath}metadata.json", "r") as f:
            data = json.load(f)

        if metadata == data:
            pass
        else:
            with open(f"{homepath}metadata.json", "w") as f:
                json.dump(metadata, f)
