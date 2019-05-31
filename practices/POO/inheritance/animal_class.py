class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
class Cat(Animal):
    def purr(self):
        print("Purrr. . .")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "Brown")
print(fido.name, fido.color)
fido.bark()
