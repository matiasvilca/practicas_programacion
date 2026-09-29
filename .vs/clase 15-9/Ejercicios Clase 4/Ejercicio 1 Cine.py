# Un cine ofrece descuento del 50% a menores de 12 años y a jubilados mayores de 65. 
# Consigna: Pedir la edad y mostrar si paga entrada completa o con descuento.

edad = int(input("Ingrese su edad: "))
if edad >= 65 and edad < 90:
    print("Usted tiene un descuento de 50% para jubilados")
elif edad >= 90:
    print ("Usted no tiene descuento por ser demasiado mayor")
elif edad <= 12 and edad >= 1:
        print("Usted tiene un descuento de 50% por ser menor") 
else:
    print("Usted no posee ningún descuento, solo menores y jubilados")
