import json
import os

from setup.tasks import home_directory

newpath = home_directory()

metadata = {
    "metadata": {
        "application": "MyArchives",
        "version": "3.2.0",
        "author": "EdwinRodger",
    }
}


class file_setup:
    def pathtxt_setup():
        if not os.path.exists(f"{newpath}Textfiles\\path.txt"):
            with open(f"{newpath}Textfiles\\path.txt", "w") as f:
                f.write(str(newpath))

    def md_setup():
        if not os.path.exists(f"{newpath}metadata.json"):
            with open(f"{newpath}metadata.json", "w") as f:
                json.dump(metadata, f, indent=4)

        with open(f"{newpath}metadata.json", "r") as f:
            data = json.load(f)

        if metadata == data:
            pass
        else:
            with open(f"{newpath}metadata.json", "w") as f:
                json.dump(metadata, f)
