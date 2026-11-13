# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Mostra la taula de multiplicar d'un nombre enter introduït per l'usuari utilitzant range().
# Especificacions d'entrada: Un nombre enter introduït per l'usuari.

try:
    n = int(input("Introdueix un nombre enter per veure la seva taula de multiplicar: "))
    
    print("Taula de multiplicar del", n)
    
    # Generem els multiplicadors de l'1 al 10
    for i in range(1, 11):
        resultat = n * i
        print(n, "x", i, "=", resultat)

except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")
