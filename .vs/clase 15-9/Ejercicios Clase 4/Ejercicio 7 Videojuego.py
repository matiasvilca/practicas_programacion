# Un personaje entra a una zona peligrosa:
# Si tiene más de 50 puntos de vida, puede luchar.
# Si tiene menos, debe huir. Consigna: Pedir los puntos de vida y mostrar la acción.

hp = float(input("Ingrese sus puntos de vida actuales: "))
if hp >= 50:
    print("Puede luchar.")
else:
    hp <50
    print("Debe huir.")
 