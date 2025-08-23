#imprimir los numeros del 100 al 0
"""
100 99 98 97 96
95  94 93 92 91
"""
contador =0
for i in range(100, 0, -1):
    if contador < 4:
        print(i, end= " ")
        contador = contador+1
    else:
        contador =0
        print(i)
    
    
    