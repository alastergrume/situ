import logging
from lesson_3.db_connect import create_connection
from lesson_3.migrations import Init_DB


logger = logging.getLogger(__name__)


class DbManager:

    def __init__(self):
        self.conn = self.get_connection()


    def get_connection(self):
        return create_connection()


    def insert_data(self, rows: set):

        query = """INSERT INTO Students (
        first_name, last_name, age) 
        VALUES (?, ?, ?);
        """
        if not rows:
            rows = []
        try:
            cursor = self.conn.cursor()
            cursor.executemany(query, rows)
            self.conn.commit()
            cursor.close()
            logger.info("Database is updated")
        except Exception as ex:
            logger.error(f"An error occurred: {ex}")
            self.conn.rollback()


    def select_data(self):
        query = "SELECT id, first_name, last_name, age FROM Students;"
        cursor = self.conn.cursor()
        data = cursor.execute(query)
        response = data.fetchall()
        return response


    def remove_rows(self, id: int):
        query = f"DELETE FROM Students WHERE id={id};"
        try:
            cursor = self.conn.cursor()
            if id:
                cursor.execute(query)
                cursor.close()
                self.conn.commit()
        except Exception as ex:
            logger.error(f"Error remove rows from Database: {ex}")
            self.conn.rollback()


    def migrate(self):
        init_db = Init_DB()
        init_db.init_migrations()
        print("Migrations applied")



