class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        pi = 3.14159
        return pi * (self.radio ** 2)

# Uso del programa
el_circulo = Circulo(7)
area = el_circulo.calcular_area()
print(f"El área del círculo con radio {el_circulo.radio} es: {area}")
