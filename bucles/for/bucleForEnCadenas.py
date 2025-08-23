#Saber si un texto es un palindromo y cuantas vocales tiene
#ana, oso, anita lava la tina

#hola mundo
texto = input("ingrese un texto: ")
textoPivote =  texto
texto = texto.replace(" ", "")
#odnum aloh
textoInvertido = ""

for i in range(len(texto) -1, -1, -1):
    textoInvertido = textoInvertido +  texto[i]
    #print(texto[i])  

if textoInvertido == texto:
    print(f"{textoPivote} es un palindromo")
else: 
     print(f"{textoPivote} no es un palindromo")