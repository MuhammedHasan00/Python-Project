from addRecord import *
from deleteRecord import *
from updateRecord import *
from readRecords import *
from report import *

def menuOptions():
    options  = 0
    while options not in ["1","2","3","4","5", "6"]:
        with open(r"dbMenu.txt") as menu:
            choices = menu.readlines()
        for line in choices:
            print(line, end = "")
        options = input("\nEnter a Main Menu Option: ")
        if options not in ["1","2","3","4","5", "6"]:
            print(f"{options} not a valid choice!")
    return options

def reportsMenuOptions():
    options = 0
    while options not in ["1","2","3","4","5"]:
        with open(r"dbRecordsMenu.txt") as menu:
            choices = menu.readlines()
        for line in choices:
            print(line, end = "")
        options = input("\nEnter a Records Menu Option: ")
        if options not in ["1","2","3","4","5"]:
            print(f"{options} not a valid choice!")
    return options

def reportsMenu():
    main = True

    while main:
        reportsMenu = reportsMenuOptions()
        if reportsMenu == "1":
            readRecords()
        elif reportsMenu == "2":
            genre()
        elif reportsMenu == "3":
            year()
        elif reportsMenu == "4":
            rating()
        else:
            main = False
    input("Press enter to exit the Reports Menu")
    return main

def mainMenu():
    main = True

    while main:
        mainMenu = menuOptions()
        if mainMenu == "1":
            addFilm()
        elif mainMenu == "2":
            deleteRecord()
        elif mainMenu == "3":
            updateRecord()
        elif mainMenu == "4":
            readRecords()
        elif mainMenu == "5":
            reportsMenu()
        else:
            main = False
    input("Press Enter to exit the Main Menu")
    return main


if __name__ == "__main__":
   mainMenu()