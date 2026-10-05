# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

# Aquest programa genera una adreça de correu electrònic a partir del nom i cognom.

nom = input("Nom: ")
cognom = input("Cognom: ")

correu = nom.lower() + "." + cognom.lower() + "@alumnes.cat"

print("Correu: " + correu)