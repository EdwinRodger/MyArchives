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
        print("Enter y or n (y = yes, n = no)")
        template()
