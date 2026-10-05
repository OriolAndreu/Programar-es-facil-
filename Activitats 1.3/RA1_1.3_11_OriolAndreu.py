# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

# Aquest programa converteix minuts en hores completes i minuts restants.

minuts = int(input("Minuts: "))

hores = minuts // 60
restants = minuts % 60

print(str(hores) + " hores i " + str(restants) + " minuts")