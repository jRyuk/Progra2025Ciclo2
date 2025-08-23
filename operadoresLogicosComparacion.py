#Necesitamos saber si una persona es menor de edad, si es adolescente, si es considerado joven
# o si es considerado adulto o si es considerado de la tercera edad

edad =0
print("Ingrese su edad: ")
edad = input()

edad = int(edad)

# edad < 18 menor de edad
# adolescente 12 a los 19 
# joven 20 a los 35
# si es mayor a 35 y memor de 60 es adulto
# mayor de 60 tercera edad 

if edad < 18:
    print("Es menor de edad")
elif edad >= 12 and edad <=19:
    print("La persona es adolescente")

if edad >=20 and edad <= 35:
    print("La persona es joven")
    
if edad > 35 and edad < 60:
    print("Adulto")

if edad  >= 60:
    print("Tercera edad")