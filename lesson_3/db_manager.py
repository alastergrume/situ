import os
import logging
import sqlite3
from typing import List, Tuple
from lesson_3.db_connect import create_connection


logger = logging.getLogger(__name__)


class DbManager:

    def __init__(self):
        self._conn = self._get_connection()
        self._migrate()
        if os.environ["APP_ENV"] == "TEST" and not self.select_all():
            self._init_db_data()

    def _get_connection(self) -> sqlite3.Connection:
        return create_connection()

    def insert_data(self, rows: List) -> None:

        query = """
        INSERT INTO Students 
        (name, email, age) 
        VALUES (?, ?, ?);
        """
        if not rows:
            rows = []
        try:
            cursor = self._conn.cursor()
            cursor.executemany(query, rows)
            self._conn.commit()
            cursor.close()
            logger.info("Database is updated")
        except Exception as ex:
            logger.error(f"An error occurred: {ex}")
            self._conn.rollback()

    def select_all(self) -> List[Tuple[str, int]]:
        query = "SELECT id, name, email, age FROM Students;"
        cursor = self._conn.cursor()
        data = cursor.execute(query)
        response = data.fetchall()
        return response

    def remove_rows(self, row_id: int) -> None:
        query = f"DELETE FROM Students WHERE id={row_id};"
        try:
            cursor = self._conn.cursor()
            if row_id:
                cursor.execute(query)
                cursor.close()
                self._conn.commit()
        except Exception as ex:
            logger.error(f"Error remove rows from Database: {ex}")
            self._conn.rollback()

    def update_rows(self, rows: List[Tuple[str, int]]) -> None:
        query = """UPDATE Students 
                 SET name = ?, email = ?, age = ?
                 WHERE id = ?;"""
        try:
            cursor = self._conn.cursor()
            cursor.executemany(query, rows)
            cursor.close()
            self._conn.commit()
        except Exception as ex:
            logger.error(f"Error update rows: {ex}")
            self._conn.rollback()

    def _migrate(self) -> None:
        try:
            cursor = self._conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS Students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER
                )
                """
            )

            cursor.close()
            logger.debug("Migrations applied")
        except Exception as ex:
            logger.error(f"An error occurred: {ex}")
            self._conn.rollback()

    def _init_db_data(self):
        students = [
            ("Мария", "newuser@example.com", 28),
            ("Иван", "new@example.com", 30),
            ("Анна", "qwert@example.com", 25),
        ]
        self.insert_data(students)
