from functions import system, menu
from os import system as osSystem, name as osName


def main():
    system.checkSystem()  # Needed to initiate colorama in case we are using Windows
    osSystem('cls' if osName == 'nt' else 'clear')
    print(system.sysMsg + 'Seaching database...')
    databaseConnection = system.checkDatabase()  # Call database connection
    menu.userMenu()


main()
