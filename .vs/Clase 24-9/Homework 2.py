# Calificación de un estudiante
# Imagina que eres un profesor y deseas calcular las calificaciones finales de tus estudiantes en función de sus puntajes
# en un examen.  La calificación final se asignará de la siguiente manera: 
# Si el puntaje…

# Es mayor o igual a 90, la calificación es "A".
# Está entre 80 y 89, la calificación es "B".
# Está entre 70 y 79, la calificación es "C".
# Está entre 60 y 69, la calificación es "D".
# Es menor que 60, la calificación es "F".

nota = round(float(input("Por favor ingrese la calificación final (0-100): ")))
if nota >= 90 and nota <= 100:
    print("Su calificación es A.")
elif nota >= 80 and nota < 90:
    print("Su calificación es B.")
elif nota >= 70 and nota < 80:
    print("Su calificación es C.")
elif nota >= 60 and nota < 70:
    print("Su calificación es D.")
elif nota >= 0 and nota < 60:
    print("Su calificación es F.")
else:
    print("Por favor, ingrese un valor válido (0-100).")
    
