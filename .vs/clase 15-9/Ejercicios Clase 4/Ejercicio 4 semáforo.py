# Un auto se acerca a un semáforo:
# Si está en verde: avanzar.
# Si está en amarillo: decidir si frenar o acelerar.
# Si está en rojo: detenerse. Consigna: Pedir el color y mostrar la acción.

color_semaforo = str(input("Por favor, ingrese el color del semáforo actualmente: "))
if color_semaforo == 'verde':
    print("Usted puede avanzar.")
else:
    if color_semaforo == 'amarillo':
        print("Usted debe frenar/acelerar.")
    else: 
        if color_semaforo == 'rojo':
         print("Por favor, detenerse.")
        else:
            print("Color inválido.")