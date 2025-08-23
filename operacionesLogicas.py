x1 = input("Ingrese un numero: ") 
x2 = input("Ingrese otro numero: ") 

x1 = float(x1)
x2 = float(x2)

x1MayorAx2 = x1 > x2   #>mayor a 
x1Igualx2 = x1 == x2 # == igual a
x1Diferentex2 = x1 != x2 # != diferente de 
x1MenorQuex2 = x1 < x2 # < menor que 


print(f"{x1} es mayor a {x2}: {x1MayorAx2}")
print(f"{x1} es igual  a {x2}: {x1Igualx2}")
print(f"{x1} es difente de  {x2}: {x1Diferentex2}")
print(f"{x1} es menor que  {x2}: {x1MenorQuex2}")
