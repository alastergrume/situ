import sqlite3

class Students():
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
    return '\nИмя: ' + self.name + \
           '\nПочтовый адрес: ' + self.email + \
           '\nВозраст: ' + str(self.age)
  def set_age(self, new_age):
    if str(new_age).isdigit():
      self.age = new_age
  def convert_to_tuple(self):
    return (self.age, self.name)

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Выбираем всех пользователей
cursor.execute('SELECT * FROM Students ')
students = cursor.fetchall()

# Выводим результаты
for student in students:
  print(student)
  student_obj = Students(student[0],
                         student[1],
                         student[2],
                         student[3])

for student in Students.all_students:
  print(student)

# Изменение Мария -> 30

update_data = []

for student in Students.all_students:
  if student.name == 'Мария':
    student.set_age(30)
    student.flag = 1
    update_data.append(student.convert_to_tuple())

# Удалим Анна

delete_data = []

for student in Students.all_students:
  if student.name == 'Анна' and student.flag != 2:
    #if student.flag == 1:
      # удалить запись из update_data
    student.flag = 2
    delete_data.append(student.convert_to_tuple())

print(update_data)

print(delete_data)

# Обновляем возраст пользователя "newuser"
cursor.executemany('UPDATE Students SET age = ? WHERE name = ?', update_data)

# Удаление


connection.commit()

connection.close()