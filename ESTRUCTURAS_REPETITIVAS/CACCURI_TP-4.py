import random
from statistics import mode, mean, median
#Ejercicio 1
num = 0
for i in range(0,101):
    print(num)
    num += 1

#Ejercicio 2
numero = int(input("Ingrese un numero entero: "))
for numero in range(0, numero + 1):
    length = len(str(numero))
print(f"El numero tiene {length} digitos")

#Ejercicio 3
primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
suma = 0
for i in range(primer_numero + 1, segundo_numero):
    suma = suma + i
print(f"La suma de los numeros entre {primer_numero} y {segundo_numero} es: {suma}")

#Ejercicio 4
numero_usuario = int(input("Ingrese un numero entero para iniciar la secuencia cuando coloque 0 se detendra: "))
suma_secuencia = 0
while numero_usuario != 0:
    suma_secuencia += numero_usuario
    numero_usuario = int(input("Ingrese otro numero entero para continuar la secuencia o 0 para detenerse: "))
print(f"La suma de la secuencia es: {suma_secuencia}")

#Ejercicio 5
intentos = 0
usuario = int(input("Ingrese un numero entero: "))
numero_aleatorio = random.randint(0,9)
while usuario != numero_aleatorio:
    intentos = 1 + intentos
    print("El numero ingresado no es correcto, intente nuevamente")
    usuario = int(input("Ingrese otro numero entero: "))
print(f"Bien adivinaste el numero aleatorio tardaste {intentos} intentos en adivinar")

#Ejercicio 6
for i in range(100, -1, -2):
    print(i)
#Ejercicio 7
nume1 = int(input("Ingrese un numero entero positivo para hacer la secuencia de suma: "))
sum = 0
for i in range(0, nume1):
    sum += i
print(f"La suma de la secuencia es: {sum}")

#Ejercicio 8
usuario1 = 0
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(0,100):
    usuario1 = int(input("Ingrese un numero entero: "))
    if usuario1 % 2 == 0:
        pares += 1
    else:
        impares += 1
    if usuario1 > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")


#Ejercicio 9
usuario2 = 0
media = 0
for i in range(0,5):
    usuario2 = int(input("Ingrese un numero entero: "))
    media = usuario2 + media
media = media / 5
print(f"La media de los numeros ingresados es: {media}")

#Ejercicio 10
numeroo = int(input("Ingrese un numero que quiera invertir: "))
numero_invertido = 0
while numeroo > 0:
    digito = numeroo % 10
    numero_invertido = (numero_invertido * 10) + digito
    numeroo = numeroo // 10
print(f"El numero invertido es: {numero_invertido}")