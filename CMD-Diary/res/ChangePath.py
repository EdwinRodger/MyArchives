# Currently changing path is in progress, this code is a place holder for future code


def read_path():
    with open("textFiles/path.txt", "r") as f:
        wait = input("\n\n\n\nDiary path is " + f.read())
