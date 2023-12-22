
# make variables private
# Prevent direct instantiation of Student class
#

class Student:

    class __Builder:

        def __init__(self):
            self._name = None
            self._age = None

        def get_name(self):
            return self._name

        def set_name(self, _name):
            self._name = _name
            return self

        def get_age(self):
            return self._age

        def set_age(self, _age):
            self._age = _age
            return self

        def __str__(self):
            return f"{self._name}, {self._age}"

        def build(self):
            if self.get_age() > 18:
                raise Exception('Age is too high!')

            student = Student(self)
            student._name = self.get_name()
            student._age = self.get_age()
            return student

    def __init__(self, __builder):
        if not isinstance(__builder, Student.__Builder):
            raise Exception("Cannot create Student instance without using Student.build()")

    def __str__(self):
        return f"{self._name}, {self._age}"

    @staticmethod
    def get_builder():
        builder_obj = Student.__Builder()
        return builder_obj


student_obj = Student.get_builder().set_age(12).set_name("ABC").build()
print(type(student_obj))
print(student_obj)

# AttributeError: type object 'Student' has no attribute 'Builder'
# direct_student_builder = Student.Builder()
# Directly trying to instantiate Student should not work
#student_direct_obj = Student(direct_student_builder)
#print(type(student_obj))

# Incorrect route still possible. not recommended
student3 = Student(Student.get_builder().set_age(15).set_name("Cara"))
student3.name = "Cara"
student3.age = 45
print(student3)








