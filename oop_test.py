
class Student:
    name: str
    age: int
    gender: str

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def print_student(self):
        print(self.name)
        print(self.age)
        print(self.gender)


if __name__ == "__main__":
    student2 = Student("John", "18", "Male")
    student2.print_student()