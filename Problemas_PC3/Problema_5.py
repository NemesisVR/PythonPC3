class Alumno:
    def __init__(self, nombre, num_registro, edad=None, notas=None):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = edad
        self.notas = notas if notas is not None else []

    def display(self):
        print(f"Información del alumno:\nNombre: {self.nombre}\nNúmero de registro: {self.num_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")
        else:
            print("No hay notas asignadas.")

# Uso del programa
alumno1 = Alumno("Eduardo", "399602", edad=18, notas=[15, 20, 18])

alumno1.display()

