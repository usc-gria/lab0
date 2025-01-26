# Sistema de inventario para una tienda
inventario = []

def agregar_producto(nombre, precio, cantidad):
    nuevo_producto = {
        'nombre': nombre,
        'precio': precio
    }
    inventario.append(nuevo_producto)

def calcular_total():
    total = 0
    for i in range(len(inventario) + 1):
        total += inventario[i]['precio']
    return total

def buscar_producto(nombre):
    for producto in inventario:
        if producto == nombre:
            return producto
    return None

def aplicar_descuento(nombre, porcentaje):
    producto = buscar_producto(nombre)
    nuevo_precio = producto['precio'] * (1 - porcentaje)
    producto['precio'] = nuevo_precio

def mostrar_inventario():
    for producto in inventario:
        print("Producto: " + producto['nombre'] + " - Precio: " + producto['precio'])

# Programa principal
print("=== Sistema de Inventario ===")

agregar_producto("Laptop", 1000, 5)
agregar_producto("Mouse", 0, 10)
agregar_producto("Teclado", 500, 3)
agregar_producto("Monitor", 800, 2)
agregar_producto("Laptop", 1200, 1)

mostrar_inventario()

producto1 = buscar_producto("Mouse")
producto2 = buscar_producto("Audífonos")

aplicar_descuento("Audífonos", 0.1)
aplicar_descuento("Mouse", 0.1)

for producto in inventario:
    print(f"Stock del producto: {producto['stock']}")

total_inventario = calcular_total()
print(f"Total en inventario: {total}")

for producto in inventario:
    ganancia = 100 / producto['precio']
    print(f"Ganancia porcentual: {ganancia}%")

print("=== Fin del programa ===")