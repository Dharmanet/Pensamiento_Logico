def tabla_verdad(tipo_tabla, p, q):
    """Crea una tabla de verdad para dos proposiciones y los operadores lógicos"""
    
    # Encabezado de la tabla
    print(f"{'p':^5} {'q':^5} {'not p':^6} {tipo_tabla:^6}")
    print("-" * 26)

    # Filas de la tabla
    for i in range(2):
        p_val = i
        q_val = i

        # Evaluar la negación de p
        not_p_val = int(not p_val)

        # Evaluar la proposición compuesta
        if tipo_tabla == 'AND':
            pq_val = p_val and q_val
        elif tipo_tabla == 'OR':
            pq_val = p_val or q_val
        elif tipo_tabla == 'XOR':
            pq_val = p_val ^ q_val
        else:
            raise ValueError("Tipo de tabla no válido")

        # Mostrar la fila en la tabla
        print(f"{p_val:^5} {q_val:^5} {not_p_val:^6} {pq_val:^6}")

# Pedir al usuario los valores de p y q y el tipo de tabla
p = int(input("Valor de p (0 o 1): "))
q = int(input("Valor de q (0 o 1): "))
tipo_tabla = input("Tipo de tabla (AND, OR, XOR): ")

# Mostrar la tabla de verdad
tabla_verdad(tipo_tabla, p, q)
