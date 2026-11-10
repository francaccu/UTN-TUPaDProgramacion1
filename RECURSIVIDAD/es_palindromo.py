def comparar_letras(palabra, inicio, fin):
    if inicio >= fin:
        return True
    if palabra[inicio] != palabra[fin]:
        return False
    return comparar_letras(palabra, inicio + 1, fin - 1)


def es_palindromo(palabra):
    return comparar_letras(palabra, 0, len(palabra) - 1)
