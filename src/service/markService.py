from model.student import Student
from model.mark import Mark


class MarksService(object):

    def __int__(self):
        self.students = dict()

    def add_student(self, name):
        self.students.update({name: Student(name)})

    def add_mark(self, student_name, subject_name, mark_value):
        mark = Mark(mark_value, subject_name)
        self.students[student_name].add_mark(mark)
