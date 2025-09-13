frutas = ["Manzana", "Banana", "Cereza", "mango", "Cereza"]

contador = 1

print("Lista de frutas")

for fruta in frutas:
    print(f"{contador}. {fruta}")
    contador +=  1

remover = input("Ingrese el nombre de la fruta a remover: ")

frutas.remove(remover)

#indice = frutas.index(remover)

#del frutas[indice]

print(f"Frutas restantes: {frutas}")