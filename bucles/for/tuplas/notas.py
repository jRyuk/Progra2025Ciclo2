"""
    1. Promedio
    2. Nota mayor 
    3. Nota menor
"""
notas = {"Juan": 7, "María": 9, "Pedro": 6, "Pepito": 5.9}

notaMayor =0
notaMenor=10
sumaNotas =0
contador =0

for key, value in notas.items():
    #obtenemos la nota mayor
    if value > notaMayor:
        notaMayor = value
    
    if value < notaMenor:
        notaMenor = value

    sumaNotas = sumaNotas + value
    contador += 1

print(f"Nota mayor: {notaMayor}")
print(f"Nota menor: {notaMenor}")
promedio = sumaNotas/ contador
print(f"Promedio: {promedio}")




