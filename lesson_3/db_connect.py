import sqlite3


def create_connection():
    return sqlite3.connect("my_database.db")
