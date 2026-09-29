# Verificación de edad para ver una película
# Supongamos que estás desarrollando un programa para un cine y deseas asegurarte de que los espectadores sean lo suficientemente mayores para ver una película clasificada como PG-13. 
# Debes solicitar la edad del espectador y permitir el acceso solo si tienen al menos 13 años.

edad = int(input("Por favor, ingrese su edad: "))
if edad >= 13 and edad >=0:
    print("Usted puede pasar.")
else:
    print("Usted no puede pasar.")