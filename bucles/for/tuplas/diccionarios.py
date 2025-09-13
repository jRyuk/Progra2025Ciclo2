diccionario = {"clave1": 5,
                "clave2": "Hola mundo", 
                "PI": 3.1416, 
                "numero10":10,
                "clave1": 10,
                "claveNotas": {"Juan": 7, "Jorge": 8, "Pepito": 5.99}
                }

print(diccionario.get("Pepito","none"))
print(diccionario["clave1"])
print(type(diccionario["numero10"]))

for clave in diccionario:
    print(f"Clave: {clave}, valor: {diccionario[clave]}")

print("----- Imprimiendo clave valor sin acceder por clave")
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, valor: {valor}")
