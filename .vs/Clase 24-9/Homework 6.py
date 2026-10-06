# Notas de un alumno
# Crea un programa que determine y muestre al alumno, según la nota que ingrese, 
# a que categoría pertenece de calificación.  Si la nota no corresponde con las categorías, 
# mostrar el mensaje "La nota ingresada es invalida". Las categorías son: 

# Suspenso → Notas: 0, 1, 2, 3, 4 y 5 
# Aprobado → Nota: 6 
# Buena → Nota: 7 
# Notable → Nota: 8 
# Sobresaliente → Notas: 9 y 10 

nota = float(input("Ingrese la nota del alumno (1-10): "))
if nota == 10 or nota == 9:
    print("Sobresaliente.")
elif nota == 8:
    print("Notable.")
elif nota == 7:
    print("Buena.")
elif nota == 6:
    print("Aprobado.")
elif nota >= 0 and nota < 6:
    print("Suspenso.")
else:
    print("La nota ingresada es inválida.")