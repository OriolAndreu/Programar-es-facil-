# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

# Aquest programa substitueix una paraula per una altra dins d'una frase.

frase = input("Frase: ")
paraula_vella = input("Paraula a substituir: ")
paraula_nova = input("Paraula nova: ")

resultat = frase.replace(paraula_vella, paraula_nova)

print(resultat)