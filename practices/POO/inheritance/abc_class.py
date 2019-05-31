# El uso de super() para llamar al metodo de la superclase
# solo funciona usando python en su version 3

class A:
    # Uso de constructor opcional si no voy
    # a utilizar argumentos
    def method(self):
        print("A method")

    def spam(self):
        print(1)

class B(A):
    def another_method(self):
        print("B method")

    def spam(self):
        print(2)
        super().spam()

class C(B):
    def third_method(self):
        print("C method")

    def spam(self):
        print(3)
        super().spam()

c = C()
c.method()
c.another_method()
c.third_method()

C().spam()
