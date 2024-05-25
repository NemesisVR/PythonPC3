import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "Sobre el origen"
    
    def vector(self, segundo_punto):
        dx = segundo_punto.x - self.x
        dy = segundo_punto.y - self.y
        return Punto(dx, dy)
    
    def distancia(self, segundo_punto):
        dx = segundo_punto.x - self.x
        dy = segundo_punto.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        print(f"La distancia entre {self} y {segundo_punto} es: {distancia}")

# Uso de la clase "Punto"
p1 = Punto(-6, 9)
p2 = Punto(3, 5)

print("Coordenadas de p1:", p1)
print("Cuadrante de p1:", p1.cuadrante())
print("Vector de p1 a p2:", p1.vector(p2))
p1.distancia(p2)
