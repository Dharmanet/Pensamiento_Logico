def sumar_binarios(a, b):
    # Convierte a enteros los valores binarios de entrada
    a_int = int(a, 2)
    b_int = int(b, 2)
    # Suma los valores enteros y los convierte a binario
    resultado_int = a_int + b_int
    resultado_bin = bin(resultado_int)[2:]
    # Devuelve el resultado en formato binario
    return resultado_bin

def restar_binarios(a, b):
    # Convierte a enteros los valores binarios de entrada
    a_int = int(a, 2)
    b_int = int(b, 2)
    # Resta los valores enteros y los convierte a binario
    resultado_int = a_int - b_int
    resultado_bin = bin(resultado_int)[2:]
    # Devuelve el resultado en formato binario
    return resultado_bin

def multiplicar_binarios(a, b):
    # Convierte a enteros los valores binarios de entrada
    a_int = int(a, 2)
    b_int = int(b, 2)
    # Multiplica los valores enteros y los convierte a binario
    resultado_int = a_int * b_int
    resultado_bin = bin(resultado_int)[2:]
    # Devuelve el resultado en formato binario
    return resultado_bin

def dividir_binarios(a, b):
    # Convierte a enteros los valores binarios de entrada
    a_int = int(a, 2)
    b_int = int(b, 2)
    # Divide los valores enteros y los convierte a binario
    resultado_int = a_int // b_int
    resultado_bin = bin(resultado_int)[2:]
    # Devuelve el resultado en formato binario
    return resultado_bin

# Función para mostrar un menú de opciones
def mostrar_menu():
    print("Elija una opción:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = input("Opción seleccionada: ")
    return opcion

# Función para pedir dos números binarios al usuario
def pedir_numeros():
    a = input("Ingrese el primer número binario: ")
    b = input("Ingrese el segundo número binario: ")
    return a, b

# Programa principal
opcion = mostrar_menu()
a, b = pedir_numeros()

if opcion == "1":
    resultado = sumar_binarios(a, b)
    print(f"La suma de {a} y {b} es: {resultado}")
elif opcion == "2":
    resultado = restar_binarios(a, b)
    print(f"La resta de {a} y {b} es: {resultado}")
elif opcion == "3":
    resultado = multiplicar_binarios(a, b)
    print(f"La multiplicación de {a} y {b} es: {resultado}")
elif opcion == "4":
    resultado = dividir_binarios(a, b)
    print(f"La división de {a} entre {b} es: {resultado}")
else:
    print("Opción inválida")
