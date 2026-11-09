# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 2/11/2026
# Descripció: Demana una frase a l'usuari i compta el nombre total de vocals que conté.
# Especificacions d'entrada: Una frase o cadena de text demanada per teclat.

frase = input("Introdueix una frase: ")
vocals = ["a","e","i","o","u"]
comptador = 0

for lletra in frase:
    if lletra in vocals:
        comptador += 1

print(f"hi han {comptador} vocals a la frase introduida.")
            