from private_public_protected.my_package import module1 as m1


if __name__ == "__main__":

    other_obj = m1.MyClass("Bob", 40, 2000)

    # cleaner python way of accessing the attributes. MyClass handles the access controls with appropriate setters
    print(other_obj.name)
    print(other_obj.age)
    print(other_obj.salary)

    # incorrect approach that is not recommended. But it proves that Python does not have strict access controls like
    # Java
    print(other_obj.name)
    print(other_obj._age)
    print(other_obj._MyClass__salary)

