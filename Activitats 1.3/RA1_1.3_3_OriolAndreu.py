# Administració de Sistemes Informàtics en Xarxa
# Autor: Oriol Andreu
# Data: CURRENT_DAY/10/2026
# Versió: 1.0

preu = float(input("Preu: "))        # Demana el preu i el converteix a decimal
quantitat = int(input("Quantitat: ")) # Demana la quantitat i la converteix a enter
total = preu * quantitat             # Calcula el preu total
print("Total: " + str(total) + " euros") # Mostra el total per pantalla