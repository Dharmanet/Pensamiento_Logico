def sumar_binarios(binario1, binario2):
    # Convertir los binarios a enteros
    entero1 = int(binario1, 2)
    entero2 = int(binario2, 2)

    # Sumar los enteros
    resultado_entero = entero1 + entero2

    # Convertir el resultado de nuevo a binario
    resultado_binario = bin(resultado_entero)[2:]

    # Agregar ceros a la izquierda si es necesario
    if len(resultado_binario) < len(binario1):
        diferencia = len(binario1) - len(resultado_binario)
        resultado_binario = "0" * diferencia + resultado_binario

    return resultado_binario


def restar_binarios(binario1, binario2):
    # Convertir los binarios a enteros
    entero1 = int(binario1, 2)
    entero2 = int(binario2, 2)

    # Restar los enteros
    resultado_entero = entero1 - entero2

    # Convertir el resultado de nuevo a binario
    resultado_binario = bin(resultado_entero)[2:]

    # Agregar ceros a la izquierda si es necesario
    if len(resultado_binario) < len(binario1):
        diferencia = len(binario1) - len(resultado_binario)
        resultado_binario = "0" * diferencia + resultado_binario

    return resultado_binario


# Pedir los números binarios al usuario
binario1 = input("Introduce el primer número binario: ")
binario2 = input("Introduce el segundo número binario: ")

# Sumar los números binarios
resultado_suma = sumar_binarios(binario1, binario2)

# Restar los números binarios
resultado_resta = restar_binarios(binario1, binario2)

# Mostrar los resultados
print(f"El resultado de sumar {binario1} y {binario2} es: {resultado_suma}")
print(f"El resultado de restar {binario1} y {binario2} es: {resultado_resta}")

