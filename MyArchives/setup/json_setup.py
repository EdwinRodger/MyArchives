# Python file to create JSON file
import os.path
import json
from setup.tasks import home_directory
from datetime import datetime, date

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

date = date.today()
_, newapth = home_directory()



metadata = {
    "metadata":{
        "application":"MyArchives",
        "version":"v5.0",
        "author":"EdwinRodger"
    }
}

entries = {
    "entries":[
        {
            "date": f"{date}",
            "time": f"{current_time}",
            "title": "Some Title",
            "text": "Some Text"
        }
    ]
}

def setup_json():
    with open(f"{newapth}metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)
    if not os.path.exists(f"{newapth}MyArchives.json"):
        with open(f"{newapth}MyArchives.json", "w") as f:
            json.dump(entries, f, indent=4)