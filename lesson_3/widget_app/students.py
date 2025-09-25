import sqlite3


class Students:
    all_students = []

    def __init__(self, id, name, email, age):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        # 0 - не трогали запись, 1 - изменили, 2 - удаляем
        self.flag = 0
        Students.all_students.append(self)

    def __str__(self):
        return (
            "\nИмя: "
            + self.name
            + "\nПочтовый адрес: "
            + self.email
            + "\nВозраст: "
            + str(self.age)
        )

    def set_age(self, new_age):
        if str(new_age).isdigit():
            self.age = new_age

    def convert_to_tuple(self):
        return (self.age, self.name)


# Устанавливаем соединение с базой данных
connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

# Выбираем всех пользователей
cursor.execute("SELECT * FROM Students;")
students = cursor.fetchall()

# Выводим результаты
for student in students:
    student_obj = Students(student[0], student[1], student[2], student[3])

connection.close()
