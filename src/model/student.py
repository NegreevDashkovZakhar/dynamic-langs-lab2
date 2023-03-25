import statistics

from model.mark import Mark


class Student(object):

    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark: Mark):
        self.marks.append(mark)

    def get_all(self):
        result = "Оценки ученика"
        mark_rows = dict()
        for mark in self.marks:
            try:
                last_row_value = mark_rows[mark.subject_name]
                mark_rows.update({mark.subject_name: "{} {}".format(last_row_value, mark.value)})
            except:
                mark_rows.update({mark.subject_name: "{}: {}".format(mark.subject_name, mark.value)})

        for row in mark_rows:
            result += "\n{}".format(mark_rows[row])
        return result

    def get_averages(self):
        result = "Оценки ученика"
        mark_rows = dict()

        for mark in self.marks:
            try:
                last_row_value = mark_rows[mark.subject_name]
                mark_rows.update({mark.subject_name: "{} {}".format(last_row_value, mark.value)})
            except:
                mark_rows.update({mark.subject_name: "{}".format(mark.value)})

        for row in mark_rows:
            string_marks = mark_rows[row]
            marks_array = [int(mark) for mark in string_marks.split(" ")]
            average = round(sum(marks_array) / len(marks_array), 3)
            result += "\n{}: {}".format(row, average)
        return result
