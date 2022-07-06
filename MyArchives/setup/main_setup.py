from .folders_setup import folder_setup
from .image_setup import icon_download
from .update_setup import update
from .file_setup import font_file


def setup():
    folder_setup()
    update()
    icon_download()
    font_file()
