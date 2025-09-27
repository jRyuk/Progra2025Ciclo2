import csv
index = 0
salarioMaximo = 0
infoMaxima =[]
data= []

with open("datos.csv",mode="r",encoding="utf-8") as file:
    data = list(csv.reader(file))

indexEdad = data[0].index("Edad")

listaEdades = [row[indexEdad] for row in data[1:]]
print(listaEdades)






