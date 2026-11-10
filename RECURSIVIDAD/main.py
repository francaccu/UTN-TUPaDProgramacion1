from contar_bloques import contar_bloques
from contar_digito import contar_digito
from decimal_a_binario import decimal_a_binario
from es_palindromo import es_palindromo
from factorial import factorial
from fibonacci import fibonacci
from potencia import potencia
from suma_digitos import suma_digitos


if __name__ == "__main__":
    print("EJERCICIO 1")
    numero = int(input("Ingrese un numero entero positivo: "))
    for i in range(1, numero + 1):
        print("El factorial de", i, "es", factorial(i))

    print("\nEJERCICIO 2")
    posicion = int(input("Ingrese una posicion de la serie de Fibonacci: "))
    print("Serie completa:")
    for i in range(posicion + 1):
        print(fibonacci(i), end=" ")
    print()
    print("El valor en la posicion", posicion, "es", fibonacci(posicion))

    print("\nEJERCICIO 3")
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese un exponente entero no negativo: "))
    print(base, "elevado a", exponente, "es", potencia(base, exponente))

    print("\nEJERCICIO 4")
    numero = int(input("Ingrese un numero entero positivo en base decimal: "))
    print("El numero", numero, "en binario es", decimal_a_binario(numero))

    print("\nEJERCICIO 5")
    palabra = input("Ingrese una palabra sin espacios ni tildes: ")
    print(es_palindromo(palabra))

    print("\nEJERCICIO 6")
    numero = int(input("Ingrese un numero entero positivo: "))
    print("La suma de los digitos es", suma_digitos(numero))

    print("\nEJERCICIO 7")
    numero = int(input("Ingrese la cantidad de bloques del nivel mas bajo: "))
    print("Se necesitan", contar_bloques(numero), "bloques para construir la piramide")

    print("\nEJERCICIO 8")
    numero = int(input("Ingrese un numero entero positivo: "))
    digito = int(input("Ingrese un digito entre 0 y 9: "))
    print("El digito", digito, "aparece", contar_digito(numero, digito), "veces")
