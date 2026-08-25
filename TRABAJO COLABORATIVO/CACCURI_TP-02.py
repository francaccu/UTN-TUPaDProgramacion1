#Ejercicio 1
print("Hola Mundo")
#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"¡Hola, {nombre}!")
#Ejercicio 3
name = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
casa = input("Ingrese donde vive: ")
print(f"Hola mi nombre es {name}, tengo {edad} y vivo en {casa}")
#Ejercicio 4
radio = float(input("Ingrese el radio de su circulo: "))
print(f"El area de su circulo es: {3.14 * radio ** 2} y su perimetro es: {2 * 3.14 *radio}")
#Ejercicio 5
segunodos = int(input("Ingrese la cantidad de segundos: "))
print(f"Los segundos equivalen a: {segunodos // 3600} horas")
#Ejercicio 6
num = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    
    
#Ejercicio 7
num1 = int(input("Ingrese un numero distinto de 0: "))
num2 = int(input("Ingrese otro numero distinto de 0: "))
suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La división es: {division}")
print(f"La multiplicación es: {multiplicacion}")
#Ejercicio 8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc}")
#Ejercicio 9
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (temperatura * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")
#Ejercicio 10
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
numero3 = float(input("Ingrese un tercer numero: "))
print(f"El promedio de los tres numeros es: {(numero1 + numero2 + numero3) / 3}")
