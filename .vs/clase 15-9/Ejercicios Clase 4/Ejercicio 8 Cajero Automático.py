# El cajero solo entrega dinero si el saldo es suficiente. 
# Consigna: Pedir saldo y monto a retirar, y mostrar si la operación es posible.

saldo = float(input("Por favor, ingrese su saldo: "))
monto = float(input("Por favor, ingrese el monto a retirar: "))
if monto > saldo: 
    print("Usted no posee el saldo sufiente a retirar.")
else:
    saldo > monto 
    print("Usted puede retirar el monto en su totalidad.")