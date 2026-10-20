# Práctica de Programación I: Archivos
# Ejecutar este programa desde la carpeta donde está productos.txt.

# 1. Crear el archivo inicial solamente si no existe.
try:
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,1500.0,10\n")
        archivo.write("Goma,250.0,20\n")

    with open("productos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

# 2 y 4. Leer, mostrar y cargar los productos en una lista de diccionarios.
productos = []

print("PRODUCTOS GUARDADOS")
for linea in lineas:
    linea = linea.strip()

    if linea != "":
        datos = linea.split(",")
        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        productos.append(producto)

        print(f"Producto: {producto['nombre']} | "
              f"Precio: ${producto['precio']} | "
              f"Cantidad: {producto['cantidad']}")

# 3. Agregar uno o más productos desde el teclado.
agregar = "s"

while agregar == "s":
    print("\nINGRESAR UN NUEVO PRODUCTO")
    nombre = input("Nombre: ").strip()

    # La coma se utiliza para separar los datos dentro del archivo.
    while nombre == "" or "," in nombre:
        print("El nombre no puede estar vacío ni contener comas.")
        nombre = input("Nombre: ").strip()

    while True:
        try:
            precio = float(input("Precio (usar punto para los decimales): "))
            if precio >= 0:
                break
            print("El precio no puede ser negativo.")
        except ValueError:
            print("Ingresá un número válido.")

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad >= 0:
                break
            print("La cantidad no puede ser negativa.")
        except ValueError:
            print("Ingresá un número entero válido.")

    # El modo "a" agrega al final sin borrar lo que ya estaba guardado.
    with open("productos.txt", "a", encoding="utf-8") as archivo:
        # Si la última línea no tenía salto, separar el nuevo registro.
        if len(lineas) > 0 and not lineas[-1].endswith("\n"):
            archivo.write("\n")
        nueva_linea = f"{nombre},{precio},{cantidad}\n"
        archivo.write(nueva_linea)

    lineas.append(nueva_linea)
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(producto)
    print("Producto agregado.")

    agregar = input("¿Querés agregar otro producto? (s/n): ").strip().lower()
    while agregar != "s" and agregar != "n":
        agregar = input("Ingresá s o n: ").strip().lower()

# 5. Buscar un producto por su nombre.
buscado = input("\nNombre del producto a buscar: ").strip().lower()
encontrado = False

for producto in productos:
    if producto["nombre"].lower() == buscado:
        print(f"Producto: {producto['nombre']} | "
              f"Precio: ${producto['precio']} | "
              f"Cantidad: {producto['cantidad']}")
        encontrado = True

if encontrado == False:
    print("Error: no se encontró un producto con ese nombre.")

# 6. Sobrescribir el archivo con todos los productos de la lista.
# La lista incluye tanto los productos originales como los nuevos.
with open("productos.txt", "w", encoding="utf-8") as archivo:
    for producto in productos:
        archivo.write(
            f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        )

print("\nTodos los productos quedaron guardados en productos.txt.")
