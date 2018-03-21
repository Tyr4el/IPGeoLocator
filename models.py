import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    # Create a database connection to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # Create the table if it doesn't exist
    create_table(cursor)

    return conn, cursor


def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (ip text, country text, city text)''')
