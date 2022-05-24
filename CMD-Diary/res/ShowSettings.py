def about():
    with open("textFiles/about.txt", "r") as abt:
        print("\n\n" + abt.read())
    wait = input("\n\nPress enter to continue...")


def contribution():
    with open("textFiles/contribution.txt", "r") as contri:
        print("\n\n" + contri.read())
    wait = input("\n\nPress enter to continue...")


def help():
    with open("textFiles/helpme.txt", "r") as helpmeh:
        print("\n\n" + helpmeh.read())
    wait = input("\n\nPress enter to continue...")


# Will use tkinter file dialogue feature to get folder path
"""
def change_path():
    with open("textFiles/path.txt", "r") as path:
        print(f"\n\n\n\nYour current save folder is: {path.read()}\n\n")
        print(" - If not already present, add a \ (back slash) at the end of the folder path")
        print(" - Type 'cancel' to exit without any changes\n\n")
    new_path = input("Enter new folder to save your entries: ")
    if new_path == "cancel" or new_path=="'cancel'":
        pass
    else:
        with open("textFiles/path.txt", "w") as f:
            f.write(str(f))
        print(f"Your new save folder is: {new_path}")
        wait = input("Press enter to continue...")
"""


def template():
    print("\n" * 5)
    tempt = input("Do you want a template to write your diary?(y/n)")
    if tempt == "y":
        with open("textFiles/template.txt", "w") as tt:
            tt.write("1")
        print("\n" * 5)
        text = input("Diary template ON")
    elif tempt == "n":
        with open("textFiles/template.txt", "w") as tt:
            tt.write("0")
        print("\n" * 5)
        text = input("Diary template OFF")
    else:
        print("\n" * 5)
        print("Enter on y or n (y = yes, n = no)")
        template()
