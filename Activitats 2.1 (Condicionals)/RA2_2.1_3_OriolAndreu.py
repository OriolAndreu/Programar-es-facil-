# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 26/10/2026
# Descripció: Compara tres números diferents i mostra per pantalla quin d'ells és el més gran.
# Especificacions d'entrada: Tres números reals (float) introduïts de manera seqüencial.

a = float(input("Introdueix un número: "))
b = float(input("Introdueix un altre número: "))
c = float(input("Introdueix un número: "))

# Comentari clau: S'inicia una estructura de condició niada per comparar primer el valor d' 'a' respecte a 'b'.
if (a > b):
    if (a > c):
        print("El número més gran és: ", a)
    else:
        if (b > c):
            print("El número més gran és: ", b)
        if b < c:
            print("El número més gran és: ", c)
