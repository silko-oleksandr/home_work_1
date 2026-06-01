#14.1
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old, Record book: {self.record_book}"


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def __str__(self):
        if not self.students:
            return "No students in the group"
        result = "Students in group:\n"
        for student in self.students:
            result += str(student) + "\n"
        return result.rstrip("\n")
#14.2
class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_max(self, max_value):
        self.max_value = max_value

    def set_min(self, min_value):
        self.min_value = min_value

    def set_current(self, current):
        self.current = current

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнутий мінімум")
        self.current -= 1

    def get_current(self):
        return self.current