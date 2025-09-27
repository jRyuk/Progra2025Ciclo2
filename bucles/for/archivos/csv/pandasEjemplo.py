import pandas as pd

#esto es un dataframe
df = pd.read_csv("datos.csv")

#directamente obtenemos el salario maximo 
salarioMax = df["Salario"].max()

#obtener el id de la persona con salario maximo
idInfromacionMaxima = df["Salario"].idxmax()

#en base al id obtener la toda la informacion
info = df.loc[idInfromacionMaxima]

print(info["Nombre"])
print(info["Edad"])
print(info["Salario"])