def decimal_a_binario(numero):
    """Convierte un número decimal a binario"""
    cociente = numero
    residuos = []
    binario = ""

    while cociente > 0:
        residuo = cociente % 2
        residuos.append(residuo)
        cociente //= 2

    # Revertir la lista de residuos
    residuos.reverse()

    # Imprimir el resultado con los cálculos intermedios
    print(f"{numero} en binario es:")
    for i, residuo in enumerate(residuos):
        if binario:
            binario_int = int(binario, 2)
            cociente_int = binario_int * 2 + residuo
            cociente = bin(cociente_int)[2:]
            binario += str(residuo)
            print(f"{cociente:4}  {cociente_int} dividido entre 2 da {binario_int} y sobra {residuo}")
        else:
            binario = str(residuo)
            print(f"{binario:4}  {residuo} dividido entre 2 da 0 y sobra {residuo}")

    return binario


def binario_a_decimal(binario):
    """Convierte un número binario a decimal"""
    decimal = 0
    potencia = len(binario) - 1

    for digito in binario:
        decimal += int(digito) * (2 ** potencia)
        potencia -= 1

    return decimal


# Ejemplo de uso
numero_decimal = 41
numero_binario = decimal_a_binario(numero_decimal)
print(numero_binario)

numero_binario = "101010"
numero_decimal = binario_a_decimal(numero_binario)
print(numero_decimal)



