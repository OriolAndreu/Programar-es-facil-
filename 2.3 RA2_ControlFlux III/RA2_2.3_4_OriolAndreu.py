# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Demana un nombre enter positiu i imprimeix tots els nombres parells des de 0 fins a aquest nombre.
# Especificacions d'entrada: Un nombre enter positiu introduït per l'usuari.

try:
    n = int(input("Introdueix un nombre enter positiu: "))
    
    if n > 0:
        print("Nombres parells des de 0 fins a", n, ":")
        # El tercer paràmetre (2) fa que el bucle salti de 2 en 2
        for i in range(0, n + 1, 2):
            print(i)
    else:
        print("Error: El nombre ha de ser positiu (més gran que 0).")

except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")
