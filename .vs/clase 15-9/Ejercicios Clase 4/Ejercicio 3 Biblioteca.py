# La biblioteca permite retirar libros solo si el usuario no tiene devoluciones pendientes. 
# Consigna: Pedir el estado del usuario (pendiente o no) y mostrar si puede retirar libros.

estado_usuario = str(input("El usuario tiene devoluciones pendientes? si/no: "))
if estado_usuario == 'si':
    print("El usuario puede retirar libros")
elif estado_usuario == 'no': 
    print("El usuario tiene pendiente libros a devolver")
else :
    print("Caracter no vállido.")