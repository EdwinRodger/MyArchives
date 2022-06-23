from setup.folders_setup import folder_setup

from .image_setup import icon_download
from .update_setup import update


def setup():
    update()
    folder_setup()
    icon_download()
