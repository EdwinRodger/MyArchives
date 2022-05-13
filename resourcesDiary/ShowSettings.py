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