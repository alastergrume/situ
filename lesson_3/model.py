import dataclasses

from lesson_3.db_manager import DbManager

@dataclasses.dataclass
class Students:
    all_students = []

    def __init__(self, id, name, email, age):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        Students.all_students.append(self)

    @classmethod
    def get_all_students(cls):
        db_manager = DbManager()
        result = db_manager.select_all()
        for row in result:
            Students(*row)


    def convert_to_tuple(self):
        return (self.age, self.name)


    def __str__(self):
        return (
                "\nИмя: "
                + self.name
                + "\nПочтовый адрес: "
                + self.email
                + "\nВозраст: "
                + str(self.age)
        )
