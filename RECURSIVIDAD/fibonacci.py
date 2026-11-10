def fibonacci(posicion):
    if posicion == 0:
        return 0
    if posicion == 1:
        return 1
    return fibonacci(posicion - 1) + fibonacci(posicion - 2)
