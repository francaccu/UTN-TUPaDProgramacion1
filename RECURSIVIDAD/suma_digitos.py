def suma_digitos(numero):
    if numero < 10:
        return numero
    return numero % 10 + suma_digitos(numero // 10)
