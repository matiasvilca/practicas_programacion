# Si el cliente compra más de $10.000, obtiene un 10% de descuento. 
# Consigna: Pedir el monto de la compra y calcular el precio final.

monto_total = float(input("Ingrese el monto total de su compra: "))
if monto_total >= 10000 and monto_total > 0:
    descuento = float((monto_total * 10) / 100)
    monto_final = float(monto_total - descuento)
    print(f"Felicidades, usted tiene un 10 por ciento de descuento, {descuento} y su precio final es: {monto_final} ")
elif monto_total <= 0:
    print("Error, ingrese solo números mayores a 0")
else:
    print("Usted no posee ningún descuento.")
    