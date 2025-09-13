def sumar(n1, n2):
    return n1 + n2

def saludar():
    print("Hola mundo")

def factorialN(n):
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * i
    
    return resultado


#llamar a la funcion o definicion
#resultado = sumar(10,20)
#saludar()
#print(resultado)
factorial = factorialN(5)
print(f"El factorial de 5 es: {factorial}")