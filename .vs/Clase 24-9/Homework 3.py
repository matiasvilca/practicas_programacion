# Calculadora de descuento

# Ahora debes generar un programa calcule el descuento de un producto, 
# se le solicita al usuario ingresar el precio original de un producto. 
# Luego, calcula y muestra el precio final después del descuento. 
# Tener en cuenta lo siguiente: 
# Si se ingresa un precio de producto mayor o igual a $12.999 entonces se realizará el descuento del 30%, 
# Sino, se realizará el descuento del 20% sobre el total del producto.

precio_original = float(input("Ingrese precio total: "))
if precio_original >= 12999:
    descuento = precio_original * 0.3
    print(f"Usted tiene un descuento del 30% de '{descuento}' y su precio final es: {precio_original - descuento}")
else:
    descuento = precio_original * 0.2
    print(f"Usted tiene un descuento del 20% de '{descuento}' y su precio final es: {precio_original - descuento}")
    