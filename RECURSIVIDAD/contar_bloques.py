def contar_bloques(numero):
    if numero == 1:
        return 1
    return numero + contar_bloques(numero - 1)
