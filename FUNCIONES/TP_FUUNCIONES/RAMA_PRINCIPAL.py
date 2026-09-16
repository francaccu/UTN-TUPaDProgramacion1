import imprimir_hola_mundo
import saludar_usuario
import informacion_personal
import calcular_area_circulo
import segundos_a_horas
import tabla_multiplicar
import operacion_basicas
import calcular_imc
import celcius_a_faren
import calcular_promedio
#Ejercicio 1


imprimir_hola_mundo.imprimir_hola_mundo()

#EJERCICIO 2
saludar_usuario.saludar_usuario("Francisco")

#EJERCICIO 3

informacion_personal.informacion_personal("Francisco","Caccuri",18,"Mendoza")

#EJERCICIO 4
radio = float(input("Ingrese el radio del círculo: "))

calcular_area_circulo.calcular_area_circulo(radio)
calcular_area_circulo.calcular_perimetro_circulo(radio)

#EJERCICIO 5
segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas.segundos_a_horas(segundos)

#Ejercicio 6
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar.tabla_multiplicar(numero)

#EJERCICIO 7

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultado = operacion_basicas.operacion_basicas(a, b)
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")


#EJERCICIO 8
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc.calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#EJERCICIO 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
faren = celcius_a_faren.celcius_a_farenheit(celsius)

#EJERCICIO 10

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

calcular_promedio.calcular_promedio(a,b,c)

print(f"El promedio es: {calcular_promedio}")