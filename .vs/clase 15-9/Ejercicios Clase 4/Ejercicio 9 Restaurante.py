# Un restaurante ofrece menú vegetariano. 
# Consigna: Preguntar si el cliente es vegetariano y mostrar el menú correspondiente.

food_status = str(input("¿Es usted vegetariano?: Si/No: "))
if food_status == "si":
    print("Perfecto, acá tiene el menú vegetariano.")
elif food_status == "no":
    print("Vale, no necesitará el menú vegetariano.")
else:
    print("Respuesta incorrecta. Por favor, ingrese 'si' o 'no'.")
        