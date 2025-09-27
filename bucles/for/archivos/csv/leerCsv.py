import csv
index = 0
salarioMaximo = 0
infoMaxima =[]
with open("datos.csv",mode="r",encoding="utf-8") as file:
    data = csv.reader(file)
    
    for row in data:
        if index == 0:
            index += 1
            continue
        if(float(row[-1]) > salarioMaximo):
            salarioMaximo = float(row[-1])
            infoMaxima= row

        index +=1

print(infoMaxima)

    