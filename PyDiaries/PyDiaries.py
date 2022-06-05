from gui.MainUI import main
from setup.database_setup import database
from setup.folder_setup import folder



if __name__=="__main__":
    folder()
    database()
    main()