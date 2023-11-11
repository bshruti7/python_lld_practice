class Student:

    def __init__(self, name, problems_solved):
        self.name = name
        self.problems_solved = problems_solved

    def solve_problems(self, problems_solved):
        self.problems_solved += problems_solved
        print(f'{self.name} solved total of {self.problems_solved} problems')


if __name__ == "__main__":
    adam = Student("Adam", 5)
    adam.solve_problems(2)