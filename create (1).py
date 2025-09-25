import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

# Добавляем нового пользователя
cursor.executemany('INSERT INTO Students (name, email, age) VALUES (?, ?, ?)',
               [('Мария', 'newuser@example.com', 28),
                                 ('Иван', 'new@example.com', 30),
                                ('Анна', 'qwert@example.com', 25)])

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()