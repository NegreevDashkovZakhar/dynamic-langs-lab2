from model.student import Student
from model.mark import Mark


class MarksService(object):

    def __init__(self):
        self.students_dict = dict()
        self.add_mark('Захар', 'История', 5)
        self.add_mark('Захар', 'История', 4)

    def add_student(self, name):
        self.students_dict.update({name: Student(name)})

    def add_mark(self, student_name, subject_name, mark_value):
        mark = Mark(mark_value, subject_name)
        if student_name not in self.students_dict:
            self.add_student(student_name)
        self.students_dict[student_name].add_mark(mark)

    def get_student_all(self, student_name):
        try:
            return self.students_dict.get(student_name).get_all()
        except:
            return "Ой, кажется такой студент еще не был добавлен. Обратитесь к администратору системы."

    def get_student_averages(self, student_name):
        try:
            return self.students_dict.get(student_name).get_averages()
        except:
            return "Ой, кажется такой студент еще не был добавлен. Обратитесь к администратору системы."
