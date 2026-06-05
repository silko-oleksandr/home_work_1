# main.py
from group import Group, GroupLimitError
from student import Student

group = Group("P01")

for i in range(11):
    try:
        group.add_student(Student(name=f"Name{i}", surname=f"Surname{i}"))
    except GroupLimitError as e:
        print(e)