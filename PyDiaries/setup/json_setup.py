# Python file to create JSON file
import json
from setup.tasks import home_directory
import datetime

date = datetime.datetime.today()
_, path = home_directory()

try:
    with open(f"{path}Textfiles\json.txt", "r") as f:
        condition = int(f.read())
except:
    with open(f"{path}Textfiles\json.txt", "w") as f:
        f.write("0")
    with open(f"{path}Textfiles\json.txt", "r") as f:
        condition = int(f.read())

contents = {
    "metadata":{
        "application":"PyDiaries",
        "version":"v5.0",
        "dateUpdated":f"{date}"
    },
    "entries":{}
}


def setup_json():
    if condition==0:
        with open(f"{path}\\DiaryEntry.json", "w") as f:
            json.dump(contents, f, indent=4)
        with open(f"{path}Textfiles\json.txt", "w") as f:
            f.write("1")
    elif condition==1:
        pass