from .image_setup import icon_download
from setup.files_setup import file_setup
from setup.folders_setup import folder_setup


def setup():
    folder_setup.myarchive()
    folder_setup.textfiles()
    file_setup.md_setup()
    file_setup.pathtxt_setup()
    icon_download()
