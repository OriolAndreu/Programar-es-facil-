# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0
#
# Descripció: Què fa el programa
# Especificacions d'entrada: Dades que rep el programa
nom = input("Introdueix el teu nom: ")
cognom = input("Introdueix el teu cognom: ")

# Ajuntem les variables amb el domini del correu (tot en minúscules per seguretat)
correu = nom.lower() + "." + cognom.lower() + "@institut.com"
print("El teu correu és: " + correu)
