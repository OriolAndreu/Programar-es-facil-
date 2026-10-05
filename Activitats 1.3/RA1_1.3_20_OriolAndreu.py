# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

# Aquest programa genera una fitxa d'alumne amb les seves dades principals.

nom = input("Nom: ")
cognom = input("Cognom: ")
edat = int(input("Edat: "))
ciutat = input("Ciutat: ")
cicle = input("Cicle formatiu: ")

nom_complet = nom.upper() + " " + cognom.upper()
correu = nom.lower() + "." + cognom.lower() + "@alumnes.cat"

print("FITXA DE L'ALUMNE")
print("Nom complet: " + nom_complet)
print("Edat l'any vinent: " + str(edat + 1) + " anys")
print("Ciutat: " + ciutat)
print("Cicle: " + cicle)
print("Correu: " + correu)