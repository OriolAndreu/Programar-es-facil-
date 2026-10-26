# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 26/10/2026
# Descripció: Determina si un número introduït per l'usuari és positiu o negatiu.
# Especificacions d'entrada: Un número real (float).

numero = float(input("Introdueix un número: "))
if (numero > 0):
    print("El número és positiu.")
else:
    # Comentari clau: Si el número no és major que zero (incloent-hi el mateix 0), s'executa el bloc else.
    print("El número és negatiu.")
