# Python file to create JSON file
import json
from setup.tasks import home_directory
import datetime

date = datetime.datetime.today()
_, newapth = home_directory()

try:
    with open(f"{newapth}\\Textfiles\json.txt", "r") as f:
        condition = int(f.read())
except:
    with open(f"{newapth}\\Textfiles\json.txt", "w") as f:
        f.write("0")
    with open(f"{newapth}\\Textfiles\json.txt", "r") as f:
        condition = int(f.read())

contents = {
    "metadata":{
        "application":"MyArchives",
        "version":"v5.0",
        "dateUpdated":f"{date}"
    },
    "entries":[]
}


def setup_json():
    if condition==0:
        with open(f"{newapth}MyArchive.json", "w") as f:
            json.dump(contents, f, indent=4)
        with open(f"{newapth}Textfiles\json.txt", "w") as f:
            f.write("1")
    elif condition==1:
        pass