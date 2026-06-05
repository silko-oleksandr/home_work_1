class GroupLimitError(Exception):
    pass

class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupLimitError("Too many students")
        self.students.append(student)