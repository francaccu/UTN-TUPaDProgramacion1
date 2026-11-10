def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    return contar_digito(numero // 10, digito)
