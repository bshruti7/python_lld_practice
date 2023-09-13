class User:

    def __init__(self, username):
        self.username = username

    def login(self):
        print("Logged in user as User" + self.username)


class Instructor(User):

    def login(self):
        print("Logged in user as Instructor " + self.username)


class Mentor(User):
    # since login method is not defined, when the login() method is called for an instance of Mentor,
    # it calls the login() method for parent class - User
    pass

class TA(User):
    def login(self):
        print("Logged in user as TA " + self.username)


user = User("Shruti")
user.login()

user1 = Instructor("Shruti")
user1.login()

user2 = Mentor("Shruti")
user2.login()

user3 = TA("Shruti")
user3.login()