def factorialN(n):
    resultado = 1
    for index in range(1, n + 1):
        resultado *= index

    return resultado

continuar = True

while continuar == True:
    numero = input("Ingrese un valor para saber su factorial: ")
    factorial = factorialN(int(numero))

    print(f"El factorial de {numero} es: {factorial}")

    respuestaUsuario = input("¿Evaluar otro número? s/n: ")

    continuar = respuestaUsuario.lower() == "s"
