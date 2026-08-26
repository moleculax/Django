import numpy as np

class Matriz():
    def funMatriz(self):
        self.lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.matriz = np.array(self.lista)
        print("matriz:\n", self.matriz)
        # TAMBIEN PUEDE SER
        matriz2 = np.matrix(self.lista)
        print("matriz2:\n", matriz2)
        # MATEMATICAS
        sqrt = np.sqrt(self.lista)
        print("sqrt:\n", sqrt)
        mean = np.mean(self.lista)
        print("mean:\n", mean)
        sum = np.sum(self.lista)
        print("sum:\n", sum)
        max = np.max(self.lista)
        print("max:\n", max)
        min = np.min(self.lista)
        print("min:\n", min)
        # OPERACIONES
        suma = self.matriz + 10
        print("suma:\n", suma)
        resta = self.matriz - 10
        print("resta:\n", resta)
        multiplicacion = self.matriz * 10
        print("multiplicacion:\n", multiplicacion)
        division = self.matriz / 10
        print("division:\n", division)



response = Matriz()
response.funMatriz()

class SumaMatriz():
    def suma(self):
        self.lista1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.lista2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        self.matriz1 = np.array(self.lista1)
        self.matriz2 = np.array(self.lista2)
        print("matriz1:\n", self.matriz1)
        print("matriz2:\n", self.matriz2)
        suma = self.matriz1 + self.matriz2
        print("suma:\n", suma)

response2 = SumaMatriz()
response2.suma()

class RestaMatriz():
    def resta(self):
        self.lista1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.lista2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        self.matriz1 = np.array(self.lista1)
        self.matriz2 = np.array(self.lista2)
        print("matriz1:\n", self.matriz1)
        print("matriz2:\n", self.matriz2)
        resta = np.subtract(self.lista1, self.lista2)
        print("resta:\n", resta)

response3 = RestaMatriz()
response3.resta()

class Transpuesta():
    def transpuestMatriz(self):
        self.lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.matriz = np.array(self.lista)
        print("matriz:\n", self.matriz)
        transpuesta = np.transpose(self.matriz)
        print("transpuesta:\n", transpuesta)

response4 = Transpuesta()
response4.transpuestMatriz()