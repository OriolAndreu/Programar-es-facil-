# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Utilitza un bucle per imprimir un patró triangular d'estrelles creixent de l'1 al 10.
# Especificacions d'entrada: Cap entrada requerida.

a = "          "
for i in range (1,10):
    print(a + " *"*i)
    a = a[:-1]

