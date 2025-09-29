import dataclasses
from typing import Tuple
from lesson_3.db_manager import DbManager


@dataclasses.dataclass
class Students:
    all_students = []

    def __init__(self, id: int, name: str, email: str, age: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.is_create = None
        self.is_update = None
        self.is_remove = None
        Students.all_students.append(self)

    @classmethod
    def get_all_students(cls) -> None:
        db_manager = DbManager()
        result = db_manager.select_all()
        for row in result:
            Students(*row)

    def convert_to_tuple(self) -> Tuple:
        return self.name, self.email, self.age, self.id

    @staticmethod
    def apply_changes():
        print(Students.all_students)
        print(Students.remove_students)
        print(Students.update_students)
        print(Students.create_students)
        print("Обновление базы данных выполнено")

    def __repr__(self):
        return "Students_" + str(self.id)

    def __str__(self):
        return (
            "\nИмя: "
            + self.name
            + "\nПочтовый адрес: "
            + self.email
            + "\nВозраст: "
            + str(self.age)
        )
