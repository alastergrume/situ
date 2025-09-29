import os
import sys
from PyQt5 import QtWidgets
import lesson_3.main_window_form as mw_fom
import lesson_3.second_window_form as sv_form
from lesson_3.model import Students


class MainWindow(QtWidgets.QMainWindow, mw_fom.Ui_MainWindow):
    def __init__(self, second_window):
        super().__init__()
        self.setupUi(self)
        self.create_list()
        self.second_window = second_window
        self.btnCreate.clicked.connect(self.create_values)
        self.btnUpd.clicked.connect(self.update_values)
        self.btnDel.clicked.connect(self.remove_values)

    def create_values(self):
        self.second_window.is_new = True
        self.second_window.lineEdit_name.clear()
        self.second_window.lineEdit_email.clear()
        self.second_window.lineEdit_age.clear()
        self.second_window.show()

    def update_values(self):
        self.second_window.is_new = False
        current_row = self.listWidget.currentRow()
        self.second_window.retranslateUi(
            self,
            Students.all_students[current_row].name,
            Students.all_students[current_row].email,
            str(Students.all_students[current_row].age),
        )
        self.second_window.show()

    def remove_values(self):
        current_row = self.listWidget.currentRow()
        remove_student = Students.all_students.pop(current_row)
        self.create_list()

    def create_list(self):
        self.listWidget.clear()
        for student in Students.all_students:
            self.listWidget.addItem(
                student.name + "\t" + student.email + "\t" + str(student.age)
            )

    def closeEvent(self, event):
        print("Окно закрывается")
        # TODO Нужно добавить проверку, если есть изменения, то сохранить и выйти
        reply = QtWidgets.QMessageBox.question(
            self, "Выход",
            "Форма содержит изменения. Сохранить и выйти?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if reply == QtWidgets.QMessageBox.No:
            event.ignore()
        else:
            Students.apply_changes()
            event.accept()


class SecondWindow(QtWidgets.QMainWindow, sv_form.Ui_MainWindow):
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
            Students(len(Students.all_students) + 1, name, email, str(age), is_create=True)


        else:
            current_row = main_window.listWidget.currentRow()
            Students.all_students[current_row].name = self.lineEdit_name.text()
            Students.all_students[current_row].email = self.lineEdit_email.text()
            Students.all_students[current_row].age = self.lineEdit_age.text()


        main_window.create_list()
        self.close()


def main():
    global main_window

    Students.get_all_students()
    app = QtWidgets.QApplication(sys.argv)
    second_window = SecondWindow()
    main_window = MainWindow(second_window)
    main_window.show()
    app.exec_()
