from . import system


def load_user():
    pass


def create_user():
    pass


def delete_user():
    pass


def show_users():
    result = system.exec_query(
        system.database, "SELECT username, points FROM users")
    for row in result:
        print("User: {0}".format(row[0]), end="\t")
        print("Points: {0}".format(row[1]))
