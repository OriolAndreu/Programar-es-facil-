# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Demana un número enter a l'usuari i en mostra la taula de multiplicar de l'1 al 10.
# Especificacions d'entrada: Un número enter introduït per l'usuari.

numero = int(input("Introdueix un número entern: "))
for i in range(1, 11):
    resultat = numero * i
    print (f"{numero} x {i} = {resultat}")