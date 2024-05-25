class Producto:
    def __init__(self, codigo, nombre, precio, año):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Año: {self.año}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __str__(self):
        if not self.productos:
            return "El catálogo está vacío."

        catalogo_str = "Lista de productos en el catálogo:\n"
        for producto in self.productos:
            catalogo_str += str(producto) + "\n"
        
        return catalogo_str.strip()

# Uso del programa
catalogo = Catalogo()

productos = [
    Producto("321", "Filtro de agua", 25.40, 2024),
    Producto("478", "Procesador", 50.60, 2024),
]

for producto in productos:
    catalogo.agregar_producto(producto)

print(catalogo)
