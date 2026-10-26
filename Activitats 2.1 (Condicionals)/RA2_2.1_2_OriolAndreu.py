# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 26/10/2026
# Descripció: Comprova si el número sencer introduït és parell o senar.
# Especificacions d'entrada: Un número sencer (int).

numero = int(input("Introdueix un número: "))
# Comentari clau: L'operador % calcula el residu de dividir el número entre 2 per saber si és parell.
parell = numero % 2
if (parell == 0):
    print("El número és parell.")
else:
    print("El número és senar.")
