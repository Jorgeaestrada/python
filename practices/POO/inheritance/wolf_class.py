# Superclase
class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark():
        print("Grrr. . .")
# Subclase
class Dog(Wolf):
    def bark(self):
        print("Woof!")

husky = Dog("Max", "Gray")
husky.bark()
