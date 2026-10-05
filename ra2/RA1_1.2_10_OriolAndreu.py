# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0
#
# Descripció: Què fa el programa
# Especificacions d'entrada: Dades que rep el programa
paraula = input("Introdueix una paraula: ")

# Utilitzem l'slicing [:: -1] que inverteix el text sense fer servir bucles
paraula_inversa = paraula[::-1]
print("Al revés és: " + paraula_inversa)
