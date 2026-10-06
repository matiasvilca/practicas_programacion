# El mayor de tres números

# Crea un programa que solicite al usuario ingresar tres números y 
# determine cuál es el mayor de los tres, luego informa al usuario con un mensaje cual es el número mayor.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

print("El número mayor es: ", max(num1,num2,num3))