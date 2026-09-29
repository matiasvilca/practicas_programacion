# Validar dias de la semana

# Crea un programa que pida al usuario ingresar un número del 1 al 7 y muestre el día de la semana correspondiente. 
# Si ingresa un número fuera de ese rango, mostrar el siguiente mensaje de error: "Número de día incorrecto".

numero = input("Ingrese un número (1-7): ")
if numero == '1':
    print("Domingo.")
elif numero == '2':
    print("Lunes.")
elif numero == '3':
    print("Martes.")
elif numero == '4':
    print("Miércoles.")
elif numero == '5':
    print("Jueves.")
elif numero == '6':
    print("Viernes.")
elif numero == '7':
    print("Sábado.")
else:
    print("Número de día incorrecto (1-7).")