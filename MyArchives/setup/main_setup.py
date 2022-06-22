from setup.files_setup import file_setup
from setup.folders_setup import folder_setup

from .image_setup import icon_download
from .update_setup import update


def setup():
    folder_setup()
    file_setup.md_setup()
    file_setup.pathtxt_setup()
    icon_download()
    update()
