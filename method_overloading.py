class MultiAdd:

    def add(self, a, b=0):
        return a + b


if __name__ == "__main__":

    madd = MultiAdd()
    print(madd.add(5))
    print(madd.add(5, 2))


    # Python does not allow multiple add methods with different arguments types and number

