# Validar altura de una persona

# Realizar un programa calcule si una persona es de estatura baja, media o alta. En tales casos, informar…

# Si la altura es menor o igual a 150 cm →  “Persona de altura baja”;  
# Si la altura está entre 151 y 170 →  “Persona de altura media”
# Si la altura es mayor al 171 →  “Persona alta”.

altura = float(input("Ingrese su altura expresado en cm: "))
if altura <= 150:
    print("Persona de altura baja")
elif altura >= 151 and altura <= 170:
    print("Persona de altura media")
elif altura > 171:
    print("Persona alta")