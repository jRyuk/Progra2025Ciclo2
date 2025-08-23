#validar que la entrada por teclado si es un numero

numero = input("Ingrese un número: ")

def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

if numero.isnumeric() or is_float(numero)  :
    numero = float(numero)
    print(f"Ingresaste el número: {numero}, {type(numero)}")
else: 
    print("El valor ingresao no es valido")