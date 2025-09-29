from dataclasses import dataclass
from lesson_3.db_manager import DbManager


@dataclass
class Students:
    all_students = []

    def __init__(
        self, id: int, name: str, email: str, age: str, is_update: str = None
    ) -> None:

        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.is_update = is_update
        self.remove_list = []
        Students.all_students.append(self)

    @classmethod
    def get_all_students(cls) -> list:
        db_manager = DbManager()
        result = db_manager.select_all()
        for row in result:
            Students(*row)
        return Students.all_students

    @staticmethod
    def formating_lists():
        remove_list = []
        update_list = []
        insert_list = []
        for student in Students.all_students:
            if student.is_update == "create":
                insert_list.append((student.name, student.email, student.age))
            elif student.is_update == "update":
                update_list.append(
                    (student.name, student.email, student.age, student.id)
                )
            elif student.is_update == "delete":
                remove_list.append(student.id)
        return remove_list, update_list, insert_list

    @staticmethod
    def apply_changes() -> None:
        db_manager = DbManager()
        remove_list, update_list, insert_list = Students.formating_lists()
        db_manager.update_rows(update_list)
        db_manager.insert_data(insert_list)
        db_manager.remove_rows(remove_list)

    def __str__(self) -> str:
        return (
            "\nИмя: "
            + self.name
            + "\nПочтовый адрес: "
            + self.email
            + "\nВозраст: "
            + str(self.age)
        )
