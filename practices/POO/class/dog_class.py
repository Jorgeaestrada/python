# Los atributos de clase son compartidos por
# todas las instancias de una clase

class Dog:
    # Las clases tambien pueden tener atributos de clase
    # pueden ser accedidos desde la instancia de una
    # clase o de la clase misma
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Metodo ladrar
    def bark(self):
        print("Woof!")

# Creamos objeto de tipo "Dog"
fido = Dog("fido", "brown")
# Accedido desde la instancia de una clase
print(fido.name, fido.legs)
# Accedido desde la clase misma
print(Dog.legs)
fido.bark()
