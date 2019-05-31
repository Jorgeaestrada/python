class Student:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hi from " + self.name)


student = Student("Bob")
student1 = Student("Amy")
print(student.name)
student1.sayHi()
