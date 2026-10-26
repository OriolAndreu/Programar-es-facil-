# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 26/10/2026
# Descripció: Verifica si un caràcter introduït per l'usuari és una vocal o una consonant.
# Especificacions d'entrada: Una cadena de text d'un sol caràcter (string).

vocals = ["a", "e", "i", "o", "u"]
lletra = input("Introdueix una lletra: ")
# Comentari clau: S'utilitza l'operador lògic 'or' per comprovar si la lletra coincideix amb qualsevol dels elements de la llista.
if lletra == vocals[0] or lletra == vocals[1] or lletra == vocals[2] or lletra == vocals[3] or lletra == vocals[4]:
    print("La lletra és una vocal.")
else:
    print("consonant")
