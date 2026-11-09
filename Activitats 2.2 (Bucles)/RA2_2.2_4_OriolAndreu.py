# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Genera un número aleatori de l'1 al 100 i dona pistes a l'usuari fins que l'endevina.
# Especificacions d'entrada: Intents successius de nombres enters per part de l'usuari.

import random
a = random.randint(1, 100)
while True:
    b = int(input("Introdueix un número del 1-100: "))
    if b == a:
        print("Has encertat!")
        break
    if a > b:
        print("El número és més gran")

    if a < b:
        print("El número és més petit")
