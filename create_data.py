import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(sqlite3.version)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection("/home/inisoft/Documents/apistar_example/sqlite_user.db")
