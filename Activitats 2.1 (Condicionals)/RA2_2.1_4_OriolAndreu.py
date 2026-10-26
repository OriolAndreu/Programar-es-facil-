# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 26/10/2026
# Descripció: Avalua una nota numèrica de l'1 al 10 i indica si correspon a un aprovat o a un suspès.
# Especificacions d'entrada: Un número sencer (int) de l'1 al 10.

a = int(input("Introdueix un número del 1 al 10: "))
# Comentari clau: L'operador >= inclou el número 5 com a nota mínima necessària per aprovar.
if (a >= 5):
    print("Aprovat")
else:
    print("Suspès")
