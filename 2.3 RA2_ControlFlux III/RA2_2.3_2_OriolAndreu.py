# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Demana un nombre enter positiu i calcula la suma de tots els nombres des de 1 fins a aquest nombre.
# Especificacions d'entrada: Un nombre enter positiu introduït per l'usuari.

try:
    n = int(input("Introdueix un nombre enter positiu: "))
    
    if n > 0:
        resultat = 0
        # Recorrem els nombres de l'1 fins a n i els anem sumant un per un
        for i in range(1, n + 1):
            resultat = resultat + i
            
        print(f"La suma dels nombres de l'1 al {n} és: {resultat}")
    else:
        print("Error: El nombre ha de ser positiu (més gran que 0).")

except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")
