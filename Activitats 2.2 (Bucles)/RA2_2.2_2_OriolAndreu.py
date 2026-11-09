# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Calcula i mostra la suma dels primers 100 nombres enters positius (de 1 a 100).
# Especificacions d'entrada: Cap entrada requerida.

numero = 1
resultat = numero
while numero <= 100:
    resultat = numero + resultat
    numero += 1
print(resultat)