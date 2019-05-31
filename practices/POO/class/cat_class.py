class Cat:
    # Metodo comun a todas las clases en python.
    # es utilizado como un 'Constructor' de objetos.
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color, felix.legs)
print(rover.color, rover.legs)
print(stumpy.color, stumpy.legs)
