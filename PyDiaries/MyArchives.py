from gui.MainUI import main
from setup.json_setup import setup_json
from setup.folder_setup import setup_folder



if __name__=="__main__":
    setup_folder()
    setup_json()
    main()