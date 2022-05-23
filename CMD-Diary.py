import os.path

# newpath command to create a CMD-Diary folder in Programfiles if not already exists

newpath = 'C:\\CMD-Diary\\'
if not os.path.exists(newpath):
    os.makedirs(newpath)

if __name__=="__main__":
    from res import DiaryEntry
    from res import UserInterface