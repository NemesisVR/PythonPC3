class Rectangulo:
    def __init__(self, largo, ancho):
        if largo <= 0 or ancho <= 0:
            raise ValueError("El largo y el ancho deben ser valores positivos.")
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

# Uso del programa
try:
    el_rectangulo = Rectangulo(12, 6)
    area = el_rectangulo.calcular_area()
    print(f"El área del rectángulo con largo {el_rectangulo.largo} y ancho {el_rectangulo.ancho} es: {area}")
except ValueError as e:
    print(e)
