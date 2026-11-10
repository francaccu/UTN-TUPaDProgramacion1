def decimal_a_binario(numero):
    if numero < 2:
        return str(numero)
    return decimal_a_binario(numero // 2) + str(numero % 2)
