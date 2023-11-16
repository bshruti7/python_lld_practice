import copy


class Performance:
    marks: int
    psp: float

    def __init__(self, marks, psp):
        self.marks = marks
        self.psp = psp


class Student:
    name: str
    age: int
    problems_solved: int

    performance: Performance

    def __init__(self, name, age, problems_solved, performance):
        self.name = name
        self.age = age
        self.problems_solved = problems_solved
        self.performance = performance

    def create_copy(self, other_student):
        self.name = other_student.name
        self.age = other_student.age
        self.problems_solved = other_student.problems_solved

        return Student(other_student.name, other_student.age, other_student.problems_solved, Performance(other_student.performance))


if __name__ == "__main__":
    p1 = Performance(100, 67.1)
    s1 = Student("John", 18, 50, p1)

    # shallow copy
    s2 = copy.copy(s1)
    print(s1.name, s1.age, s1.problems_solved, s1.performance.marks, s1.performance.psp)
    s2.performance.marks = 200
    print(s1.name, s1.age, s1.problems_solved, s1.performance.marks, s1.performance.psp)

    # deep copy
    s3 = copy.deepcopy(s1)
    s3.performance.marks = 300
    print(s1.name, s1.age, s1.problems_solved, s1.performance.marks, s1.performance.psp)
    print(s3.name, s3.age, s3.problems_solved, s3.performance.marks, s3.performance.psp)













