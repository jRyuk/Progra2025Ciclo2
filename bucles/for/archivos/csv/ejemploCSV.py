import csv

with open("datos.csv", mode="+a", newline="", encoding="utf-8") as file:
    data = []
    writer = csv.writer(file)
    data.append(["ID","Nombre","Edad","Salario"])
    
    for i in range(0,101):
        data.append([i,"Nombre " + str(i), i+10, i * 2 ])
    
    writer.writerows(data)
