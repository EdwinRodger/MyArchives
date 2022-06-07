# Python file to create JSON file
import json
from setup.tasks import home_directory
import datetime

date = datetime.datetime.today()
_, path = home_directory()

contents = {
    "metadata":{
        "application":"PyDiaries",
        "version":"v5.0",
        "dateUpdated":f"{date}"
    },
    "entries":{}
}


def setup_json():
    with open(f"{path}\\DiaryEntry.json", "w") as f:
        json.dump(contents, f, indent=4)