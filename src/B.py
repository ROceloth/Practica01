from A import A

class B(A):
    def metodoB(self, palabra):
        return self.str + ' ' + palabra

b = B('clase 2')
print(b.metodoB('hola'))
