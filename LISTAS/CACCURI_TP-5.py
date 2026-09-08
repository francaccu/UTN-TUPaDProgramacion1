
# 1) 

multiplos_de_4 = list(range(4, 101, 4))
print("Ejercicio 1:", multiplos_de_4)


# 2) 

elementos = ["auto", "pelota", "libro", "computadora", "mochila"]
penultimo = elementos[-2]  # el índice -2 es el anteúltimo elemento
print("Ejercicio 2:", penultimo)


# 3) 

lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("Ejercicio 3:", lista_vacia)


# 4)

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"   
animales[-1] = "oso"  
print("Ejercicio 4:", animales)


# 5) 

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print("Ejercicio 5:", numeros)
# Explicación:
# max(numeros) busca el valor más grande de la lista
# numeros.remove elimina ese valor en la lista.
# Entonces el programa busca el número más grande y lo saca de la lista,
# y al final imprime la lista sin ese elemento: [8, 15, 3, 7]



# 6)

numeros_saltos = list(range(10, 31, 5))
print("Ejercicio 6:", numeros_saltos[0], numeros_saltos[1])


# 7) 

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "audi"
autos[2] = "bmw"
print("Ejercicio 7:", autos)


# 8) 

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Ejercicio 8:", dobles)


# 9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Ejercicio 9:", compras)


# 10)

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Ejercicio 10:", lista_anidada)
