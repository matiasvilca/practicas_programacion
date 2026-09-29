#Linea por linea
#Así y así
'''Esto me permite 
hacer múltiples líneas
o multilíneas
sin necesidad de usar a a cada rato el hash
funciona también con doble comilla triple
'''
'''edad = 19
if edad >= 18:
    print("Usted es mayor")
'''
"""if es el condicional
else
while es el bucle
for 
def para crear funciones
class para crear clases, más apegado a lo orientado a objetos
import importar códigos de otro archivo de python
return va de la mano con def, es un retorno, devuelve un valor
Identificadores: Case-sensitive-> congruencia en el nombre de variable
nombre = "Ana"
edad = 20
print ("Hola,", nombre )
"""

#Identificadores - Reglas y ejemplos
#nombre_variable, numero123,_mi_var,NombreClase,lista_de_compras,PI
#_mi_var se usa para encapsulamiento, restringir
#cuando creamos clases, usamos pascal case: NombreClase
#incorrectos: 1nombre,mi-var,for,nombre completo,class,$precio
#no usar tildes ni la ñ, más que nada al importar en otros lenguajes sensibles
#False o True van con la primer letra mayúscula
""" =! es para el son diferentes o distinto de
nombre = "Pepe"
if nombre != "Pedro":
    print("Son iguales")
else:
        print("No son iguales")"""
#Conversión de tipos (Casting)
#numero_entero = "10"
#resultado = numero_entero + "5"
#print(resultado) #resultado: 105 porque lo toma como caracteres, los concatena
#frase1 = "que lindo dia " 
#frase2 = "para correr"
#concatenacion = frase1 + frase2
#print(concatenacion) #otro ejemplo de concatenar para unir dos oraciones
#decimal = float("3.14")
#resultado = decimal * 2
#print(resultado)  # 6.28

#saludo = "Hola "
#resultado = saludo * 5
#print(resultado)  # 5 holas

#en booleano, 0 es falso y 1 es verdadero del binario
#print(bool(0))    # False
#print(bool(1))    # True
#print(bool(""))   # False porque no detecta ningún valor, no hay datos

#Input y output
#en input siempre se toma como string
#nombre = input("ingresa tu nombre: ")
#print("Tu nombre es: ", nombre)
#Por si quiero transformarlo a entero:
#numero = int(input("Ingrese un numero: "))
#print(numero)

#num1 = int(input("Ingrese el primer numero: "))
#num2 = int(input("Ingrese el segundo numero: "))
#num3 = int(input("Ingrese el tercer numero: "))
#suma = num1 + num2 + num3
#print("La suma de " ,num1, " y " ,num2, " y " ,num3, "Es: ",suma) #otra forma de hacerlo
#print(f"La suma de {num1} {num2} {num3} es: ", suma) #Otra forma de hacerlo (ambas funcan)

