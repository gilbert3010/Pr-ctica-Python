class Ropa:
    def __init__(self):
        self.marca = "Traki"
        self.talla = "M"
        self.color = "Azul"
        
camisa = Ropa()
print(camisa.marca)
print(camisa.talla)
print(camisa.color)

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2

calcular = Calculadora(10, 2)
print(calcular.suma)