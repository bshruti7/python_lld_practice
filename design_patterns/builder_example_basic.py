class Student:

    def __new__(cls, builder):
        if builder.get_age() > 18:
            raise Exception('Age is too high!')
        self = super().__new__(Student)
        print(id(self))
        return self

    def __init__(self, builder):
        print(id(self), "Init")
        self.name = builder.get_name()
        self.age = builder.get_age()

    def __str__(self):
        return f"{self.name}, {self.age}"


class Builder:

    def __init__(self):
        self.name = None
        self.age = None
        self.email = None
        self.phonenumber = None


    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

# Basic method of creating builder object and passing to Student
builder_obj = Builder()
builder_obj.set_age(15)
builder_obj.set_name("Shruti")
# print(builder_obj)
student = Student(builder_obj)
print(student)









