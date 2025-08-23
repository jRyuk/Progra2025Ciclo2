#Si el cliente compra más de $100, 
# se le aplica 10% de descuento. Mostrar total a pagar.

def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


compra = input("Ingrese el valor de la compra: ")
totalPagar = 0

if is_float(compra):
    compra = float(compra)
    if compra > 100:
        totalPagar = compra - (compra * 0.1)
        print(f"Total a pagar: {totalPagar}")
    else: 
         print(f"Total a pagar: {compra}")
else:
    print("El valor ingresado es incorrecto")
