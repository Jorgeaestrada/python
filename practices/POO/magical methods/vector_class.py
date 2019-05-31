class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Los metodos magicos son metodos especiales que tienen
# un doble guion bajo al principio y final de sus nombres
# conocidos como dunders en ingles
# crean funcionalidades que no pueden ser representados
# en un metodo regular

# SE USAN PARA SOBRECARGA DE OPERADORES
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
first = Vector2D(5, 7)
second = Vector2D(3, 9)

result = first + second
print(result.x, result.y)
