class Calificaciones:
    def __init__(self):
        self.calificaciones = []

    def obtener_calificaciones(self):
        while True:
            entrada = input("Ingrese una lista de calificaciones separadas por comas: ")
            try:
                self.calificaciones = [int(cal.strip()) for cal in entrada.split(',')]
                print("Calificaciones convertidas:", self.calificaciones)
                break
            except ValueError:
                print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

calificaciones = Calificaciones()
calificaciones.obtener_calificaciones()
