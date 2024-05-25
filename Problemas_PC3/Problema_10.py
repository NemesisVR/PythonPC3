def calcular_area_circulo(radio):
    from Problema_3 import Circulo
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo con radio {radio} es: {area}")

def calcular_area_rectangulo(largo, ancho):
    from Problema_4 import Rectangulo
    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    print(f"El área del rectángulo es: {area}")

def calcular_area_cuadrado(lado):
    from Problema_4 import Rectangulo
    rectangulo = Rectangulo(lado, lado)
    area = rectangulo.calcular_area()
    print(f"El área del cuadrado es: {area}")

def mostrar_menu():
    print("Menú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '4':
            print("¡Bye Bye!")
            break
        elif opcion == '1':
            radio = float(input("Ingrese el radio del círculo: "))
            calcular_area_circulo(radio)
        elif opcion == '2':
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            calcular_area_rectangulo(largo, ancho)
        elif opcion == '3':
            lado = float(input("Ingrese el lado del cuadrado: "))
            calcular_area_cuadrado(lado)
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
