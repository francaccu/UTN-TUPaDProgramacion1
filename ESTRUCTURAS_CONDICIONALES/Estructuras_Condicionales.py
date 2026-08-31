from statistics import mode, mean, median
import random
#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad.")

#Ejercicio 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")

#Ejercicio 3
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print("El numero es par.")
else:
    print("Por favor, ingrese un numero par")
    
#Ejercicio 4
edad1 = int(input("Ingrese su edad: "))
if edad1 <= 12:
    print("Usted es un niño.")
elif edad1 >= 12 and edad1 < 18:
    print("Usted es un adolescente.")
elif edad1 >= 18 and edad1 < 30:
    print("Usted es un adulto joven")
else:
    print("Usted es un adulto")

#Ejercicio 5
contraseña = input("Ingrese su contraseña: ")
leer = len(contraseña)
if leer >= 8 and leer <= 14:
    print("Usted ha ingresado una contraseña valida")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres")

#Ejercicio 6
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

if moda > media > mediana:
    print("El sesgo es positivo")
else:
    print("El sesgo es negativo")
    
#Ejercicio 7
palabra = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
if palabra[-1] in vocales:
    palabra = palabra + "!"
print(palabra)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese una opcion (1-3): ")
if opcion == "1":
    mayusculas = nombre.upper()
    print(mayusculas)
elif opcion == "2":
    minusculas = nombre.lower()
    print(minusculas)
elif opcion == "3":
    primera = nombre.title()
    print(primera)
    
#Ejercicio 9
terremoto = int(input("Ingrese la magnitud del terremoto: "))
if terremoto > 3:
    print("Muy leve")
elif terremoto >= 3 and terremoto < 4:
    print("Leve")
elif terremoto >= 4 and terremoto < 5:
    print("Moderado")
elif terremoto >= 5 and terremoto < 6:
    print("Fuerte")
elif terremoto >= 6 and terremoto < 7:
    print("Muy fuerte")
else:
    print("Extremo")

#Ejercicio 10
emisferio = input("Ingrese el hemisferio (Norte/Sur): ")
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el dia (1-31): "))
if emisferio == "Norte":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Invierno")
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Primavera")
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Verano")
elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")
else:
    if emisferio == "Sur":
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
            print("Verano")
    elif (mes == 3 and dia >=21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
            print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
            print("Primavera")
