import os
import sys
from PyQt5 import QtWidgets
import lesson_3.form1 as form1
import lesson_3.form2 as form2
from lesson_3.model import Students


class ExampleApp(QtWidgets.QMainWindow, form1.Ui_MainWindow):
    def __init__(self, window2):
        super().__init__()
        self.setupUi(self)
        self.create_list()
        self.window2 = window2
        self.btnCreate.clicked.connect(self.create_values)
        self.btnUpd.clicked.connect(self.update_values)
        self.btnDel.clicked.connect(self.remove_values)

    def create_values(self):
        self.window2.is_new = True
        self.window2.lineEdit_name.clear()
        self.window2.lineEdit_email.clear()
        self.window2.lineEdit_age.clear()
        self.window2.show()

    def update_values(self):
        self.window2.is_new = False
        current_row = self.listWidget.currentRow()
        self.window2.retranslateUi(
            self,
            Students.all_students[current_row].name,
            Students.all_students[current_row].email,
            str(Students.all_students[current_row].age),
        )
        self.window2.show()

    def remove_values(self):
        current_row = self.listWidget.currentRow()
        Students.all_students.pop(current_row)
        self.create_list()

    def create_list(self):
        self.listWidget.clear()
        for student in Students.all_students:
            self.listWidget.addItem(
                student.name + "\t" + student.email + "\t" + str(student.age)
            )


class ExampleApp2(QtWidgets.QMainWindow, form2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_save.clicked.connect(self.save_values)
        self.is_new = True

    def save_values(self):
        if self.is_new:
            name = self.lineEdit_name.text()
            email = self.lineEdit_email.text()
            age = self.lineEdit_age.text()
            Students(
                len(Students.all_students) + 1, name, email, str(age)
            )
        else:
            current_row = window.listWidget.currentRow()
            Students.all_students[current_row].name = self.lineEdit_name.text()
            Students.all_students[current_row].email = (
                self.lineEdit_email.text()
            )
            Students.all_students[current_row].age = self.lineEdit_age.text()

        window.create_list()
        self.close()


def main():
    global window

    Students.get_all_students()
    app = QtWidgets.QApplication(sys.argv)
    window2 = ExampleApp2()
    window = ExampleApp(window2)
    window.show()
    app.exec_()