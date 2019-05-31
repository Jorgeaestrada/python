class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

rectangle = Rectangle(7, 8)

# Esta linea imprime un error:
# AttributeError: Rectangle instance has no attribute 'color'
print(rectangle.color)
