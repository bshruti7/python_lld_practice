class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.email = None

    # Python does not allow multiple init methods with same names
    @classmethod
    def init_with_email(cls, name, age, email):
        my_student = Student(name, age)
        my_student.email = email
        return my_student

    @classmethod
    def init_with_optional_name(cls, age, email, name=None):
        my_student = Student(name, age)
        my_student.email = email
        return my_student


if __name__=='__main__':
    st = Student("John", 50)
    print(st.name, st.age)

    st1 = Student.init_with_email("B", 45, 'b@gmail.com')
    print(st1.name, st1.age, st1.email)

    st2 = Student.init_with_optional_name(48, 'c@gmail.com')
    print(st2.name, st2.age, st2.email)



