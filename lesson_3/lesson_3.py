
from lesson_3.db_connect import create_connection


class DbManager:

    def __init__(self):
        self.conn = self.get_connection()

    def get_connection(self):

        return create_connection()


    def insert_data(self, raws: set):


        query = """INSERT INTO Students (
        first_name, last_name, age) 
        VALUES (?, ?, ?)
        """
        if not raws:
            raws = []
        cursor = self.conn.cursor()
        cursor.executemany(query, raws)
        cursor.commit()
        cursor.close()

    def select_data(self):

        query = "SELECT id, first_name, last_name, age FROM Students;"
