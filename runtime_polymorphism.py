class User:

    def __init__(self, name):
        print("Called the init method of User class")
        self.name = name

    def login(self):
        print("User logged in is (user login method): ", self.name)


class Instructor(User):

    def __init__(self, name):
        print("Called the init method of Instructor class")
        super().__init__(name)

    def login(self):
        print("User logged in is (instructor login method): ", self.name)

    def teach(self, subjects):
        print(self.name, " teaches ", subjects)


if __name__ == "__main__":
    user1 = User("Anna")
    user1.login()
    # Python does not flag the below error until runtime,
    # but PyCharm may do static code analysis and identify problems before running
    # user1.teach("English") # AttributeError: 'User' object has no attribute 'teach'

    instructor1 = Instructor("Pam")
    instructor1.login()
    instructor1.teach("Math")

    # since type is determined at runtime, no concept of typecasting user2 = Instructor(--) like in Java
    # because at runtime



