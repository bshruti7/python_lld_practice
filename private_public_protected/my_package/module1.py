
class MyClass:

    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary


if __name__ == "__main__":
    myclass_obj = MyClass("Anna", 30, 1000)
    print("My Class: ", myclass_obj.name, myclass_obj.age, myclass_obj.salary)
