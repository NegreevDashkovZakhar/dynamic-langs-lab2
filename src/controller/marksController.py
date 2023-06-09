import API_KEY
from service.markService import MarksService


class MarksController(object):

    def __init__(self):
        self.service = MarksService()
        self.parent_commands = {
            'все': self.service.get_student_all,
            'ср': self.service.get_student_averages
        }

    def parse_message(self, message: str):
        words = message.split(",")
        if words[0] == API_KEY.teacher_key_word:
            if len(words) < 4:
                return "Ошибка, недостаточно данных"
            name = words[1]
            subject_name = words[2]
            mark_value = words[3]
            self.service.add_mark(name, subject_name, mark_value)
            return "Оценка успешно добавлена"
        else:
            name = words[0]
            return self.parent_commands[words[1]](name)
