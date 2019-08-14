from B import B

class C(B):
    def metodoC(self, x:int) -> str:
        return self.str * x

"""test"""

str = input("Escribe una palabra ")
x = int(input('Escribe un numero '))

c = C(str)
print(c.metodoC(x))
