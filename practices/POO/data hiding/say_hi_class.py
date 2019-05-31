class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def sayHi(cls):
        print("Hi")

person = Person.sayHi("Jorge")
