# Declarar variables
consulta = True
resultado=0
while consulta:
    # Ingresar número
    numero = int(input("Ingrese un número: "))

    # Según el diagrama: resultado = numero / 5
    resultado = resultado % 5

    # Verificación incorrecta: se evalúa si el resultado es múltiplo de 5
    if resultado == 0:
        print("El número es múltiplo de 5")
    else:
        print("El número no es múltiplo de 5")

    # Consultar si desea evaluar otro número
    respuesta = input("¿Desea evaluar otro número? (s/n): ")
    if respuesta.lower() != 's':
        consulta = False