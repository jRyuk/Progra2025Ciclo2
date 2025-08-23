"""
Crea un programa en Python que:
1- Genere un número secreto entre 1 y 20.
2- Permita al usuario intentar adivinarlo con máximo 5 intentos.
3- Si el usuario ingresa un número menor o igual a 0, use continue para pedirle otro número (no cuenta como intento).
4- Si el usuario acierta el número secreto, use break para terminar el bucle inmediatamente.
5- Al final, muestra un mensaje indicando si ganó o perdió.
"""
import random

numSecret = random.randint(1,20)
userNum = 0 # es el número que ingreso el usuario

maximoIntentos= 5 #bandera el usuario solo tiene 5 intentos
intentosUsuario = 0 #cuantos intentos lleva el usuario
resultado = f"El usuario no adivino el número: {numSecret}"

while intentosUsuario < maximoIntentos: #mientras que los intentos del usuario no pasen de 5, vamos a ejecutar el bucle
    userNum = input("Adivina el un número entre 1 y 20: ")

    if userNum.isnumeric() == False:
        continue

    if userNum <=0 or userNum > 20:
        print("Numero fuera del rango entre 1 y 20")
        continue

    intentosUsuario += 1

    if userNum == numSecret:
        resultado = f"El usuario adivino el número: {numSecret}"
        break


print(resultado)

