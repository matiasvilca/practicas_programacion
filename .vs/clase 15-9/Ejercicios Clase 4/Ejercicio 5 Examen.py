# Un alumno aprueba si su nota es mayor o igual a 6. 
# Consigna: Pedir la nota y mostrar “Aprobado” o “Desaprobado”.

nota_alumno = float(input("Por favor, ingrese la nota del alumno: "))
if nota_alumno >= 6 and nota_alumno <= 10:
    print("Aprobado.")
else:
    if nota_alumno <= 6 and nota_alumno >= 0:
        print("Desaprobado.")
    else:
        print("Por favor, ingrese un número entre 0 y 10.")