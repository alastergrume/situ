

class Students:
    all_students = []

    def __init__(self, id, first_name, last_name, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Students.all_students.append(self)


    def __str__(self):
        return f"Student id {self.id} Last Name {self.last_name}, First Name {self.first_name}, Age {self.age}"

