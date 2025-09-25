from lesson_3.lesson_3 import DbManager
from lesson_3.model import Students

students = [
    ("Василий", "Вакуленко", 35),
    ("Josev", "Dowson", 65),
    ("Emele", "Backer", 96),
]

manager = DbManager()
db_students = manager.select_data()

students_obj = []
for student in students:
    students_obj.append(Students(*student))

print(students_obj)
