from lesson_3.db_connect import create_connection


class Init_DB:

    def __init__(self):
        self.conn = create_connection()

    def create_db(self):

            cursor = self.conn.cursor()

            query = """
                CREATE TABLE IF NOT EXISTS Students (
                id INTEGER PRIMARY KEY,
                first_name STRING UNIQUE NOT NULL,
                last_name STRING UNIQUE NOT NULL,
                age DATE UNIQUE NOT NULL
                )        
                """

            cursor.execute(query)
            cursor.close()
