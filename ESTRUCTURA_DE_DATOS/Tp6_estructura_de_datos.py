print("Ejercicio 1")

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

print("\nEjercicio 2")

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

print("\nEjercicio 3")

frutas = list(precios_frutas.keys())
print(frutas)

print("\nEjercicio 4")

contactos = {}

for i in range(5):
    nombre = input("Nombre del contacto: ").strip()
    telefono = input("Número de teléfono: ").strip()
    contactos[nombre] = telefono

nombre = input("Nombre a consultar: ").strip()

if nombre in contactos:
    print("Teléfono:", contactos[nombre])
else:
    print("El contacto no existe.")

print("\nEjercicio 5")

frase = input("Ingresá una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

print("\nEjercicio 6")

alumnos = {}

for i in range(3):
    nombre = input("Nombre del alumno: ").strip()
    nota1 = float(input("Primera nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Tercera nota: "))
    alumnos[nombre] = (nota1, nota2, nota3)

for nombre in alumnos:
    notas = alumnos[nombre]
    promedio = sum(notas) / 3
    print(nombre, "- Promedio:", round(promedio, 2))

print("\nEjercicio 7")

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {3, 4, 5, 6, 7}

print("Aprobaron ambos parciales:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos un parcial:", parcial1 | parcial2)

print("\nEjercicio 8")

stock = {"arroz": 10, "leche": 15, "pan": 20}
opcion = ""

while opcion != "3":
    print("\n1. Consultar stock")
    print("2. Agregar unidades o un producto nuevo")
    print("3. Continuar")
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        producto = input("Nombre del producto: ").strip().lower()
        if producto in stock:
            print("Stock:", stock[producto])
        else:
            print("El producto no existe.")
    elif opcion == "2":
        producto = input("Nombre del producto: ").strip().lower()
        unidades = int(input("Unidades a agregar: "))
        if unidades > 0:
            if producto in stock:
                stock[producto] += unidades
            else:
                stock[producto] = unidades
            print("Stock de", producto + ":", stock[producto])
        else:
            print("La cantidad debe ser mayor que cero.")
    elif opcion != "3":
        print("Opción incorrecta.")

print("\nEjercicio 9")

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Día a consultar: ").strip().lower()
hora = input("Hora a consultar (HH:MM): ").strip()
fecha = (dia, hora)

if fecha in agenda:
    print("Actividad:", agenda[fecha])
else:
    print("No hay actividades en ese día y horario.")

print("\nEjercicio 10")

paises = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
capitales = {}

for pais in paises:
    capital = paises[pais]
    capitales[capital] = pais

print(capitales)
