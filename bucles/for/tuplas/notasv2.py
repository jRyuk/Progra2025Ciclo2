"""
    1. Promedio
    2. Nota mayor 
    3. Nota menor
"""
notas = {"Juan": 7, "María": 9, "Pedro": 6, "Pepito": 5.9}

alumnoNotaMayor = max(notas, key=notas.get)
notaMayor=notas[alumnoNotaMayor]

alumnoNotaMenor = min(notas, key=notas.get)
notaMenor= notas[alumnoNotaMenor]

promedio = sum(notas.values()) / len(notas)

print(f"Nota mayor: {notaMayor}, Alumno: {alumnoNotaMayor}")
print(f"Nota menor: {notaMenor}, Alumno: {alumnoNotaMenor}")
print(f"Promedio de notas: {promedio}")


