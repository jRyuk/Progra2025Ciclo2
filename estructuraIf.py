#Temperatura ambiente

temperatura =int(input("Ingrese la temperatura actual: "))

if temperatura > 30 :
    print("Usa ropa ligera")
elif temperatura >=20:
    print("El clima esta agradable")
elif temperatura >=10:
    print("Esta fresco")
else: 
    print("Esta helado abrigate.")