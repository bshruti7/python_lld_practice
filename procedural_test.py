from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    gender: str


def print_student(student: Student):

    print(student.name)
    print(student.age)
    print(student.gender)


if __name__ == "__main__":
    student1 = Student(name="John", age=18, gender="Male")
    print_student(student1)



