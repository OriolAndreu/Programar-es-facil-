# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Troba i mostra el valor màxim d'una llista de números introduïda per l'usuari.
# Especificacions d'entrada: Una sèrie de números enters o reals introduïts per l'usuari.

i = 0
contador = 10

primer_numero = int(input("Introdueix un número: "))
numero_max = primer_numero

while (contador -1) > i:
    numero = int(input("Introdueix un número: "))
        
    if numero > numero_max:
        numero_max = numero
    i = i + 1

print(f"El número més gran és: {numero_max}")