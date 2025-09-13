#Una tienda de tecnología guarda los precios de sus productos en una lista:
precios = [120, 250, 75, 300, 150, 600, 50, 400, 90]

"""
Se pide:
1. Mostrar el precio más bajo y el más alto.
2. Calcular el promedio de precios.
3. Crear una lista con solo los precios mayores o iguales a 200.
4. Aplicar un 10% de descuento a todos los productos y guardar el resultado en una nueva lista.
5. Ordenar la lista original de menor a mayor.
6. Mostrar la lista original invertida (de último a primero).
"""

#1. Precio más bajo y más alto
print(f"Precio más bajo: {min(precios)}")
print(f"Precio más alto: {max(precios)}")

#2. Calcular el promedio de precios.
promedio = sum(precios) / len(precios)
print(f"Promedio de precios: {promedio}")

#3. precios >= 200
precios_altos = [precio for precio in precios if precio >= 200]
print(f"Precios mayores o iguales a 200: {precios_altos}")

#4. Aplicar un 10% de descuento a todos los productos y guardar el resultado en una nueva lista.
precios_descuentos = [ precio - (precio * 0.1) for precio in precios]
print(f"Precios con 10% de descuento: {precios_descuentos}")

#5. Ordenar la lista original de menor a mayor.
nueva_lita = [p for p in precios]
nueva_lita.sort()
print(f"Ordenados de menor a mayor: {nueva_lita}")

#6. Mostrar la lista original invertida (de último a primero).
print(f"Lista original invertida: {precios[::-1]}")