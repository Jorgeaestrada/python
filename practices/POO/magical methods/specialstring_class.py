# Solo funciona con python en su version 3+
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]

    def __truediv__(self, other):
        if (len(self.cont) > len(other.cont)):
            line = "=" * len(self.cont)
        else:
            line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello World!")
eggs = SpecialString("eggs")
# EL METODO TRUEDIV SE LLAMA DESDE ESTA LINEA
#print(spam / hello)
spam > eggs
