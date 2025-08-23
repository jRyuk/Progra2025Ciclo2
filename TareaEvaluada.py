"""Sistema de Descuento y Verificación de Edad para un Centro Deportivo

Imagina que trabajas en un sistema para un centro deportivo que ofrece descuentos y verifica la edad de sus usuarios. El sistema debe seguir estas reglas:

Si un usuario es menor de 18 años, debe recibir un descuento del 20% en la membresía. Si tiene entre 18 y 25 años, recibirá un descuento del 10%. Si tiene más de 25 años, no recibirá descuento.
Si el usuario tiene más de 60 años, deberá pagar un precio reducido, pero solo si es miembro del centro.
Si el usuario no es miembro, se le cobrará el precio completo.
Si el usuario no proporciona su edad o estado de membresía (es decir, los campos están vacíos o no se proporcionan), se debe mostrar un mensaje de error.
Subir un archivo pdf que contenga:
Captura de código de solución completo, legible
captura de ejemplo de ejecución en consola  
captura de diagrama de flujo en imagen en el mismo pdf
Ponderación: 

Diagrama 50%
Solución 50%"""

edad =0
estaRegistradoStr = ""
estaRegistrado=False;
descuento =0
precio = 25
totalPagar =0

print("Ingrese su edad:" )
edad = int(input())

estaRegistradoStr = input("Tiene membresia ? (S/N) ") 

if estaRegistradoStr == "s":
    estaRegistrado = True

if edad == "" or estaRegistradoStr == "":
    print("Datos incorrectos")
else:
    if edad < 18:
        descuento = 0.2
    elif edad >= 18 and edad <= 25:
        descuento = 0.1
    elif edad > 60 and estaRegistrado == True:
        descuento = 0.5

    totalPagar = precio - (precio * descuento)
    print(f"Total a pagar: ${totalPagar}")

