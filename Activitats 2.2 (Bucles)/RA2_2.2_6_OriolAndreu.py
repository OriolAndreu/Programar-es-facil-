# Curs: 2026-2027
# Estudis: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Oriol Andreu
# Data: 9/11/2026
# Descripció: Calcula i mostra els primers 10 termes de la seqüència de Fibonacci.
# Especificacions d'entrada: Cap entrada requerida.

a = 0
b = 1

print("Els 10 primers termes de Fibonacci són:")

for i in range(10):
    print(a)  
    
    a, b = b, a + b
