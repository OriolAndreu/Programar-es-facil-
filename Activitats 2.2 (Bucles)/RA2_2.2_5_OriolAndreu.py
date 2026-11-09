# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Demana un número enter positiu i determina si és un nombre primer o no.
# Especificacions d'entrada: Un número enter positiu introduït per l'usuari.

numero = int (input("Introdueix un número enter: "))
for i in range(2, numero):
    if numero % i == 0:
        print(f"{numero} no és primer")
        break
else:
    print(f"{numero} és primer")