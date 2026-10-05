# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0
#
# Descripció: Què fa el programa
# Especificacions d'entrada: Dades que rep el programa
frase = input("Introdueix la frase original: ")
buscar = input("Quina paraula vols substituir? ")
substituta = input("Per quina paraula la vols canviar? ")

nova_frase = frase.replace(buscar, substituta)
print("Resultat: " + nova_frase)
