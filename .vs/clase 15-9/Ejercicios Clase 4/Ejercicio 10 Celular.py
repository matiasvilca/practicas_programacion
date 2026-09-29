# Un celular muestra “Batería baja” si el nivel es menor al 20%. 
# Consigna: Pedir el porcentaje de batería y mostrar el mensaje adecuado.

battery = int(input("Por favor, ingrese el nivel de su batería: "))
if battery < 20 and battery > 0:
    print("Batería baja.")
elif battery >= 20 and battery <= 100:
    print("Batería no tan baja.")
else:
    print("Ingrese un valor adecuado de batería (0-100).")