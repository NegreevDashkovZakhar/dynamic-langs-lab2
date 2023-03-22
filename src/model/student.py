from model.mark import Mark


class Student(object):

    def __int__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark: Mark):
        self.marks.append(mark)

    def get_average(self):
        return 5
