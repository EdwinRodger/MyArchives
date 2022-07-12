from .folders_setup import folder_setup
from .image_setup import icon_download
from .update_setup import update
from .file_setup import theme_setup


def setup():
    folder_setup()
    update()
    icon_download()
    theme_setup()
