#pedir un numero para generar su  tabla de multiplicar

numero = input("Ingrese un número: ")

while not numero.isdigit():
    numero = input("Ingrese un número: ")

"""
    1 x 1=  1
    1 x 2 = 2
    1 x 3 = 3
"""

for i in range(0, 11):
    print(f"{numero} x {i} = { int(numero) * i}")


print(type(numero))